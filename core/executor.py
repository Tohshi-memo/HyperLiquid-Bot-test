from __future__ import annotations

import logging
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from core.analyzer import AnalysisResult
from utils.hyperliquid_client import HyperLiquidClient

logger = logging.getLogger(__name__)


@dataclass
class TradeProposal:
    symbol: str
    direction: str
    entry_price: float
    stop_loss: float
    take_profit: float
    sl_pct: float
    tp_pct: float
    rsi_at_entry: float | None
    bb_upper_at_entry: float | None
    volume_24h_usdt: float
    change_1h_pct: float
    created_at: str = ""

    def __post_init__(self) -> None:
        if not self.created_at:
            self.created_at = datetime.now(timezone.utc).isoformat()


class BaseExecutor(ABC):
    @abstractmethod
    def execute(self, proposal: TradeProposal) -> dict[str, Any]:
        ...

    @abstractmethod
    def close_position(self, symbol: str, amount: float) -> dict[str, Any]:
        ...


class DryRunExecutor(BaseExecutor):
    def execute(self, proposal: TradeProposal) -> dict[str, Any]:
        logger.info(
            "[DRY RUN] %s %s entry=%.8g sl=%.8g tp=%.8g sl_pct=%.2f tp_pct=%.2f",
            proposal.direction.upper(),
            proposal.symbol,
            proposal.entry_price,
            proposal.stop_loss,
            proposal.take_profit,
            proposal.sl_pct,
            proposal.tp_pct,
        )
        return {
            "status": "dry_run",
            "symbol": proposal.symbol,
            "entry_price": proposal.entry_price,
            "stop_loss": proposal.stop_loss,
            "take_profit": proposal.take_profit,
        }

    def close_position(self, symbol: str, amount: float) -> dict[str, Any]:
        logger.info("[DRY RUN] close %s amount=%.8g", symbol, amount)
        return {"status": "dry_run_close", "symbol": symbol, "amount": amount}


class LiveExecutor(BaseExecutor):
    def __init__(self, client: HyperLiquidClient) -> None:
        self._client = client
        self._base_risk_pct = float(os.getenv("LIVE_BASE_RISK_PCT", "0.5"))
        self._max_risk_pct = float(os.getenv("LIVE_MAX_RISK_PCT", "1.5"))
        self._max_leverage = float(os.getenv("LIVE_MAX_LEVERAGE", "3.0"))
        self._min_balance_usdt = float(os.getenv("LIVE_MIN_BALANCE_USDT", "5.0"))
        self._max_open_positions = int(os.getenv("LIVE_MAX_OPEN_POSITIONS", "3"))

    def execute(self, proposal: TradeProposal) -> dict[str, Any]:
        if proposal.direction.lower() != "short":
            return {"status": "skipped_direction", "reason": "live executor is short-only"}

        balance = self._client.fetch_balance()
        usdc = balance.get("USDC") or balance.get("USDT") or {}
        free_usdc = float(usdc.get("free") or 0.0)
        total_usdc = float(usdc.get("total") or 0.0)
        if free_usdc < self._min_balance_usdt:
            return {"status": "skipped_low_balance", "free_usdc": free_usdc}

        open_positions = [
            p for p in self._client.exchange.fetch_positions()
            if float(p.get("contracts") or 0) > 0
        ]
        if any(p.get("symbol") == proposal.symbol for p in open_positions):
            return {"status": "skipped_already_open", "symbol": proposal.symbol}
        if len(open_positions) >= self._max_open_positions:
            return {"status": "skipped_max_positions", "open_count": len(open_positions)}

        if proposal.stop_loss <= proposal.entry_price:
            return {"status": "error", "reason": "short stop loss must be above entry"}
        if proposal.take_profit >= proposal.entry_price:
            return {"status": "error", "reason": "short take profit must be below entry"}

        risk_pct = min(self._base_risk_pct, self._max_risk_pct)
        risk_usdc = total_usdc * risk_pct / 100
        notional = risk_usdc / (proposal.sl_pct / 100)
        notional = min(notional, total_usdc * self._max_leverage)
        amount = notional / proposal.entry_price

        market = self._client.exchange.market(proposal.symbol)
        min_amount = (market.get("limits", {}).get("amount") or {}).get("min")
        min_cost = (market.get("limits", {}).get("cost") or {}).get("min")
        if min_amount is not None and amount < float(min_amount):
            return {"status": "skipped_below_min_amount", "amount": amount, "min_amount": min_amount}
        if min_cost is not None and notional < float(min_cost):
            return {"status": "skipped_below_min_cost", "notional": notional, "min_cost": min_cost}

        amount = float(self._client.exchange.amount_to_precision(proposal.symbol, amount))
        sl_price = float(self._client.exchange.price_to_precision(proposal.symbol, proposal.stop_loss))
        tp_price = float(self._client.exchange.price_to_precision(proposal.symbol, proposal.take_profit))

        try:
            self._client.exchange.set_leverage(int(self._max_leverage), proposal.symbol)
        except Exception as e:
            logger.warning("set_leverage failed for %s: %s", proposal.symbol, e)

        order = self._client.create_order(
            symbol=proposal.symbol,
            order_type="market",
            side="sell",
            amount=amount,
            params={
                "stopLossPrice": sl_price,
                "takeProfitPrice": tp_price,
                "reduceOnly": False,
            },
        )
        logger.warning(
            "[LIVE] short %s amount=%.8g notional=$%.2f sl=%.8g tp=%.8g order=%s",
            proposal.symbol,
            amount,
            notional,
            sl_price,
            tp_price,
            order.get("id"),
        )
        return {
            "status": "ok",
            "order_id": order.get("id"),
            "symbol": proposal.symbol,
            "amount": amount,
            "notional_usdc": notional,
            "risk_usdc": risk_usdc,
            "sl_price": sl_price,
            "tp_price": tp_price,
            "raw": order,
        }

    def close_position(self, symbol: str, amount: float) -> dict[str, Any]:
        order = self._client.create_order(symbol, "market", "buy", amount, params={"reduceOnly": True})
        return {"status": "ok", "order_id": order.get("id"), "raw": order}


