from __future__ import annotations

import json
import math
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = ROOT / "data" / "processed"
REPORT_DIR = ROOT / "data" / "reports"

ASSET_UNIVERSE_FILE = PROCESSED_DIR / "asset_universe_latest.json"
ASSET_PRICE_HISTORY_FILE = PROCESSED_DIR / "asset_price_history.json"
MARKET_CONTEXT_HISTORY_FILE = PROCESSED_DIR / "market_context_history.json"
FLOW_ALERT_HISTORY_FILE = PROCESSED_DIR / "flow_alert_history.json"
LATEST_FILE = PROCESSED_DIR / "relationship_scan_latest.json"
REPORT_FILE = REPORT_DIR / "latest_relationship_scan.md"

DEFAULT_HORIZONS = {
    "1h": timedelta(hours=1),
    "4h": timedelta(hours=4),
    "24h": timedelta(hours=24),
}


def update_relationship_scan(now: datetime) -> dict[str, Any]:
    if os.getenv("RELATIONSHIP_SCAN_ENABLED", "true").lower() == "false":
        return {"enabled": False, "reason": "RELATIONSHIP_SCAN_ENABLED=false"}

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    asset_universe = load_json(ASSET_UNIVERSE_FILE, {})
    price_history = load_json(ASSET_PRICE_HISTORY_FILE, {})
    market_history = load_json(MARKET_CONTEXT_HISTORY_FILE, [])
    flow_history = load_json(FLOW_ALERT_HISTORY_FILE, [])
    min_samples = int(os.getenv("RELATIONSHIP_MIN_SAMPLES", "30"))
    top_limit = int(os.getenv("RELATIONSHIP_TOP_LIMIT", "40"))

    records = price_history.get("records", []) if isinstance(price_history, dict) else []
    records = [row for row in records if isinstance(row, dict)]
    records.sort(key=lambda item: item.get("observed_at", ""))

    class_map = build_class_map(asset_universe)
    market_points = parse_points(market_history)
    flow_points = parse_points(flow_history)
    event_points = build_event_points(records, market_points, flow_points)
    baselines = build_baselines(records, class_map)
    patterns = scan_patterns(records, class_map, event_points, baselines, min_samples)
    symbol_patterns = scan_symbol_patterns(records, class_map, asset_universe, event_points, min_samples)

    latest = {
        "schema_version": 1,
        "generated_at": now.isoformat(),
        "purpose": (
            "Mechanical relationship scan. It finds conditional patterns only; "
            "AI and private trading logic decide whether a hypothesis is useful."
        ),
        "leakage_guard": "Each condition uses only market/context/flow data available at or before the price timestamp.",
        "min_samples": min_samples,
        "price_records": len(records),
        "market_context_records": len(market_points),
        "flow_alert_records": len(flow_points),
        "asset_classes": sorted(set(class_map.values())),
        "conditions": condition_catalog(),
        "baselines": baselines,
        "top_patterns": patterns[:top_limit],
        "top_symbol_patterns": symbol_patterns[:top_limit],
        "pattern_count": len(patterns),
        "symbol_pattern_count": len(symbol_patterns),
    }

    LATEST_FILE.write_text(json.dumps(latest, indent=2, ensure_ascii=False), encoding="utf-8")
    REPORT_FILE.write_text(render_report(latest), encoding="utf-8")

    return {
        "enabled": True,
        "updated_at": now.isoformat(),
        "latest_file": "data/processed/relationship_scan_latest.json",
        "report_file": "data/reports/latest_relationship_scan.md",
        "pattern_count": len(patterns),
        "symbol_pattern_count": len(symbol_patterns),
        "top_patterns": patterns[:10],
        "top_symbol_patterns": symbol_patterns[:10],
        "min_samples": min_samples,
    }


def build_class_map(asset_universe: dict[str, Any]) -> dict[str, str]:
    rows = asset_universe.get("assets", []) if isinstance(asset_universe, dict) else []
    mapping: dict[str, str] = {}
    for row in rows if isinstance(rows, list) else []:
        if not isinstance(row, dict):
            continue
        symbol = row.get("symbol")
        asset_class = row.get("asset_class")
        if symbol and asset_class:
            mapping[str(symbol)] = str(asset_class)
    return mapping


