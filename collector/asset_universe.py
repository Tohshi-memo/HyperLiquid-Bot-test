from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = ROOT / "data" / "processed"
REPORT_DIR = ROOT / "data" / "reports"
LATEST_FILE = PROCESSED_DIR / "asset_universe_latest.json"
HISTORY_FILE = PROCESSED_DIR / "asset_price_history.json"
REPORT_FILE = REPORT_DIR / "latest_asset_universe.md"
HYPERLIQUID_INFO_URL = "https://api.hyperliquid.xyz/info"

logger = logging.getLogger(__name__)


def update_asset_universe_snapshot(now: datetime) -> dict[str, Any]:
    if os.getenv("ASSET_UNIVERSE_ENABLED", "true").lower() == "false":
        return {"enabled": False, "reason": "ASSET_UNIVERSE_ENABLED=false"}

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    bucket_minutes = int(os.getenv("ASSET_UNIVERSE_BUCKET_MINUTES", "15"))
    max_records = int(os.getenv("ASSET_UNIVERSE_MAX_RECORDS", "2880"))
    top_limit = int(os.getenv("ASSET_UNIVERSE_TOP_LIMIT", "25"))
    bucket = floor_time(now, bucket_minutes)

    rows = collect_asset_rows()
    latest = build_latest_snapshot(now, bucket, rows, top_limit)
    history = update_price_history(now, bucket, rows, max_records)
    summary = {
        "enabled": True,
        "updated_at": now.isoformat(),
        "observed_at": bucket.isoformat(),
        "asset_count": latest["asset_count"],
        "history_records": history["record_count"],
        "latest_file": "data/processed/asset_universe_latest.json",
        "history_file": "data/processed/asset_price_history.json",
        "report_file": "data/reports/latest_asset_universe.md",
        "top_by_volume": latest["top_by_volume"][:5],
        "top_gainers_24h": latest["top_gainers_24h"][:5],
        "top_losers_24h": latest["top_losers_24h"][:5],
    }

    LATEST_FILE.write_text(json.dumps(latest, indent=2, ensure_ascii=False), encoding="utf-8")
    HISTORY_FILE.write_text(json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8")
    REPORT_FILE.write_text(render_report(summary), encoding="utf-8")
    logger.info("Wrote %s", LATEST_FILE)
    return summary


def collect_asset_rows() -> list[dict[str, Any]]:
    meta, asset_ctxs = fetch_meta_and_contexts()
    mids = fetch_all_mids()
    universe = meta.get("universe", []) if isinstance(meta, dict) else []
    rows: dict[str, dict[str, Any]] = {}

    for idx, asset in enumerate(universe):
        if not isinstance(asset, dict):
            continue
        symbol = str(asset.get("name") or "").strip()
        if not symbol:
            continue
        ctx = asset_ctxs[idx] if idx < len(asset_ctxs) and isinstance(asset_ctxs[idx], dict) else {}
        row = build_row(symbol, asset, ctx, mids.get(symbol))
        rows[symbol] = row

    for symbol, mid in mids.items():
        if symbol not in rows:
            rows[symbol] = build_row(symbol, {}, {}, mid, source="allMids_only")

    return sorted(rows.values(), key=lambda row: row["symbol"])


def fetch_meta_and_contexts() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    response = requests.post(
        HYPERLIQUID_INFO_URL,
        json={"type": "metaAndAssetCtxs"},
        headers={"Content-Type": "application/json"},
        timeout=20,
    )
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, list) or len(data) < 2:
        return {}, []
    meta = data[0] if isinstance(data[0], dict) else {}
    contexts = data[1] if isinstance(data[1], list) else []
    return meta, contexts


def fetch_all_mids() -> dict[str, str]:
    response = requests.post(
        HYPERLIQUID_INFO_URL,
        json={"type": "allMids"},
        headers={"Content-Type": "application/json"},
        timeout=15,
    )
    response.raise_for_status()
    data = response.json()
    return data if isinstance(data, dict) else {}


def build_row(
    symbol: str,
    asset: dict[str, Any],
    ctx: dict[str, Any],
    mid_override: Any = None,
    source: str = "metaAndAssetCtxs",
) -> dict[str, Any]:
    mid_px = to_float(mid_override) or to_float(ctx.get("midPx"))
    mark_px = to_float(ctx.get("markPx"))
    oracle_px = to_float(ctx.get("oraclePx"))
    price = first_positive(mid_px, mark_px, oracle_px)
    prev_day = to_float(ctx.get("prevDayPx"))
    return {
        "symbol": symbol,
        "asset_class": "unknown",
        "classification_source": "unclassified",
        "source": source,
        "price": round(price, 8) if price else None,
        "mid_px": round(mid_px, 8) if mid_px else None,
        "mark_px": round(mark_px, 8) if mark_px else None,
        "oracle_px": round(oracle_px, 8) if oracle_px else None,
        "prev_day_px": round(prev_day, 8) if prev_day else None,
        "change_24h_pct": pct_change(price, prev_day) if price and prev_day else None,
        "day_ntl_vlm": round(to_float(ctx.get("dayNtlVlm")), 2),
        "day_base_vlm": round(to_float(ctx.get("dayBaseVlm")), 8),
        "open_interest": round(to_float(ctx.get("openInterest")), 8),
        "funding": round(to_float(ctx.get("funding")), 10) if ctx.get("funding") is not None else None,
        "premium": round(to_float(ctx.get("premium")), 10) if ctx.get("premium") is not None else None,
        "max_leverage": asset.get("maxLeverage"),
        "sz_decimals": asset.get("szDecimals"),
        "margin_table_id": asset.get("marginTableId"),
    }


