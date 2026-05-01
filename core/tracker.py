from __future__ import annotations

import json
import logging
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from utils.hyperliquid_client import HyperLiquidClient

logger = logging.getLogger(__name__)
TRACKING_FILE = Path("data/tracking.json")

OUTCOME_ACTIVE = "ACTIVE"
OUTCOME_TP_HIT = "TP_HIT"
OUTCOME_SL_HIT = "SL_HIT"
OUTCOME_EXPIRED = "EXPIRED"


@dataclass
class PricePoint:
    timestamp: str
    price: float
    change_pct: float


@dataclass
class TrackedSymbol:
    symbol: str
    detected_at: str
    expires_at: str
    detection_price: float
    detection_rsi: float | None
    detection_1h_change: float
    sl_price: float
    tp_price: float
    conviction: str = "MEDIUM"
    market_regime: str = "UNKNOWN"
    detection_rel_strength: float = 0.0
    outcome: str = OUTCOME_ACTIVE
    outcome_at: str | None = None
    outcome_price: float | None = None
    prices: list[PricePoint] = field(default_factory=list)

    @property
    def current_price(self) -> float:
        return self.prices[-1].price if self.prices else self.detection_price

    @property
    def current_change_pct(self) -> float:
        return self.prices[-1].change_pct if self.prices else 0.0

    @property
    def is_expired(self) -> bool:
        return datetime.now(timezone.utc) >= datetime.fromisoformat(self.expires_at)

    @property
    def is_closed(self) -> bool:
        return self.outcome != OUTCOME_ACTIVE

    @property
    def hours_tracked(self) -> float:
        return (datetime.now(timezone.utc) - datetime.fromisoformat(self.detected_at)).total_seconds() / 3600


class SymbolTracker:
    def __init__(self) -> None:
        self._tracking_hours = int(os.getenv("TRACKING_HOURS", "24"))
        self._symbols: dict[str, TrackedSymbol] = {}
        self._load()

    def add_if_new(
        self,
        symbol: str,
        detection_price: float,
        rsi: float | None,
        change_1h: float,
        sl_price: float,
        tp_price: float,
        conviction: str = "MEDIUM",
        market_regime: str = "UNKNOWN",
        detection_rel_strength: float = 0.0,
    ) -> bool:
        existing = self._symbols.get(symbol)
        if existing and not existing.is_closed and not existing.is_expired:
            return False
        now = datetime.now(timezone.utc)
        self._symbols[symbol] = TrackedSymbol(
            symbol=symbol,
            detected_at=now.isoformat(),
            expires_at=(now + timedelta(hours=self._tracking_hours)).isoformat(),
            detection_price=detection_price,
            detection_rsi=rsi,
            detection_1h_change=change_1h,
            sl_price=sl_price,
            tp_price=tp_price,
            conviction=conviction,
            market_regime=market_regime,
            detection_rel_strength=detection_rel_strength,
        )
        return True

    def update_prices(self, client: "HyperLiquidClient") -> list[TrackedSymbol]:
        closed: list[TrackedSymbol] = []
        now = datetime.now(timezone.utc).isoformat()
        for tracked in self.active_symbols():
            try:
                ohlcv = client.fetch_ohlcv(tracked.symbol, "1m", 6)
                if not ohlcv:
                    continue
                high = max(float(c[2]) for c in ohlcv)
                low = min(float(c[3]) for c in ohlcv)
                close = float(ohlcv[-1][4])
            except Exception as e:
                logger.debug("Could not update %s: %s", tracked.symbol, e)
                continue

            change = (close - tracked.detection_price) / tracked.detection_price * 100
            tracked.prices.append(PricePoint(now, close, change))
            tracked.prices = tracked.prices[-200:]

            sl_hit = high >= tracked.sl_price
            tp_hit = low <= tracked.tp_price
            if sl_hit:
                tracked.outcome = OUTCOME_SL_HIT
                tracked.outcome_at = now
                tracked.outcome_price = tracked.sl_price
                closed.append(tracked)
            elif tp_hit:
                tracked.outcome = OUTCOME_TP_HIT
                tracked.outcome_at = now
                tracked.outcome_price = tracked.tp_price
                closed.append(tracked)
        return closed

    def clean_expired(self) -> list[TrackedSymbol]:
        closed: list[TrackedSymbol] = []
        now = datetime.now(timezone.utc).isoformat()
        for symbol, tracked in list(self._symbols.items()):
            if tracked.is_closed:
                closed.append(tracked)
                del self._symbols[symbol]
            elif tracked.is_expired:
                tracked.outcome = OUTCOME_EXPIRED
                tracked.outcome_at = now
                tracked.outcome_price = tracked.current_price
                closed.append(tracked)
                del self._symbols[symbol]
        return closed

    def active_symbols(self) -> list[TrackedSymbol]:
        return [s for s in self._symbols.values() if not s.is_closed and not s.is_expired]

    def save(self) -> None:
        TRACKING_FILE.parent.mkdir(parents=True, exist_ok=True)
        payload = {}
        for symbol, tracked in self._symbols.items():
            row = asdict(tracked)
            payload[symbol] = row
        TRACKING_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def _load(self) -> None:
        if not TRACKING_FILE.exists():
            return
        try:
            data = json.loads(TRACKING_FILE.read_text(encoding="utf-8"))
            for symbol, entry in data.items():
                entry["prices"] = [PricePoint(**p) for p in entry.get("prices", [])]
                self._symbols[symbol] = TrackedSymbol(**entry)
        except Exception as e:
            logger.warning("Failed to load tracking data: %s", e)
