from __future__ import annotations

import gzip
import hashlib
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from collector.collect_context import build_polymarket_outcome_history_rows
from collector.day_swing import label_records
from collector.storage_sync import (
    PreparedObject,
    assess_time_series,
    extract_day_swing_events,
    make_event_object,
    make_manifest_event,
)
from utils.trading_data_client import TradingDataClient
from tools.sync_storage_gateway import (
    object_idempotency_key,
    resolve_since,
    save_sync_state,
)


class StorageSyncTests(unittest.TestCase):
    def setUp(self) -> None:
        self.since = datetime(2026, 7, 30, 1, 0, tzinfo=timezone.utc)
        self.now = datetime(2026, 7, 30, 1, 10, tzinfo=timezone.utc)
        self.records = [
            {
                "observed_at": "2026-07-30T00:00:00+00:00",
                "collected_at": "2026-07-30T00:07:10+00:00",
                "context_scores": {"market_context_score": 55},
                "symbols": {
                    "BTC": {
                        "price": 100.0,
                        "features": {"1h": {"rsi_14": 52}},
                        "labels": {
                            "1h": {
                                "return_pct": 2.0,
                                "price": 102.0,
                                "labeled_at": "2026-07-30T01:00:00+00:00",
                                "delay_minutes": 0,
                            }
                        },
                    }
                },
            },
            {
                "observed_at": "2026-07-30T01:00:00+00:00",
                "collected_at": "2026-07-30T01:07:20+00:00",
                "context_scores": {"market_context_score": 58},
                "symbols": {
                    "BTC": {
                        "price": 102.0,
                        "features": {"1h": {"rsi_14": 58}},
                        "labels": {},
                    }
                },
            },
        ]

    def test_features_and_labels_are_exported_separately(self) -> None:
        features, labels, quality = extract_day_swing_events(
            self.records,
            self.since,
            self.now,
        )

        self.assertEqual(len(features), 1)
        self.assertEqual(len(labels), 1)
        self.assertNotIn(
            "labels",
            features[0]["payload"]["symbols"]["BTC"],
        )
        self.assertEqual(
            labels[0]["available_at"],
            "2026-07-30T01:07:20+00:00",
        )
        self.assertEqual(
            labels[0]["event_time"],
            "2026-07-30T00:00:00+00:00",
        )
        self.assertIn("decision_path_forbidden", labels[0]["tags"])
        self.assertTrue(quality["feature_label_separated"])
        self.assertEqual(quality["labels_before_feature_count"], 0)

    def test_label_is_selected_by_availability_not_feature_time(self) -> None:
        features, labels, _ = extract_day_swing_events(
            self.records,
            self.since,
            self.now,
        )

        self.assertEqual(
            [event["event_time"] for event in features],
            ["2026-07-30T01:00:00+00:00"],
        )
        self.assertEqual(
            [event["event_time"] for event in labels],
            ["2026-07-30T00:00:00+00:00"],
        )

    def test_jsonl_object_is_deterministic_and_does_not_contain_labels(self) -> None:
        features, _, _ = extract_day_swing_events(
            self.records,
            self.since,
            self.now,
        )
        first = make_event_object(
            "day_swing_features",
            features,
            "hyperliquid-bot-test",
        )
        second = make_event_object(
            "day_swing_features",
            list(reversed(features)),
            "hyperliquid-bot-test",
        )

        self.assertEqual(first.sha256, second.sha256)
        self.assertEqual(first.object_key, second.object_key)
        self.assertEqual(first.sha256, hashlib.sha256(first.body).hexdigest())
        lines = gzip.decompress(first.body).decode("utf-8").splitlines()
        payload = json.loads(lines[0])
        self.assertNotIn(
            "labels",
            payload["payload"]["symbols"]["BTC"],
        )

        manifest = make_manifest_event(
            prepared=first,
            repo="hyperliquid-bot-test",
            run_id="github:123:1:context",
            profile="context",
            code_sha="a" * 40,
        )
        TradingDataClient._validate_dataset(first.dataset)
        TradingDataClient._validate_object_key(first.object_key)
        TradingDataClient._validate_event_envelope(manifest)
        self.assertEqual(first.content_type, "application/gzip")
        self.assertLessEqual(len(manifest["source_id"]), 128)

    def test_quality_flags_large_gaps(self) -> None:
        rows = [
            {"observed_at": "2026-07-30T00:00:00+00:00"},
            {"observed_at": "2026-07-30T02:00:00+00:00"},
        ]
        quality = assess_time_series(
            rows,
            time_field="observed_at",
            expected_minutes=15,
            now=self.now,
        )

        self.assertEqual(quality["max_gap_minutes"], 120.0)
        self.assertIn("large_gap", quality["warnings"])

    def test_native_day_swing_label_records_actual_availability(self) -> None:
        records = [
            {
                "observed_at": "2026-07-30T00:00:00+00:00",
                "collected_at": "2026-07-30T00:07:00+00:00",
                "symbols": {"BTC": {"price": 100.0, "labels": {}}},
            },
            {
                "observed_at": "2026-07-30T01:00:00+00:00",
                "collected_at": "2026-07-30T01:08:00+00:00",
                "symbols": {"BTC": {"price": 102.0, "labels": {}}},
            },
        ]

        label_records(records, ["1h"])

        label = records[0]["symbols"]["BTC"]["labels"]["1h"]
        self.assertEqual(label["labeled_at"], "2026-07-30T01:00:00+00:00")
        self.assertEqual(label["available_at"], "2026-07-30T01:08:00+00:00")
        self.assertEqual(label["label_version"], "forward_return_v1")

    def test_polymarket_rows_record_collection_availability(self) -> None:
        rows = build_polymarket_outcome_history_rows(
            observed_at="2026-07-30T01:00:00+00:00",
            markets=[
                {
                    "slug": "btc-up",
                    "question": "Will BTC go up?",
                    "outcomes": [
                        {
                            "name": "Yes",
                            "probability": 0.6,
                            "token_id": "yes-token",
                        }
                    ],
                }
            ],
            profile="context",
            collected_at="2026-07-30T01:07:00+00:00",
        )

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["observed_at"], "2026-07-30T01:00:00+00:00")
        self.assertEqual(rows[0]["collected_at"], "2026-07-30T01:07:00+00:00")

    def test_success_cursor_retries_until_ack_then_advances(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            state_path = Path(temp_dir) / "state.json"

            save_sync_state("context", self.now, state_path)
            next_since = resolve_since(None, self.now, "context", state_path)

            self.assertEqual(next_since, self.now + timedelta(microseconds=1))

    def test_object_idempotency_includes_immutable_object_key(self) -> None:
        common = {
            "dataset": "test_events",
            "body": b"same compressed body",
            "content_type": "application/gzip",
            "observed_start": "2026-07-30T00:00:00Z",
            "observed_end": "2026-07-30T00:00:00Z",
            "available_start": "2026-07-30T00:00:00Z",
            "available_end": "2026-07-30T00:00:00Z",
            "row_count": 1,
            "sha256": "a" * 64,
            "event_types": ("test.event",),
            "data_class": "test",
        }
        first = PreparedObject(
            object_key="year=2026/month=07/first.jsonl.gz",
            **common,
        )
        second = PreparedObject(
            object_key="year=2026/month=07/second.jsonl.gz",
            **common,
        )

        self.assertNotEqual(
            object_idempotency_key(first),
            object_idempotency_key(second),
        )
        self.assertEqual(
            object_idempotency_key(first),
            object_idempotency_key(first),
        )


if __name__ == "__main__":
    unittest.main()
