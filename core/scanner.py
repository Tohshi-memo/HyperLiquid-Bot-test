from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from typing import Any

from utils.hyperliquid_client import HyperLiquidClient

logger = logging.getLogger(__name__)

REGIME_BEARISH = "BEARISH"
REGIME_STAGNANT = "STAGNANT"
REGIME_BULLISH = "BULLISH"


@dataclass
class BTCStatus:
    symbol: str
    price: float
    change_1h_pct: float
    is_bearish: bool
    is_stagnant: bool
    is_signal_active: bool
    regime: str = REGIME_STAGNANT


@dataclass
class SurgeCandidate:
    symbol: str
    price: float
    change_1h_pct: float
    relative_strength_pct: float
    volume_24h_usdt: float
    ticker_raw: dict[str, Any] = field(default_factory=dict)


class MarketScanner:
    BTC_SYMBOL = "BTC"

    def __init__(self, client: HyperLiquidClient) -> None:
        self._client = client
        self._btc_bearish_threshold = float(os.getenv("BTC_BEARISH_THRESHOLD", "-0.5"))
        self._btc_stagnant_threshold = float(os.getenv("BTC_STAGNANT_THRESHOLD", "0.2"))
        self._alt_surge_threshold = float(os.getenv("ALT_SURGE_THRESHOLD", "5.0"))
        self._relative_strength_threshold = float(os.getenv("RELATIVE_STRENGTH_THRESHOLD", "5.0"))
        self._min_volume_usdt = float(os.getenv("MIN_24H_VOLUME_USDT", "1000000"))
        self._max_ohlcv_checks = int(os.getenv("MAX_OHLCV_CHECKS", "50"))
        self._symbols: list[str] = []

    def run_scan(self) -> tuple[BTCStatus, list[SurgeCandidate]]:
        btc = self._check_btc_status()
        if not btc.is_signal_active:
            return btc, []
        return btc, self._scan_surge_alts(btc.change_1h_pct)

    def _check_btc_status(self) -> BTCStatus:
        try:
            ohlcv = self._client.fetch_ohlcv(self.BTC_SYMBOL, timeframe="1h", limit=2)
            if len(ohlcv) < 2:
                raise ValueError("BTC returned fewer than two 1h candles")
            prev_close = float(ohlcv[-2][4])
            curr_close = float(ohlcv[-1][4])
            change = (curr_close - prev_close) / prev_close * 100 if prev_close > 0 else 0.0
            is_bearish = change <= self._btc_bearish_threshold
            is_stagnant = abs(change) <= self._btc_stagnant_threshold
            regime = REGIME_BEARISH if is_bearish else (REGIME_STAGNANT if is_stagnant else REGIME_BULLISH)
            return BTCStatus(self.BTC_SYMBOL, curr_close, change, is_bearish, is_stagnant, True, regime)
        except Exception as e:
            logger.error("Failed to read BTC status: %s", e)
            return BTCStatus(self.BTC_SYMBOL, 0.0, 0.0, False, False, False)

    def _scan_surge_alts(self, btc_change_1h: float) -> list[SurgeCandidate]:
        if not self._symbols:
            self._symbols = self._client.fetch_swap_usdt_symbols()

        symbols = [s for s in self._symbols if s != self.BTC_SYMBOL]
        tickers = self._client.fetch_tickers(symbols)
        liquid = [
            (symbol, ticker)
            for symbol, ticker in tickers.items()
            if float(ticker.get("last") or 0) > 0
            and float(ticker.get("quoteVolume") or 0) >= self._min_volume_usdt
        ]
        liquid.sort(key=lambda row: float(row[1].get("percentage") or 0), reverse=True)

        candidates: list[SurgeCandidate] = []
        for symbol, ticker in liquid[: self._max_ohlcv_checks]:
            try:
                ohlcv = self._client.fetch_ohlcv(symbol, timeframe="1h", limit=2)
                if len(ohlcv) < 2:
                    continue
                prev_close = float(ohlcv[-2][4])
                curr_close = float(ohlcv[-1][4])
                if prev_close <= 0:
                    continue
                change = (curr_close - prev_close) / prev_close * 100
                relative = change - btc_change_1h
                if change < self._alt_surge_threshold:
                    continue
                if relative < self._relative_strength_threshold:
                    continue
                candidates.append(
                    SurgeCandidate(
                        symbol=symbol,
                        price=float(ticker.get("last") or curr_close),
                        change_1h_pct=change,
                        relative_strength_pct=relative,
                        volume_24h_usdt=float(ticker.get("quoteVolume") or 0),
                        ticker_raw=ticker,
                    )
                )
            except Exception as e:
                logger.debug("Skipping %s during scan: %s", symbol, e)

        candidates.sort(key=lambda c: c.relative_strength_pct, reverse=True)
        return candidates
