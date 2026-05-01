from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

from core.tracker import OUTCOME_SL_HIT, OUTCOME_TP_HIT, TrackedSymbol

STATS_FILE = Path("data/stats.json")


@dataclass
class TradeRecord:
    symbol: str
    outcome: str
    entry_price: float
    exit_price: float
    pnl_pct: float
    closed_at: str


@dataclass
class StatsSummary:
    total: int
    wins: int
    losses: int
    win_rate: float
    avg_pnl_pct: float
    recent_losses: int


class StatsManager:
    def __init__(self) -> None:
        self._lookback_hours = int(os.getenv("CIRCUIT_BREAKER_LOOKBACK_HOURS", "48"))
        self._records: list[TradeRecord] = []
        self._load()

    def record_many(self, symbols: list[TrackedSymbol]) -> list[TradeRecord]:
        records = [self._from_tracked(s) for s in symbols]
        self._records.extend(records)
        self.save()
        return records

    def summary(self, recent_window: int = 10) -> StatsSummary:
        total = len(self._records)
        wins = sum(1 for r in self._records if r.outcome == OUTCOME_TP_HIT)
        losses = sum(1 for r in self._records if r.outcome == OUTCOME_SL_HIT)
        avg = sum(r.pnl_pct for r in self._records) / total if total else 0.0
        recent = self._recent_records()[-recent_window:]
        recent_losses = sum(1 for r in recent if r.outcome == OUTCOME_SL_HIT)
        return StatsSummary(
            total=total,
            wins=wins,
            losses=losses,
            win_rate=wins / total * 100 if total else 0.0,
            avg_pnl_pct=avg,
            recent_losses=recent_losses,
        )

    def had_sl_within(self, symbol: str, hours: int) -> bool:
        cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
        for record in reversed(self._records):
            if record.symbol != symbol or record.outcome != OUTCOME_SL_HIT:
                continue
            if datetime.fromisoformat(record.closed_at) >= cutoff:
                return True
        return False

    def circuit_breaker_active(self, window: int, loss_threshold: int) -> bool:
        recent = self._recent_records()[-window:]
        if len(recent) < window:
            return False
        return sum(1 for r in recent if r.outcome == OUTCOME_SL_HIT) >= loss_threshold

    def save(self) -> None:
        STATS_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATS_FILE.write_text(json.dumps([asdict(r) for r in self._records], indent=2), encoding="utf-8")

    def _load(self) -> None:
        if not STATS_FILE.exists():
            return
        try:
            self._records = [TradeRecord(**r) for r in json.loads(STATS_FILE.read_text(encoding="utf-8"))]
        except Exception:
            self._records = []

    def _recent_records(self) -> list[TradeRecord]:
        if self._lookback_hours <= 0:
            return list(self._records)
        cutoff = datetime.now(timezone.utc) - timedelta(hours=self._lookback_hours)
        return [r for r in self._records if datetime.fromisoformat(r.closed_at) >= cutoff]

    @staticmethod
    def _from_tracked(symbol: TrackedSymbol) -> TradeRecord:
        exit_price = symbol.outcome_price if symbol.outcome_price is not None else symbol.current_price
        pnl_pct = (symbol.detection_price - exit_price) / symbol.detection_price * 100
        return TradeRecord(
            symbol=symbol.symbol,
            outcome=symbol.outcome,
            entry_price=symbol.detection_price,
            exit_price=exit_price,
            pnl_pct=pnl_pct,
            closed_at=symbol.outcome_at or datetime.now(timezone.utc).isoformat(),
        )
