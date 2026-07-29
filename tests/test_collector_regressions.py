from __future__ import annotations

import unittest
from datetime import datetime, timezone

from collector.collect_context import (
    classify_polymarket_market,
    is_public_health_polymarket,
    polymarket_search_text,
    summarize_polymarket,
)
from collector.macro_indicators import fallback_release


class CollectorRegressionTests(unittest.TestCase):
    def test_summarized_event_slug_remains_searchable(self) -> None:
        market = {
            "question": "Will this happen?",
            "slug": "will-this-happen",
            "event_slug": "hantavirus-pandemic-in-2026",
            "impact_category": "health",
            "query": "hantavirus",
        }
        text = polymarket_search_text(market)
        self.assertIn("hantavirus", text)
        self.assertTrue(is_public_health_polymarket(market))
        self.assertEqual(
            classify_polymarket_market(market, []),
            "health",
        )

    def test_health_market_is_kept_outside_top_thirty(self) -> None:
        regular = [
            {
                "question": f"Macro market {index}",
                "slug": f"macro-{index}",
                "impact_category": "macro",
            }
            for index in range(30)
        ]
        health = {
            "question": "Hantavirus pandemic in 2026?",
            "slug": "hantavirus-pandemic-in-2026",
            "event_slug": "hantavirus-pandemic-in-2026",
            "impact_category": "health",
        }
        summary = summarize_polymarket([*regular, health])
        self.assertEqual(len(summary["top_markets"]), 30)
        self.assertEqual(len(summary["health_markets"]), 1)
        self.assertEqual(
            summary["health_markets"][0]["event_slug"],
            "hantavirus-pandemic-in-2026",
        )

    def test_expired_static_release_is_not_upcoming(self) -> None:
        meta = {
            "key": "test",
            "name": "Test Release",
            "category": "test",
            "source": "test",
            "source_url": "https://example.com",
            "fallback_reference_period": "June 2026",
            "fallback_scheduled_for": "2026-06-01T08:30:00-04:00",
            "affects": [],
        }
        now = datetime(2026, 7, 29, tzinfo=timezone.utc)
        self.assertIsNone(fallback_release(meta, now))

    def test_future_static_release_can_be_used_as_fallback(self) -> None:
        meta = {
            "key": "test",
            "name": "Test Release",
            "category": "test",
            "source": "test",
            "source_url": "https://example.com",
            "fallback_reference_period": "August 2026",
            "fallback_scheduled_for": "2026-08-01T08:30:00-04:00",
            "affects": [],
        }
        now = datetime(2026, 7, 29, tzinfo=timezone.utc)
        release = fallback_release(meta, now)
        self.assertIsNotNone(release)
        self.assertEqual(
            release["calendar_status"],
            "official_static",
        )


if __name__ == "__main__":
    unittest.main()