def build_latest_snapshot(
    now: datetime,
    bucket: datetime,
    rows: list[dict[str, Any]],
    top_limit: int,
) -> dict[str, Any]:
    priced = [row for row in rows if row.get("price")]
    volume_rows = sorted(
        priced,
        key=lambda row: to_float(row.get("day_ntl_vlm")),
        reverse=True,
    )
    gainers = sorted(
        [row for row in priced if row.get("change_24h_pct") is not None],
        key=lambda row: to_float(row.get("change_24h_pct")),
        reverse=True,
    )
    return {
        "schema_version": 1,
        "updated_at": now.isoformat(),
        "observed_at": bucket.isoformat(),
        "asset_count": len(rows),
        "priced_asset_count": len(priced),
        "top_by_volume": compact_rows(volume_rows[:top_limit]),
        "top_gainers_24h": compact_rows(gainers[:top_limit]),
        "top_losers_24h": compact_rows(list(reversed(gainers[-top_limit:]))),
        "assets": rows,
    }


def update_price_history(
    now: datetime,
    bucket: datetime,
    rows: list[dict[str, Any]],
    max_records: int,
) -> dict[str, Any]:
    history = load_json(HISTORY_FILE, default={})
    records = history.get("records", []) if isinstance(history, dict) else []
    if not isinstance(records, list):
        records = []

    prices = {
        row["symbol"]: row["price"]
        for row in rows
        if row.get("price") is not None
    }
    record = {
        "observed_at": bucket.isoformat(),
        "collected_at": now.isoformat(),
        "asset_count": len(rows),
        "priced_asset_count": len(prices),
        "prices": prices,
    }
    records = [item for item in records if item.get("observed_at") != record["observed_at"]]
    records.append(record)
    records.sort(key=lambda item: item.get("observed_at", ""))
    if max_records > 0:
        records = records[-max_records:]

    return {
        "schema_version": 1,
        "updated_at": now.isoformat(),
        "max_records": max_records,
        "record_count": len(records),
        "records": records,
    }


def compact_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "symbol": row.get("symbol"),
            "asset_class": row.get("asset_class"),
            "price": row.get("price"),
            "change_24h_pct": row.get("change_24h_pct"),
            "day_ntl_vlm": row.get("day_ntl_vlm"),
            "open_interest": row.get("open_interest"),
            "funding": row.get("funding"),
        }
        for row in rows
    ]


def render_report(summary: dict[str, Any]) -> str:
    top_volume = render_rows(summary.get("top_by_volume", []), "day_ntl_vlm")
    gainers = render_rows(summary.get("top_gainers_24h", []), "change_24h_pct")
    losers = render_rows(summary.get("top_losers_24h", []), "change_24h_pct")
    return (
        "# Latest Asset Universe\n\n"
        f"- Updated: `{summary.get('updated_at')}`\n"
        f"- Observed: `{summary.get('observed_at')}`\n"
        f"- Assets: `{summary.get('asset_count')}`\n"
        f"- History records: `{summary.get('history_records')}`\n"
        f"- Latest file: `{summary.get('latest_file')}`\n"
        f"- History file: `{summary.get('history_file')}`\n\n"
        "## Top By Volume\n\n"
        f"{top_volume}\n\n"
        "## Top 24h Gainers\n\n"
        f"{gainers}\n\n"
        "## Top 24h Losers\n\n"
        f"{losers}\n"
    )


def render_rows(rows: list[dict[str, Any]], metric: str) -> str:
    if not rows:
        return "- No rows."
    return "\n".join(
        f"- {row.get('symbol')}: price `{row.get('price')}`, "
        f"{metric} `{row.get(metric)}`"
        for row in rows
    )


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def floor_time(dt: datetime, bucket_minutes: int) -> datetime:
    bucket = max(1, bucket_minutes)
    minute = (dt.minute // bucket) * bucket
    return dt.astimezone(timezone.utc).replace(minute=minute, second=0, microsecond=0)


def first_positive(*values: float) -> float:
    for value in values:
        if value > 0:
            return value
    return 0.0


def pct_change(new: float, old: float) -> float | None:
    if old == 0:
        return None
    return round((new / old - 1) * 100, 4)


def to_float(value: Any) -> float:
    try:
        return float(value) if value is not None else 0.0
    except (TypeError, ValueError):
        return 0.0