def build_event_points(
    price_records: list[dict[str, Any]],
    market_points: list[dict[str, Any]],
    flow_points: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    output = []
    for record in price_records:
        observed_at = parse_time(record.get("observed_at"))
        if observed_at is None:
            continue
        market = latest_before(market_points, observed_at) or {}
        flow = latest_before(flow_points, observed_at) or {}
        output.append(
            {
                "observed_at": observed_at,
                "events": evaluate_conditions(market, flow),
                "market": market,
                "flow": flow,
            }
        )
    return output


def condition_catalog() -> dict[str, str]:
    return {
        "news_risk_high": "News Risk is elevated.",
        "macro_risk_high": "Macro Risk is elevated.",
        "risk_on_high": "Risk-On score is elevated.",
        "market_context_high": "Market Context is supportive.",
        "polymarket_volume_spike": "Polymarket 24h volume z-score is elevated.",
        "flow_alert_high": "Flow Alert score is elevated.",
        "news_and_polymarket": "News Risk and Polymarket volume spike happen together.",
        "risk_on_and_context": "Risk-On and Market Context are both supportive.",
        "macro_and_flow": "Macro Risk and Flow Alert are elevated together.",
    }


def evaluate_conditions(market: dict[str, Any], flow: dict[str, Any]) -> dict[str, bool]:
    scores = market.get("scores", {}) if isinstance(market.get("scores"), dict) else {}
    flow_scores = flow.get("scores", {}) if isinstance(flow.get("scores"), dict) else {}
    poly = flow.get("polymarket", {}) if isinstance(flow.get("polymarket"), dict) else {}

    news_risk_high = to_float(scores.get("news_risk_score")) >= 55
    macro_risk_high = to_float(scores.get("macro_risk_score")) >= 50
    risk_on_high = to_float(scores.get("risk_on_score")) >= 55
    market_context_high = to_float(scores.get("market_context_score")) >= 55
    polymarket_volume_spike = to_float(poly.get("volume_24h_zscore_7d")) >= 1
    flow_alert_high = to_float(flow_scores.get("flow_alert_score")) >= 35

    return {
        "news_risk_high": news_risk_high,
        "macro_risk_high": macro_risk_high,
        "risk_on_high": risk_on_high,
        "market_context_high": market_context_high,
        "polymarket_volume_spike": polymarket_volume_spike,
        "flow_alert_high": flow_alert_high,
        "news_and_polymarket": news_risk_high and polymarket_volume_spike,
        "risk_on_and_context": risk_on_high and market_context_high,
        "macro_and_flow": macro_risk_high and flow_alert_high,
    }


def build_baselines(
    records: list[dict[str, Any]],
    class_map: dict[str, str],
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for horizon_name, horizon_delta in DEFAULT_HORIZONS.items():
        class_returns = build_forward_class_returns(records, class_map, horizon_delta)
        output[horizon_name] = {
            asset_class: summarize_returns(values)
            for asset_class, values in sorted(class_returns.items())
        }
    return output


def scan_patterns(
    records: list[dict[str, Any]],
    class_map: dict[str, str],
    event_points: list[dict[str, Any]],
    baselines: dict[str, Any],
    min_samples: int,
) -> list[dict[str, Any]]:
    event_by_time = {item["observed_at"]: item["events"] for item in event_points}
    candidates = []
    conditions = list(condition_catalog())

    for horizon_name, horizon_delta in DEFAULT_HORIZONS.items():
        class_returns = build_forward_class_returns_by_time(records, class_map, horizon_delta)
        for asset_class, time_returns in class_returns.items():
            baseline = baselines.get(horizon_name, {}).get(asset_class, {})
            baseline_up = to_float_or_none(baseline.get("up_rate_pct"))
            baseline_avg = to_float_or_none(baseline.get("avg_return_pct"))
            if baseline_up is None or baseline_avg is None:
                continue
            for condition in conditions:
                values = [
                    ret
                    for point_time, ret in time_returns
                    if event_by_time.get(point_time, {}).get(condition)
                ]
                if not values:
                    continue
                summary = summarize_returns(values)
                summary["pattern_id"] = f"{condition}->{asset_class}_{horizon_name}"
                summary["conditions"] = [condition]
                summary["target"] = asset_class
                summary["horizon"] = horizon_name
                summary["baseline_sample_count"] = baseline.get("sample_count")
                summary["baseline_up_rate_pct"] = baseline_up
                summary["baseline_avg_return_pct"] = baseline_avg
                summary["delta_probability_pct"] = round(summary["up_rate_pct"] - baseline_up, 4)
                summary["edge_return_pct"] = round(summary["avg_return_pct"] - baseline_avg, 4)
                summary["max_drawdown_pct"] = max_drawdown(values)
                summary["longest_loss_streak"] = longest_loss_streak(values)
                summary["stability"] = split_stability(values)
                summary["sample_status"] = "ready" if summary["sample_count"] >= min_samples else "thin_sample"
                summary["score"] = pattern_score(summary, min_samples)
                candidates.append(summary)

    candidates.sort(
        key=lambda item: (
            item.get("sample_status") == "ready",
            item.get("score", -999),
            item.get("sample_count", 0),
        ),
        reverse=True,
    )
    return candidates


def scan_symbol_patterns(
    records: list[dict[str, Any]],
    class_map: dict[str, str],
    asset_universe: dict[str, Any],
    event_points: list[dict[str, Any]],
    min_samples: int,
) -> list[dict[str, Any]]:
    event_by_time = {item["observed_at"]: item["events"] for item in event_points}
    conditions = list(condition_catalog())
    candidates = []
    eligible = eligible_symbols(asset_universe)

    for horizon_name, horizon_delta in DEFAULT_HORIZONS.items():
        symbol_returns = build_forward_symbol_returns_by_time(records, eligible, horizon_delta)
        for symbol, time_returns in symbol_returns.items():
            baseline_values = [ret for _, ret in time_returns]
            baseline = summarize_returns(baseline_values)
            if baseline["sample_count"] < min_samples:
                continue
            baseline_up = to_float(baseline.get("up_rate_pct"))
            baseline_avg = to_float(baseline.get("avg_return_pct"))
            for condition in conditions:
                values = [
                    ret
                    for point_time, ret in time_returns
                    if event_by_time.get(point_time, {}).get(condition)
                ]
                if not values:
                    continue
                summary = summarize_returns(values)
                summary["pattern_id"] = f"{condition}->{symbol}_{horizon_name}"
                summary["conditions"] = [condition]
                summary["symbol"] = symbol
                summary["target"] = symbol
                summary["asset_class"] = class_map.get(symbol, "unknown")
                summary["horizon"] = horizon_name
                summary["baseline_sample_count"] = baseline.get("sample_count")
                summary["baseline_up_rate_pct"] = baseline_up
                summary["baseline_avg_return_pct"] = baseline_avg
                summary["delta_probability_pct"] = round(summary["up_rate_pct"] - baseline_up, 4)
                summary["edge_return_pct"] = round(summary["avg_return_pct"] - baseline_avg, 4)
                summary["max_drawdown_pct"] = max_drawdown(values)
                summary["longest_loss_streak"] = longest_loss_streak(values)
                summary["stability"] = split_stability(values)
                summary["sample_status"] = "ready" if summary["sample_count"] >= min_samples else "thin_sample"
                summary["score"] = pattern_score(summary, min_samples)
                candidates.append(summary)

    candidates.sort(
        key=lambda item: (
            item.get("sample_status") == "ready",
            item.get("score", -999),
            item.get("sample_count", 0),
        ),
        reverse=True,
    )
    return candidates


def eligible_symbols(asset_universe: dict[str, Any]) -> set[str]:
    rows = asset_universe.get("assets", []) if isinstance(asset_universe, dict) else []
    if not isinstance(rows, list):
        return set()
    allowed_classes = {
        item.strip()
        for item in os.getenv(
            "RELATIONSHIP_ALLOWED_CLASSES",
            "equity,commodity,metal,index,fx,crypto_major,crypto_alt,unknown",
        ).split(",")
        if item.strip()
    }
    liquid = [
        row
        for row in rows
        if isinstance(row, dict)
        and row.get("symbol")
        and row.get("asset_class") in allowed_classes
        and to_float(row.get("price")) > 0
    ]
    liquid.sort(key=lambda row: to_float(row.get("day_ntl_vlm")), reverse=True)
    max_symbols = int(os.getenv("RELATIONSHIP_SYMBOL_LIMIT", "1000"))
    return {str(row["symbol"]) for row in liquid[:max_symbols]}


def build_forward_class_returns(
    records: list[dict[str, Any]],
    class_map: dict[str, str],
    horizon: timedelta,
) -> dict[str, list[float]]:
    by_time = build_forward_class_returns_by_time(records, class_map, horizon)
    output: dict[str, list[float]] = {}
    for asset_class, rows in by_time.items():
        output[asset_class] = [ret for _, ret in rows]
    return output


def build_forward_class_returns_by_time(
    records: list[dict[str, Any]],
    class_map: dict[str, str],
    horizon: timedelta,
) -> dict[str, list[tuple[datetime, float]]]:
    output: dict[str, list[tuple[datetime, float]]] = {}
    for record in records:
        point_time = parse_time(record.get("observed_at"))
        if point_time is None:
            continue
        future = find_record_at_or_after(records, point_time + horizon)
        if not future:
            continue
        current_prices = record.get("prices", {}) if isinstance(record.get("prices"), dict) else {}
        future_prices = future.get("prices", {}) if isinstance(future.get("prices"), dict) else {}
        grouped: dict[str, list[float]] = {}
        for symbol, current_price in current_prices.items():
            start = to_float(current_price)
            end = to_float(future_prices.get(symbol))
            if start <= 0 or end <= 0:
                continue
            asset_class = class_map.get(str(symbol), "unknown")
            grouped.setdefault(asset_class, []).append((end / start - 1) * 100)
        for asset_class, values in grouped.items():
            if values:
                output.setdefault(asset_class, []).append((point_time, sum(values) / len(values)))
    return output


def build_forward_symbol_returns_by_time(
    records: list[dict[str, Any]],
    symbols: set[str],
    horizon: timedelta,
) -> dict[str, list[tuple[datetime, float]]]:
    output: dict[str, list[tuple[datetime, float]]] = {}
    if not symbols:
        return output
    for record in records:
        point_time = parse_time(record.get("observed_at"))
        if point_time is None:
            continue
        future = find_record_at_or_after(records, point_time + horizon)
        if not future:
            continue
        current_prices = record.get("prices", {}) if isinstance(record.get("prices"), dict) else {}
        future_prices = future.get("prices", {}) if isinstance(future.get("prices"), dict) else {}
        for symbol in symbols:
            start = to_float(current_prices.get(symbol))
            end = to_float(future_prices.get(symbol))
            if start <= 0 or end <= 0:
                continue
            output.setdefault(symbol, []).append((point_time, (end / start - 1) * 100))
    return output


def summarize_returns(values: list[float]) -> dict[str, Any]:
    clean = [value for value in values if value is not None and not math.isnan(value)]
    if not clean:
        return {
            "sample_count": 0,
            "up_rate_pct": 0.0,
            "avg_return_pct": 0.0,
            "median_return_pct": 0.0,
        }
    ordered = sorted(clean)
    mid = len(ordered) // 2
    median = ordered[mid] if len(ordered) % 2 else (ordered[mid - 1] + ordered[mid]) / 2
    return {
        "sample_count": len(clean),
        "up_rate_pct": round(sum(1 for value in clean if value > 0) / len(clean) * 100, 4),
        "avg_return_pct": round(sum(clean) / len(clean), 4),
        "median_return_pct": round(median, 4),
    }


def pattern_score(row: dict[str, Any], min_samples: int) -> float:
    sample_count = int(row.get("sample_count") or 0)
    sample_factor = min(1.0, sample_count / max(1, min_samples))
    stability = row.get("stability", {})
    stability_penalty = 0.65 if stability.get("direction_consistent") is False else 1.0
    return round(
        (
            to_float(row.get("edge_return_pct")) * 12
            + to_float(row.get("delta_probability_pct")) * 0.08
            - abs(to_float(row.get("max_drawdown_pct"))) * 0.15
            - to_float(row.get("longest_loss_streak")) * 0.05
        )
        * sample_factor
        * stability_penalty,
        4,
    )


def max_drawdown(values: list[float]) -> float:
    equity = 0.0
    peak = 0.0
    worst = 0.0
    for value in values:
        equity += value
        peak = max(peak, equity)
        worst = min(worst, equity - peak)
    return round(worst, 4)


def longest_loss_streak(values: list[float]) -> int:
    longest = 0
    current = 0
    for value in values:
        if value <= 0:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest


def split_stability(values: list[float]) -> dict[str, Any]:
    if len(values) < 4:
        return {"direction_consistent": None}
    mid = len(values) // 2
    first = summarize_returns(values[:mid])
    second = summarize_returns(values[mid:])
    first_avg = to_float(first.get("avg_return_pct"))
    second_avg = to_float(second.get("avg_return_pct"))
    return {
        "first_avg_return_pct": first_avg,
        "second_avg_return_pct": second_avg,
        "direction_consistent": (first_avg >= 0 and second_avg >= 0) or (first_avg <= 0 and second_avg <= 0),
    }


def render_report(latest: dict[str, Any]) -> str:
    rows = latest.get("top_patterns", [])
    pattern_lines = []
    for row in rows[:20]:
        pattern_lines.append(
            f"- `{row.get('pattern_id')}` score `{row.get('score')}` "
            f"n `{row.get('sample_count')}` status `{row.get('sample_status')}` "
            f"deltaP `{row.get('delta_probability_pct')}` edge `{row.get('edge_return_pct')}` "
            f"maxDD `{row.get('max_drawdown_pct')}`"
        )
    conditions = "\n".join(
        f"- `{name}`: {description}"
        for name, description in latest.get("conditions", {}).items()
    )
    return (
        "# Latest Relationship Scan\n\n"
        "Mechanical scan for conditional relationships. This is not a trading signal; "
        "it is a candidate generator for private AI review and out-of-sample strategy work.\n\n"
        f"- Generated: `{latest.get('generated_at')}`\n"
        f"- Price records: `{latest.get('price_records')}`\n"
        f"- Market context records: `{latest.get('market_context_records')}`\n"
        f"- Flow alert records: `{latest.get('flow_alert_records')}`\n"
        f"- Minimum samples: `{latest.get('min_samples')}`\n"
        f"- Pattern count: `{latest.get('pattern_count')}`\n\n"
        f"- Symbol pattern count: `{latest.get('symbol_pattern_count')}`\n\n"
        "## Conditions\n\n"
        f"{conditions or '- No conditions.'}\n\n"
        "## Top Patterns\n\n"
        f"{chr(10).join(pattern_lines) if pattern_lines else '- No patterns yet.'}\n\n"
        "## Guardrails\n\n"
        "- No future leakage: conditions use only data available at or before the price timestamp.\n"
        "- Treat thin samples as watchlist items only.\n"
        "- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.\n"
    )


def parse_points(rows: Any) -> list[dict[str, Any]]:
    if not isinstance(rows, list):
        return []
    points = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        parsed = parse_time(row.get("generated_at") or row.get("observed_at"))
        if parsed is None:
            continue
        enriched = dict(row)
        enriched["_time"] = parsed
        points.append(enriched)
    points.sort(key=lambda item: item["_time"])
    return points


def latest_before(points: list[dict[str, Any]], point_time: datetime) -> dict[str, Any] | None:
    current = None
    for item in points:
        if item["_time"] <= point_time:
            current = item
        else:
            break
    return current


def find_record_at_or_after(records: list[dict[str, Any]], target: datetime) -> dict[str, Any] | None:
    for record in records:
        observed_at = parse_time(record.get("observed_at"))
        if observed_at is not None and observed_at >= target:
            return record
    return None


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


def to_float_or_none(value: Any) -> float | None:
    try:
        return float(value) if value is not None else None
    except (TypeError, ValueError):
        return None
