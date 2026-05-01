from __future__ import annotations

import logging
import os
from dataclasses import dataclass

import pandas as pd

from core.scanner import SurgeCandidate
from utils.hyperliquid_client import HyperLiquidClient

logger = logging.getLogger(__name__)

VOL_TREND_RISING = "RISING"
VOL_TREND_FLAT = "FLAT"
VOL_TREND_DECLINING = "DECLINING"


@dataclass
class AnalysisResult:
    symbol: str
    price: float
    change_1h_pct: float
    relative_strength_pct: float
    volume_24h_usdt: float
    rsi: float | None
    is_rsi_overbought: bool
    rsi_4h: float | None
    is_4h_overheated: bool
    bb_upper: float | None
    bb_middle: float | None
    bb_lower: float | None
    is_above_bb_upper: bool
    volume_trend: str
    volume_trend_ratio: float
    is_volume_exhaustion: bool
    atr: float | None
    atr_pct: float | None
    funding_rate: float | None
    open_interest_usd: float | None
    oi_change_pct: float | None
    is_confirmed_signal: bool
    reject_reasons: list[str]


class TechnicalAnalyzer:
    def __init__(self, client: HyperLiquidClient) -> None:
        self._client = client
        self._rsi_period = int(os.getenv("RSI_PERIOD", "14"))
        self._rsi_overbought = float(os.getenv("RSI_OVERBOUGHT", "70"))
        self._bb_period = int(os.getenv("BB_PERIOD", "20"))
        self._bb_std = float(os.getenv("BB_STD", "2.0"))
        self._timeframe = os.getenv("ANALYSIS_TIMEFRAME", "1h")
        self._ohlcv_limit = int(os.getenv("OHLCV_LIMIT", "100"))
        self._rsi_4h_max = float(os.getenv("RSI_4H_MAX", "65"))
        self._use_4h_filter = os.getenv("USE_4H_FILTER", "true").lower() != "false"
        self._vol_lookback = int(os.getenv("VOLUME_LOOKBACK", "20"))
        self._vol_rising_ratio = float(os.getenv("VOLUME_RISING_RATIO", "1.8"))
        self._vol_declining_ratio = float(os.getenv("VOLUME_DECLINING_RATIO", "0.8"))
        self._atr_period = int(os.getenv("ATR_PERIOD", "14"))

    def analyze_candidates(self, candidates: list[SurgeCandidate]) -> list[AnalysisResult]:
        results = []
        for candidate in candidates:
            result = self._analyze_single(candidate)
            if result:
                results.append(result)
        return results

    def _analyze_single(self, candidate: SurgeCandidate) -> AnalysisResult | None:
        try:
            ohlcv = self._client.fetch_ohlcv(candidate.symbol, self._timeframe, self._ohlcv_limit)
            required = max(self._rsi_period, self._bb_period, self._atr_period) + 5
            if len(ohlcv) < required:
                return None
            df = self._df(ohlcv)
            rsi_4h = self._fetch_rsi(candidate.symbol, "4h", self._rsi_period + 30)
            funding_rate = self._client.fetch_funding_rate(candidate.symbol)
            oi_usd, oi_change = self._client.fetch_open_interest(candidate.symbol)
            return self._compute(candidate, df, rsi_4h, funding_rate, oi_usd, oi_change)
        except Exception as e:
            logger.error("Analysis failed for %s: %s", candidate.symbol, e)
            return None

    def _compute(
        self,
        candidate: SurgeCandidate,
        df: pd.DataFrame,
        rsi_4h: float | None,
        funding_rate: float | None,
        open_interest_usd: float | None,
        oi_change_pct: float | None,
    ) -> AnalysisResult:
        close = df["close"]
        rsi = self._last_valid(self._rsi(close, self._rsi_period))
        bb_upper_s, bb_middle_s, bb_lower_s = self._bbands(close, self._bb_period, self._bb_std)
        bb_upper = self._last_valid(bb_upper_s)
        bb_middle = self._last_valid(bb_middle_s)
        bb_lower = self._last_valid(bb_lower_s)
        atr = self._last_valid(self._atr(df, self._atr_period))
        atr_pct = atr / candidate.price * 100 if atr and candidate.price > 0 else None
        vol_trend, vol_ratio = self._volume_trend(df["volume"])

        is_rsi_ob = rsi is not None and rsi >= self._rsi_overbought
        is_4h_ok = rsi_4h is not None and rsi_4h < self._rsi_4h_max
        is_above_bb = bb_upper is not None and candidate.price > bb_upper
        reject_reasons: list[str] = []
        if self._use_4h_filter and not is_4h_ok:
            reject_reasons.append(
                f"4h RSI {rsi_4h:.1f} >= {self._rsi_4h_max:.0f}" if rsi_4h is not None else "4h RSI unavailable"
            )

        return AnalysisResult(
            symbol=candidate.symbol,
            price=candidate.price,
            change_1h_pct=candidate.change_1h_pct,
            relative_strength_pct=candidate.relative_strength_pct,
            volume_24h_usdt=candidate.volume_24h_usdt,
            rsi=rsi,
            is_rsi_overbought=is_rsi_ob,
            rsi_4h=rsi_4h,
            is_4h_overheated=is_4h_ok,
            bb_upper=bb_upper,
            bb_middle=bb_middle,
            bb_lower=bb_lower,
            is_above_bb_upper=is_above_bb,
            volume_trend=vol_trend,
            volume_trend_ratio=vol_ratio,
            is_volume_exhaustion=vol_trend != VOL_TREND_RISING,
            atr=atr,
            atr_pct=atr_pct,
            funding_rate=funding_rate,
            open_interest_usd=open_interest_usd,
            oi_change_pct=oi_change_pct,
            is_confirmed_signal=not reject_reasons,
            reject_reasons=reject_reasons,
        )

    def _fetch_rsi(self, symbol: str, timeframe: str, limit: int) -> float | None:
        try:
            ohlcv = self._client.fetch_ohlcv(symbol, timeframe, limit)
            if len(ohlcv) < self._rsi_period + 1:
                return None
            return self._last_valid(self._rsi(self._df(ohlcv)["close"], self._rsi_period))
        except Exception:
            return None

    @staticmethod
    def _df(ohlcv: list[list[float]]) -> pd.DataFrame:
        df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms", utc=True)
        df.set_index("timestamp", inplace=True)
        return df.astype(float)

    @staticmethod
    def _last_valid(series: pd.Series | None) -> float | None:
        if series is None or series.empty:
            return None
        valid = series.dropna()
        return None if valid.empty else float(valid.iloc[-1])

    @staticmethod
    def _rsi(close: pd.Series, period: int) -> pd.Series:
        delta = close.diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        avg_gain = gain.ewm(com=period - 1, min_periods=period).mean()
        avg_loss = loss.ewm(com=period - 1, min_periods=period).mean()
        rs = avg_gain / avg_loss.replace(0, float("nan"))
        return 100 - (100 / (1 + rs))

    @staticmethod
    def _bbands(close: pd.Series, period: int, std_mult: float) -> tuple[pd.Series, pd.Series, pd.Series]:
        middle = close.rolling(period).mean()
        std = close.rolling(period).std(ddof=0)
        return middle + std_mult * std, middle, middle - std_mult * std

    @staticmethod
    def _atr(df: pd.DataFrame, period: int) -> pd.Series:
        high = df["high"]
        low = df["low"]
        close = df["close"]
        prev_close = close.shift(1)
        tr = pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)
        return tr.ewm(com=period - 1, min_periods=period).mean()

    def _volume_trend(self, volume: pd.Series) -> tuple[str, float]:
        if len(volume) < self._vol_lookback + 1:
            return VOL_TREND_FLAT, 1.0
        latest = float(volume.iloc[-1])
        avg = float(volume.iloc[-(self._vol_lookback + 1):-1].mean())
        if avg <= 0:
            return VOL_TREND_FLAT, 1.0
        ratio = latest / avg
        if ratio >= self._vol_rising_ratio:
            return VOL_TREND_RISING, ratio
        if ratio <= self._vol_declining_ratio:
            return VOL_TREND_DECLINING, ratio
        return VOL_TREND_FLAT, ratio
