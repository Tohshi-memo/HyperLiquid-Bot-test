from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = ROOT / "data" / "processed"
REPORT_DIR = ROOT / "data" / "reports"

ASSET_UNIVERSE_FILE = PROCESSED_DIR / "asset_universe_latest.json"
ASSET_PRICE_HISTORY_FILE = PROCESSED_DIR / "asset_price_history.json"
RELATIONSHIP_SCAN_FILE = PROCESSED_DIR / "relationship_scan_latest.json"
LATEST_FILE = PROCESSED_DIR / "asset_features_latest.json"
ALL_FILE = PROCESSED_DIR / "asset_features_all.json"
REPORT_FILE = REPORT_DIR / "latest_asset_features.md"

HORIZONS = {
    "15m": timedelta(minutes=15),
    "1h": timedelta(hours=1),
    "4h": timedelta(hours=4),
    "24h": timedelta(hours=24),
}


def update_asset_features(now: datetime) -> dict[str, Any]:
    if os.getenv("ASSET_FEATURES_ENABLED", "true").lower() == "false":
        return {"enabled": False, "reason": "ASSET_FEATURES_ENABLED=false"}

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    asset_universe = load_json(ASSET_UNIVERSE_FILE, {})
    price_history = load_json(ASSET_PRICE_HISTORY_FILE, {})
    relationship = load_json(RELATIONSHIP_SCAN_FILE, {})
    assets = asset_universe.get("assets", []) if isinstance(asset_universe, dict) else []
    records = price_history.get("records", []) if isinstance(price_history, dict) else []
    records = [row for row in records if isinstance(row, dict)]
    records.sort(key=lambda item: item.get("observed_at", ""))
    latest_record = records[-1] if records else {}
    latest_time = parse_time(latest_record.get("observed_at"))
    prices = latest_record.get("prices", {}) if isinstance(latest_record.get("prices"), dict) else {}

    symbol_patterns = relationship.get("top_symbol_patterns", []) if isinstance(relationship, dict) else []
    pattern_by_symbol = best_pattern_by_symbol(symbol_patterns)
    rows = []
    for asset in assets if isinstance(assets, list) else []:
        if not isinstance(asset, dict):
            continue
        symbol = asset.get("symbol")
        if not symbol or symbol not in prices:
            continue
        feature = build_feature_row(asset, records, latest_time, pattern_by_symbol.get(str(symbol)))
        rows.append(feature)

    rows.sort(key=lambda row: to_float(row.get("activity_score")), reverse=True)
    top_limit = int(os.getenv("ASSET_FEATURES_TOP_LIMIT", "80"))
    latest = {
        "schema_version": 1,
        "generated_at": now.isoformat(),
        "observed_at": latest_record.get("observed_at"),
        "asset_count": len(rows),
        "top_assets": rows[:top_limit],
        "by_class": summarize_by_class(rows, top_limit),
    }
    all_payload = {
        "schema_version": 1,
        "generated_at": now.isoformat(),
        "observed_at": latest_record.get("observed_at"),
        "purpose": (
            "All tradable HyperLiquid assets with compact derived features. "
            "Use this for private strategy screening before loading heavier history."
        ),
        "asset_count": len(rows),
        "assets": rows,
    }
    LATEST_FILE.write_text(json.dumps(latest, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    ALL_FILE.write_text(json.dumps(all_payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    REPORT_FILE.write_text(render_report(latest), encoding="utf-8")

    return {
        "enabled": True,
        "updated_at": now.isoformat(),
        "latest_file": "data/processed/asset_features_latest.json",
        "all_file": "data/processed/asset_features_all.json",
        "report_file": "data/reports/latest_asset_features.md",
        "asset_count": len(rows),
        "top_assets": rows[:10],
    }


def build_feature_row(
    asset: dict[str, Any],
    records: list[dict[str, Any]],
    latest_time: datetime | None,
    pattern: dict[str, Any] | None,
) -> dict[str, Any]:
    symbol = str(asset.get("symbol"))
    returns = {
        horizon: return_for_symbol(records, symbol, latest_time, delta)
        for horizon, delta in HORIZONS.items()
    }
    volume = to_float(asset.get("day_ntl_vlm"))
    open_interest = to_float(asset.get("open_interest"))
    funding = to_float(asset.get("funding"))
    abs_return = sum(abs(to_float(value)) for value in returns.values())
    capped_abs_return = min(abs_return, 20.0)
    activity_score = (
        log_score(volume) * 0.55
        + log_score(open_interest) * 0.25
        + capped_abs_return * 0.7
        + max(0.0, to_float(pattern.get("score") if pattern else 0)) * 0.8
        + class_boost(asset.get("asset_class"))
    )
    return {
        "symbol": symbol,
        "display_name": asset.get("display_name") or asset.get("base_symbol") or symbol,
        "asset_class": asset.get("asset_class") or "unknown",
        "market_type": asset.get("market_type"),
        "dex": asset.get("dex"),
        "price": asset.get("price"),
        "returns": returns,
        "day_ntl_vlm": asset.get("day_ntl_vlm"),
        "open_interest": asset.get("open_interest"),
        "funding": asset.get("funding"),
        "activity_score": round(activity_score, 4),
        "best_relationship": compact_pattern(pattern),
    }


def return_for_symbol(
    records: list[dict[str, Any]],
    symbol: str,
    latest_time: datetime | None,
    delta: timedelta,
) -> float | None:
    if latest_time is None or not records:
        return None
    latest = records[-1]
    latest_prices = latest.get("prices", {}) if isinstance(latest.get("prices"), dict) else {}
    current = to_float(latest_prices.get(symbol))
    if current <= 0:
        return None
    previous = find_record_at_or_before(records, latest_time - delta)
    previous_prices = previous.get("prices", {}) if isinstance(previous, dict) else {}
    start = to_float(previous_prices.get(symbol))
    if start <= 0:
        return None
    return round((current / start - 1) * 100, 4)


def best_pattern_by_symbol(patterns: Any) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    if not isinstance(patterns, list):
        return result
    for pattern in patterns:
        if not isinstance(pattern, dict):
            continue
        symbol = pattern.get("symbol")
        if not symbol:
            continue
        current = result.get(str(symbol))
        if current is None or to_float(pattern.get("score")) > to_float(current.get("score")):
            result[str(symbol)] = pattern
    return result


def compact_pattern(pattern: dict[str, Any] | None) -> dict[str, Any] | None:
    if not isinstance(pattern, dict):
        return None
    return {
        "pattern_id": pattern.get("pattern_id"),
        "condition": (pattern.get("conditions") or [None])[0],
        "horizon": pattern.get("horizon"),
        "score": pattern.get("score"),
        "sample_count": pattern.get("sample_count"),
        "edge_return_pct": pattern.get("edge_return_pct"),
        "delta_probability_pct": pattern.get("delta_probability_pct"),
    }


def summarize_by_class(rows: list[dict[str, Any]], top_limit: int) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for asset_class in sorted({str(row.get("asset_class") or "unknown") for row in rows}):
        class_rows = [row for row in rows if row.get("asset_class") == asset_class]
        output[asset_class] = {
            "count": len(class_rows),
            "top_activity": sorted(class_rows, key=lambda row: to_float(row.get("activity_score")), reverse=True)[:top_limit],
            "top_4h_return": sorted(class_rows, key=lambda row: to_float(row.get("returns", {}).get("4h")), reverse=True)[:top_limit],
            "bottom_4h_return": sorted(class_rows, key=lambda row: to_float(row.get("returns", {}).get("4h")))[:top_limit],
            "top_24h_return": sorted(class_rows, key=lambda row: to_float(row.get("returns", {}).get("24h")), reverse=True)[:top_limit],
            "bottom_24h_return": sorted(class_rows, key=lambda row: to_float(row.get("returns", {}).get("24h")))[:top_limit],
            "top_volume": sorted(class_rows, key=lambda row: to_float(row.get("day_ntl_vlm")), reverse=True)[:top_limit],
        }
    return output


def render_report(latest: dict[str, Any]) -> str:
    rows = latest.get("top_assets", [])[:20]
    lines = []
    for row in rows:
        rel = row.get("best_relationship") or {}
        lines.append(
            f"- `{row.get('symbol')}` {row.get('asset_class')} price `{row.get('price')}` "
            f"4h `{row.get('returns', {}).get('4h')}` vol `{row.get('day_ntl_vlm')}` "
            f"relationship `{rel.get('pattern_id') or 'none'}`"
        )
    return (
        "# Latest Asset Features\n\n"
        "Individual asset screen for drilling down from class-level signals.\n\n"
        f"- Generated: `{latest.get('generated_at')}`\n"
        f"- Observed: `{latest.get('observed_at')}`\n"
        f"- Assets: `{latest.get('asset_count')}`\n\n"
        "## Top Activity\n\n"
        f"{chr(10).join(lines) if lines else '- No assets.'}\n"
    )


def find_record_at_or_before(records: list[dict[str, Any]], target: datetime) -> dict[str, Any] | None:
    chosen = None
    for record in records:
        observed_at = parse_time(record.get("observed_at"))
        if observed_at is None:
            continue
        if observed_at <= target:
            chosen = record
        else:
            break
    return chosen


def log_score(value: float) -> float:
    if value <= 0:
        return 0.0
    import math

    return math.log10(value + 1)


def class_boost(asset_class: Any) -> float:
    return {
        "crypto_major": 2.0,
        "equity": 2.0,
        "commodity": 1.8,
        "metal": 1.8,
        "index": 1.6,
        "fx": 1.2,
        "crypto_alt": 0.4,
        "unknown": -4.0,
    }.get(str(asset_class or "unknown"), 0.0)


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def parse_time(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return parsed.astimezone(timezone.utc) if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
    except Exception:
        return None


def to_float(value: Any) -> float:
    try:
        return float(value) if value is not None else 0.0
    except (TypeError, ValueError):
        return 0.0
