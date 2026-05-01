"""
HyperLiquid client adapter.

The scanner was originally written against a ccxt-like futures client.  This
adapter keeps that small surface area while using the official HyperLiquid
Python SDK underneath.
"""
from __future__ import annotations

import logging
import math
import os
import time
from decimal import Decimal, ROUND_DOWN
from typing import Any

import eth_account
from hyperliquid.exchange import Exchange
from hyperliquid.info import Info
from hyperliquid.utils import constants

logger = logging.getLogger(__name__)


TIMEFRAME_MS: dict[str, int] = {
    "1m": 60_000,
    "3m": 3 * 60_000,
    "5m": 5 * 60_000,
    "15m": 15 * 60_000,
    "30m": 30 * 60_000,
    "1h": 60 * 60_000,
    "2h": 2 * 60 * 60_000,
    "4h": 4 * 60 * 60_000,
    "8h": 8 * 60 * 60_000,
    "12h": 12 * 60 * 60_000,
    "1d": 24 * 60 * 60_000,
    "3d": 3 * 24 * 60 * 60_000,
    "1w": 7 * 24 * 60 * 60_000,
    "1M": 31 * 24 * 60 * 60_000,
}


class HyperLiquidExchangeAdapter:
    """Small ccxt-like facade used by the migrated executor and tools."""

    def __init__(self, client: "HyperLiquidClient") -> None:
        self._client = client

    def fetch_positions(self) -> list[dict[str, Any]]:
        return self._client.fetch_positions()

    def market(self, symbol: str) -> dict[str, Any]:
        return self._client.market(symbol)

    def amount_to_precision(self, symbol: str, amount: float) -> str:
        return self._client.amount_to_precision(symbol, amount)

    def price_to_precision(self, symbol: str, price: float) -> str:
        return self._client.price_to_precision(symbol, price)

    def set_leverage(self, leverage: int, symbol: str) -> Any:
        return self._client.set_leverage(symbol, leverage)


