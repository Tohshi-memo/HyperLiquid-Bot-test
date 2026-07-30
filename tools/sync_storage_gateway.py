from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_STATE_PATH = ROOT / "data" / "processed" / "trading_data_sync_state.json"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from collector.storage_sync import (  # noqa: E402
    OBJECT_SCHEMA_VERSION,
    PreparedObject,
    build_sync_plan,
    parse_time,
)


def main() -> int:
    args = parse_args()
    now = datetime.now(timezone.utc)
    state_path = Path(os.getenv("TD_SYNC_STATE_FILE", str(DEFAULT_STATE_PATH)))
    since = resolve_since(args.since, now, args.profile, state_path)
    repo = os.getenv("TD_REPO", "hyperliquid-bot-test")
    run_id = (
        os.getenv("TD_RUN_ID")
        or (
            f"github:{os.getenv('GITHUB_RUN_ID')}:{os.getenv('GITHUB_RUN_ATTEMPT', '1')}:{args.profile}"
            if os.getenv("GITHUB_RUN_ID")
            else None
        )
    )
    plan = build_sync_plan(
        profile=args.profile,
        since=since,
        now=now,
        repo=repo,
        run_id=run_id,
        code_sha=os.getenv("GITHUB_SHA"),
    )

    if args.dry_run:
        print_plan(plan)
        return 0

    from utils.trading_data_client import TradingDataClient

    client = TradingDataClient.from_env(timeout=args.timeout)
    client.health()
    with tempfile.TemporaryDirectory(prefix="hyper-storage-sync-") as temp_dir:
        for prepared in plan.objects:
            upload_prepared_object(client, prepared, Path(temp_dir))

    idempotency_key = (
        f"{run_id}:ledger"
        if run_id
        else f"local:{args.profile}:{now.strftime('%Y%m%dT%H%M%SZ')}:ledger"
    )
    client.ingest_events(
        plan.ledger_events,
        schema_version="1",
        idempotency_key=idempotency_key,
    )
    save_sync_state(args.profile, now, state_path)
    print_plan(plan)
    return 0


def upload_prepared_object(client: Any, prepared: PreparedObject, temp_dir: Path) -> None:
    suffix = ".jsonl.gz" if prepared.object_key.endswith(".jsonl.gz") else ".json.gz"
    local_path = temp_dir / f"{prepared.sha256}{suffix}"
    local_path.write_bytes(prepared.body)
    client.upload_object(
        local_path=local_path,
        dataset=prepared.dataset,
        object_key=prepared.object_key,
        schema_version=OBJECT_SCHEMA_VERSION,
        content_type=prepared.content_type,
        observed_start=prepared.observed_start,
        observed_end=prepared.observed_end,
        idempotency_key=object_idempotency_key(prepared),
    )


def object_idempotency_key(prepared: PreparedObject) -> str:
    identity = "\n".join(
        [
            "TD-OBJECT-IDEMPOTENCY-v1",
            prepared.dataset,
            prepared.object_key,
            prepared.sha256,
        ]
    )
    return f"object:{hashlib.sha256(identity.encode('utf-8')).hexdigest()}"


def resolve_since(
    value: str | None,
    now: datetime,
    profile: str,
    state_path: Path = DEFAULT_STATE_PATH,
) -> datetime:
    if value:
        parsed = parse_time(value)
        if parsed is None:
            raise SystemExit(f"Invalid --since timestamp: {value}")
        return parsed
    state = load_sync_state(state_path)
    profile_state = state.get("profiles", {}).get(profile, {})
    if isinstance(profile_state, dict):
        cursor = parse_time(profile_state.get("available_through"))
        if cursor is not None:
            return cursor + timedelta(microseconds=1)
    minutes = int(os.getenv("TD_SYNC_LOOKBACK_MINUTES", "90"))
    return now - timedelta(minutes=max(1, minutes))


def load_sync_state(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return {"schema_version": 1, "profiles": {}}
    if (
        not isinstance(value, dict)
        or value.get("schema_version") != 1
        or not isinstance(value.get("profiles"), dict)
    ):
        return {"schema_version": 1, "profiles": {}}
    return value


def save_sync_state(profile: str, available_through: datetime, path: Path) -> None:
    state = load_sync_state(path)
    profiles = state.setdefault("profiles", {})
    profiles[profile] = {
        "available_through": available_through.astimezone(timezone.utc).isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def print_plan(plan: Any) -> None:
    summary = {
        "objects": [
            {
                "dataset": item.dataset,
                "object_key": item.object_key,
                "rows": item.row_count,
                "sha256": item.sha256,
                "observed_start": item.observed_start,
                "observed_end": item.observed_end,
                "available_end": item.available_end,
            }
            for item in plan.objects
        ],
        "ledger_events": len(plan.ledger_events),
        "warnings": plan.quality.get("warnings", []),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Upload only newly available HyperLiquid research rows to the storage "
            "gateway. Cumulative JSON source files are never uploaded as-is."
        )
    )
    parser.add_argument(
        "--profile",
        required=True,
        choices=("context", "flow_alert", "macro"),
    )
    parser.add_argument(
        "--since",
        help="UTC ISO-8601 lower bound. Defaults to TD_SYNC_LOOKBACK_MINUTES.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Build and print the upload plan without contacting the gateway.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    raise SystemExit(main())