class ProposalBuilder:
    def __init__(self) -> None:
        self._fixed_sl_pct = float(os.getenv("STOP_LOSS_PCT", "2.0"))
        self._fixed_tp_pct = float(os.getenv("TAKE_PROFIT_PCT", "4.0"))
        self._use_atr_sl = os.getenv("USE_ATR_SL", "true").lower() != "false"
        self._atr_sl_mult = float(os.getenv("ATR_SL_MULT", "1.5"))
        self._atr_sl_min = float(os.getenv("ATR_SL_MIN", "1.0"))
        self._atr_sl_max = float(os.getenv("ATR_SL_MAX", "4.0"))
        self._rr_ratio = float(os.getenv("RISK_REWARD_RATIO", "2.0"))

    def build(self, result: AnalysisResult) -> TradeProposal:
        entry = result.price
        if self._use_atr_sl and result.atr_pct and result.atr_pct > 0:
            sl_pct = max(self._atr_sl_min, min(result.atr_pct * self._atr_sl_mult, self._atr_sl_max))
        else:
            sl_pct = self._fixed_sl_pct
        tp_pct = sl_pct * self._rr_ratio if self._use_atr_sl else self._fixed_tp_pct
        return TradeProposal(
            symbol=result.symbol,
            direction="short",
            entry_price=entry,
            stop_loss=entry * (1 + sl_pct / 100),
            take_profit=entry * (1 - tp_pct / 100),
            sl_pct=sl_pct,
            tp_pct=tp_pct,
            rsi_at_entry=result.rsi,
            bb_upper_at_entry=result.bb_upper,
            volume_24h_usdt=result.volume_24h_usdt,
            change_1h_pct=result.change_1h_pct,
        )


class ExecutorFactory:
    @staticmethod
    def create(client: HyperLiquidClient) -> BaseExecutor:
        dry_run = os.getenv("DRY_RUN", "true").lower() != "false"
        if dry_run:
            logger.info("Executor mode: DRY RUN")
            return DryRunExecutor()
        logger.warning("Executor mode: LIVE - real HyperLiquid orders can be placed.")
        return LiveExecutor(client)