class HyperLiquidClient:
    """Official HyperLiquid SDK wrapper with the methods used by this bot."""

    RATE_LIMIT_SAFETY_FACTOR: float = 1.1

    def __init__(self) -> None:
        self._testnet = _env_bool("HYPERLIQUID_TESTNET", False)
        self._base_url = os.getenv("HYPERLIQUID_API_URL") or (
            constants.TESTNET_API_URL if self._testnet else constants.MAINNET_API_URL
        )
        self._dex = os.getenv("HYPERLIQUID_DEX", "")
        self._timeout = float(os.getenv("HYPERLIQUID_TIMEOUT_SECONDS", "10"))
        self._min_order_notional = float(os.getenv("HYPERLIQUID_MIN_ORDER_NOTIONAL_USDC", "10"))
        self._market_slippage = float(os.getenv("HYPERLIQUID_MARKET_SLIPPAGE", "0.05"))
        self._vault_address = os.getenv("HYPERLIQUID_VAULT_ADDRESS") or None
        self._account_address = os.getenv("HYPERLIQUID_ACCOUNT_ADDRESS") or None
        self._private_key = os.getenv("HYPERLIQUID_PRIVATE_KEY", "")

        self._info = Info(self._base_url, skip_ws=True, timeout=self._timeout)
        self._exchange_sdk: Exchange | None = None
        self._wallet_address: str | None = None
        if self._private_key:
            wallet = eth_account.Account.from_key(self._private_key)
            self._wallet_address = wallet.address
            self._exchange_sdk = Exchange(
                wallet,
                base_url=self._base_url,
                vault_address=self._vault_address,
                account_address=self._account_address,
                timeout=self._timeout,
            )
            logger.info(
                "HyperLiquid client initialized in authenticated mode (%s).",
                "testnet" if self._testnet else "mainnet",
            )
        else:
            logger.info(
                "HyperLiquid client initialized in public mode (%s).",
                "testnet" if self._testnet else "mainnet",
            )

        self._exchange_adapter = HyperLiquidExchangeAdapter(self)
        self._meta: dict[str, Any] = {"universe": []}
        self._asset_ctxs_by_coin: dict[str, dict[str, Any]] = {}
        self._refresh_market_cache()

    # ------------------------------------------------------------------
    # Market data
    # ------------------------------------------------------------------

    def fetch_markets(self) -> list[dict[str, Any]]:
        self._refresh_market_cache()
        return [
            {
                "symbol": coin,
                "base": coin,
                "quote": "USDC",
                "type": "swap",
                "active": True,
                "contractSize": 1.0,
                "precision": {"amount": meta.get("szDecimals", 0)},
                "limits": {
                    "amount": {"min": 10 ** -int(meta.get("szDecimals", 0))},
                    "cost": {"min": self._min_order_notional},
                },
                "info": meta,
            }
            for coin, meta in self._universe_by_coin().items()
        ]

    def fetch_swap_usdt_symbols(self) -> list[str]:
        """Return active HyperLiquid perpetual coins.

        The method name is kept for compatibility with the original scanner.
        HyperLiquid perps are USDC margined, so symbols are plain coins such as
        BTC, ETH, SOL.
        """
        mids = self._call_with_retry(self._info.all_mids, self._dex)
        universe = self._universe_by_coin()
        return sorted(coin for coin in universe if coin in mids)

    def fetch_tickers(self, symbols: list[str] | None = None) -> dict[str, Any]:
        self._refresh_market_cache()
        mids = self._call_with_retry(self._info.all_mids, self._dex)
        target = symbols or self.fetch_swap_usdt_symbols()
        tickers: dict[str, Any] = {}

        for symbol in target:
            coin = self._coin(symbol)
            ctx = self._asset_ctxs_by_coin.get(coin, {})
            last = _safe_float(
                mids.get(coin)
                or ctx.get("midPx")
                or ctx.get("markPx")
                or ctx.get("oraclePx")
            )
            prev_day = _safe_float(ctx.get("prevDayPx"))
            pct = ((last - prev_day) / prev_day * 100) if last > 0 and prev_day > 0 else 0.0
            quote_volume = _safe_float(ctx.get("dayNtlVlm"))

            tickers[coin] = {
                "symbol": coin,
                "last": last,
                "percentage": pct,
                "quoteVolume": quote_volume,
                "info": ctx,
            }

        return tickers

    def fetch_ohlcv(
        self,
        symbol: str,
        timeframe: str = "1h",
        limit: int = 100,
    ) -> list[list[float]]:
        coin = self._coin(symbol)
        interval_ms = TIMEFRAME_MS.get(timeframe)
        if interval_ms is None:
            raise ValueError(f"Unsupported HyperLiquid candle interval: {timeframe}")

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - interval_ms * max(limit + 5, limit * 2)
        rows = self._call_with_retry(
            self._info.candles_snapshot,
            coin,
            timeframe,
            start_ms,
            end_ms,
        )
        rows = sorted(rows or [], key=lambda x: int(x.get("t", 0)))[-limit:]
        return [
            [
                int(row["t"]),
                float(row["o"]),
                float(row["h"]),
                float(row["l"]),
                float(row["c"]),
                float(row["v"]),
            ]
            for row in rows
        ]

    def fetch_order_book(self, symbol: str, limit: int = 20) -> dict[str, Any]:
        book = self._call_with_retry(self._info.l2_snapshot, self._coin(symbol))
        levels = book.get("levels") or [[], []]
        bids = levels[0] if len(levels) > 0 else []
        asks = levels[1] if len(levels) > 1 else []
        return {
            "bids": [[float(x["px"]), float(x["sz"])] for x in bids[:limit]],
            "asks": [[float(x["px"]), float(x["sz"])] for x in asks[:limit]],
            "timestamp": book.get("time"),
            "info": book,
        }

    def fetch_funding_rate(self, symbol: str) -> float | None:
        ctx = self._ctx(symbol)
        if not ctx:
            return None
        funding = ctx.get("funding")
        return float(funding) * 100 if funding is not None else None

    def fetch_open_interest(self, symbol: str) -> tuple[float | None, float | None]:
        ctx = self._ctx(symbol)
        if not ctx:
            return None, None
        open_interest = _safe_float(ctx.get("openInterest"), default=math.nan)
        price = _safe_float(ctx.get("midPx") or ctx.get("markPx") or ctx.get("oraclePx"), default=math.nan)
        if math.isnan(open_interest):
            return None, None
        oi_usd = open_interest * price if not math.isnan(price) and price > 0 else open_interest
        return oi_usd, None

    def fetch_long_short_ratio(self, symbol: str) -> float | None:
        # HyperLiquid does not expose a direct global long/short account ratio
        # through the public Info API. Keep the optional metric empty.
        return None

    # ------------------------------------------------------------------
    # Private account and orders
    # ------------------------------------------------------------------

    def fetch_balance(self) -> dict[str, Any]:
        state = self._user_state()
        margin = state.get("marginSummary") or state.get("crossMarginSummary") or {}
        total = _safe_float(margin.get("accountValue"))
        used = _safe_float(margin.get("totalMarginUsed"))
        free = _safe_float(state.get("withdrawable"), max(total - used, 0.0))
        coin_balance = {"total": total, "free": free, "used": used}
        return {"USDC": coin_balance, "USDT": coin_balance, "info": state}

    def fetch_positions(self) -> list[dict[str, Any]]:
        state = self._user_state()
        mids = self._call_with_retry(self._info.all_mids, self._dex)
        positions: list[dict[str, Any]] = []
        for item in state.get("assetPositions", []):
            pos = item.get("position", {})
            coin = pos.get("coin")
            szi = _safe_float(pos.get("szi"))
            if not coin or szi == 0:
                continue
            contracts = abs(szi)
            notional = _safe_float(pos.get("positionValue"))
            mark = _safe_float(mids.get(coin), notional / contracts if contracts else 0.0)
            leverage = pos.get("leverage") or {}
            roe = _safe_float(pos.get("returnOnEquity"))
            positions.append(
                {
                    "symbol": coin,
                    "side": "long" if szi > 0 else "short",
                    "contracts": contracts,
                    "notional": notional,
                    "entryPrice": _safe_float(pos.get("entryPx")),
                    "markPrice": mark,
                    "leverage": _safe_float(leverage.get("value")),
                    "unrealizedPnl": _safe_float(pos.get("unrealizedPnl")),
                    "percentage": roe * 100,
                    "info": pos,
                }
            )
        return positions

    def create_order(
        self,
        symbol: str,
        order_type: str,
        side: str,
        amount: float,
        price: float | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        params = dict(params or {})
        exchange = self._require_exchange()
        coin = self._coin(symbol)
        is_buy = side.lower() == "buy"
        reduce_only = bool(params.get("reduceOnly", False))
        slippage = float(params.get("slippage", self._market_slippage))

        if order_type.lower() == "market":
            if reduce_only:
                raw = exchange.market_close(coin, sz=amount, slippage=slippage)
            else:
                raw = exchange.market_open(coin, is_buy=is_buy, sz=amount, slippage=slippage)
        else:
            if price is None:
                raise ValueError("price is required for non-market HyperLiquid orders")
            raw = exchange.order(
                coin,
                is_buy=is_buy,
                sz=amount,
                limit_px=float(price),
                order_type={"limit": {"tif": params.get("tif", "Gtc")}},
                reduce_only=reduce_only,
            )

        attached: list[dict[str, Any]] = []
        if not reduce_only:
            for key, tpsl in (("stopLossPrice", "sl"), ("takeProfitPrice", "tp")):
                trigger_px = params.get(key)
                if trigger_px is None:
                    continue
                trigger_px = float(trigger_px)
                attached.append(
                    exchange.order(
                        coin,
                        is_buy=not is_buy,
                        sz=amount,
                        limit_px=trigger_px,
                        order_type={
                            "trigger": {
                                "triggerPx": trigger_px,
                                "isMarket": True,
                                "tpsl": tpsl,
                            }
                        },
                        reduce_only=True,
                    )
                )

        return {
            "id": _first_order_id(raw),
            "symbol": coin,
            "side": side,
            "amount": amount,
            "raw": raw,
            "attached": attached,
        }

    def set_leverage(self, symbol: str, leverage: int) -> Any:
        exchange = self._require_exchange()
        return exchange.update_leverage(int(leverage), self._coin(symbol), is_cross=True)

    # ------------------------------------------------------------------
    # Market metadata and precision
    # ------------------------------------------------------------------

    def market(self, symbol: str) -> dict[str, Any]:
        coin = self._coin(symbol)
        meta = self._universe_by_coin().get(coin)
        if meta is None:
            self._refresh_market_cache()
            meta = self._universe_by_coin().get(coin)
        if meta is None:
            raise KeyError(f"Unknown HyperLiquid coin: {coin}")
        sz_decimals = int(meta.get("szDecimals", 0))
        return {
            "symbol": coin,
            "base": coin,
            "quote": "USDC",
            "type": "swap",
            "contractSize": 1.0,
            "precision": {"amount": sz_decimals},
            "limits": {
                "amount": {"min": 10 ** -sz_decimals},
                "cost": {"min": self._min_order_notional},
            },
            "info": meta,
        }

    def amount_to_precision(self, symbol: str, amount: float) -> str:
        sz_decimals = int(self.market(symbol)["precision"]["amount"])
        quant = Decimal("1") if sz_decimals <= 0 else Decimal("1").scaleb(-sz_decimals)
        rounded = Decimal(str(amount)).quantize(quant, rounding=ROUND_DOWN)
        return _format_decimal(rounded)

    def price_to_precision(self, symbol: str, price: float) -> str:
        sz_decimals = int(self.market(symbol)["precision"]["amount"])
        decimals = max(0, 6 - sz_decimals)
        sig_price = float(f"{float(price):.5g}")
        return _format_float(round(sig_price, decimals), decimals)

    @property
    def exchange(self) -> HyperLiquidExchangeAdapter:
        return self._exchange_adapter

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _refresh_market_cache(self) -> None:
        try:
            if self._dex:
                self._meta = self._call_with_retry(self._info.meta, self._dex)
                self._asset_ctxs_by_coin = {}
                return
            meta, ctxs = self._call_with_retry(self._info.meta_and_asset_ctxs)
            self._meta = meta
            self._asset_ctxs_by_coin = {
                asset.get("name"): dict(ctx)
                for asset, ctx in zip(meta.get("universe", []), ctxs)
                if asset.get("name")
            }
        except Exception:
            logger.exception("Failed to refresh HyperLiquid market metadata")
            raise

    def _ctx(self, symbol: str) -> dict[str, Any]:
        coin = self._coin(symbol)
        ctx = self._asset_ctxs_by_coin.get(coin)
        if ctx is None:
            self._refresh_market_cache()
            ctx = self._asset_ctxs_by_coin.get(coin)
        return ctx or {}

    def _universe_by_coin(self) -> dict[str, dict[str, Any]]:
        return {
            row["name"]: row
            for row in self._meta.get("universe", [])
            if row.get("name")
        }

    def _coin(self, symbol: str) -> str:
        if "/" in symbol:
            return symbol.split("/", 1)[0]
        return symbol

    def _account_for_reads(self) -> str:
        account = self._account_address or self._vault_address or self._wallet_address
        if not account:
            raise RuntimeError(
                "Private HyperLiquid read requires HYPERLIQUID_ACCOUNT_ADDRESS "
                "or HYPERLIQUID_PRIVATE_KEY."
            )
        return account

    def _user_state(self) -> dict[str, Any]:
        return self._call_with_retry(self._info.user_state, self._account_for_reads(), self._dex)

    def _require_exchange(self) -> Exchange:
        if self._exchange_sdk is None:
            raise RuntimeError(
                "Live trading requires HYPERLIQUID_PRIVATE_KEY. Keep DRY_RUN=true "
                "until the API wallet is configured."
            )
        return self._exchange_sdk

    def _call_with_retry(
        self,
        func: Any,
        *args: Any,
        max_retries: int = 3,
        base_sleep: float = 1.0,
    ) -> Any:
        for attempt in range(max_retries):
            try:
                result = func(*args)
                time.sleep(0.12 * self.RATE_LIMIT_SAFETY_FACTOR)
                return result
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                wait_time = base_sleep * (2 ** attempt)
                logger.warning(
                    "HyperLiquid API call failed (attempt %d/%d): %s. Sleeping %.1fs.",
                    attempt + 1,
                    max_retries,
                    e,
                    wait_time,
                )
                time.sleep(wait_time)

        raise RuntimeError(f"Max retries exceeded for {getattr(func, '__name__', func)}")


def _env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value) if value is not None else default
    except (TypeError, ValueError):
        return default


def _format_decimal(value: Decimal) -> str:
    return format(value.normalize(), "f")


def _format_float(value: float, decimals: int) -> str:
    text = f"{value:.{decimals}f}" if decimals > 0 else f"{value:.0f}"
    return text.rstrip("0").rstrip(".") if "." in text else text


def _first_order_id(raw: Any) -> Any:
    try:
        statuses = raw["response"]["data"]["statuses"]
        if not statuses:
            return None
        first = statuses[0]
        if "resting" in first:
            return first["resting"].get("oid")
        if "filled" in first:
            return first["filled"].get("oid")
        return first.get("oid")
    except Exception:
        return None
