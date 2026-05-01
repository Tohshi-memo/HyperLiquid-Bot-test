from __future__ import annotations

import json
import logging
import math
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = ROOT / "data" / "processed"
REPORT_DIR = ROOT / "data" / "reports"
DATASET_FILE = PROCESSED_DIR / "day_swing_dataset.json"
REPORT_FILE = REPORT_DIR / "latest_day_swing.md"
FLOW_ALERT_FILE = PROCESSED_DIR / "flow_alert.json"
AI_ANALYSIS_PACK_FILE = PROCESSED_DIR / "ai_analysis_pack.json"
AI_ANALYSIS_BRIEF_FILE = REPORT_DIR / "latest_ai_analysis_brief.md"

DEFAULT_SYMBOLS = "BTC,ETH,HYPE,SOL"
DEFAULT_INTERVALS = "15m,1h,4h"
DEFAULT_HORIZONS = "1h,4h,24h,72h"
HYPERLIQUID_INFO_URL = "https://api.hyperliquid.xyz/info"

logger = logging.getLogger(__name__)


def update_day_swing_dataset(now: datetime, context: dict[str, Any]) -> dict[str, Any]:
    if os.getenv("DAY_SWING_ENABLED", "true").lower() == "false":
        return {"enabled": False, "reason": "DAY_SWING_ENABLED=false"}

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    symbols = parse_symbols(os.getenv("DAY_SWING_SYMBOLS", DEFAULT_SYMBOLS))
    intervals = parse_csv(os.getenv("DAY_SWING_INTERVALS", DEFAULT_INTERVALS))
    horizons = parse_csv(os.getenv("DAY_SWING_LABEL_HORIZONS", DEFAULT_HORIZONS))
    bucket_minutes = int(os.getenv("DAY_SWING_BUCKET_MINUTES", "15"))
    max_records = int(os.getenv("DAY_SWING_MAX_RECORDS", "12000"))

    dataset = load_dataset()
    records = dataset.get("records", [])
    if not isinstance(records, list):
        records = []

    mids = fetch_all_mids()
    record = build_observation(now, bucket_minutes, symbols, intervals, mids, context)
    records = [r for r in records if r.get("observed_at") != record["observed_at"]]
    records.append(record)
    records.sort(key=lambda item: item.get("observed_at", ""))
    label_records(records, horizons)
    records = records[-max_records:]

    output = {
        "schema_version": 1,
        "updated_at": now.isoformat(),
        "symbols": symbols,
        "intervals": intervals,
        "label_horizons": horizons,
        "records": records,
    }
    DATASET_FILE.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")

    summary = summarize_dataset(output)
    analysis_pack = build_ai_analysis_pack(output, summary)
    AI_ANALYSIS_PACK_FILE.write_text(json.dumps(analysis_pack, indent=2, ensure_ascii=False), encoding="utf-8")
    AI_ANALYSIS_BRIEF_FILE.write_text(render_ai_analysis_brief(analysis_pack), encoding="utf-8")
    summary["ai_analysis_pack"] = "data/processed/ai_analysis_pack.json"
    summary["ai_analysis_brief"] = "data/reports/latest_ai_analysis_brief.md"
    REPORT_FILE.write_text(render_report(summary, record), encoding="utf-8")
    logger.info("Wrote %s", DATASET_FILE)
    return summary


def build_observation(
    now: datetime,
    bucket_minutes: int,
    symbols: list[str],
    intervals: list[str],
    mids: dict[str, str],
    context: dict[str, Any],
) -> dict[str, Any]:
    bucket = floor_time(now, bucket_minutes)
    flow_alert = load_json(FLOW_ALERT_FILE, default={})
    symbol_rows: dict[str, Any] = {}

    for symbol in symbols:
        interval_features: dict[str, Any] = {}
        fallback_price = 0.0
        for interval in intervals:
            candles = fetch_candles(symbol, interval, candle_lookback())
            features = compute_features(candles)
            interval_features[interval] = features
            if interval == "15m" and features.get("close"):
                fallback_price = to_float(features.get("close"))

        price = to_float(mids.get(symbol)) or fallback_price
        if price <= 0:
            logger.warning("No usable price for %s", symbol)
            continue

        symbol_rows[symbol] = {
            "price": round(price, 8),
            "features": interval_features,
            "labels": {},
        }

    return {
        "observed_at": bucket.isoformat(),
        "collected_at": now.isoformat(),
        "context_scores": context.get("scores", {}),
        "news": {
            "article_count": context.get("news", {}).get("article_count"),
            "risk_keyword_hits": context.get("news", {}).get("risk_keyword_hits"),
            "sentiment_score": context.get("news", {}).get("sentiment_score"),
        },
        "polymarket": {
            "market_count": context.get("polymarket", {}).get("market_count"),
        },
        "flow_alert": {
            "generated_at": flow_alert.get("generated_at"),
            "flow_alert_score": flow_alert.get("scores", {}).get("flow_alert_score")
            if isinstance(flow_alert.get("scores"), dict)
            else None,
            "flow_alert_level": flow_alert.get("scores", {}).get("flow_alert_level")
            if isinstance(flow_alert.get("scores"), dict)
            else None,
        },
        "symbols": symbol_rows,
    }


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


def fetch_candles(symbol: str, interval: str, lookback: int) -> list[dict[str, Any]]:
    duration_ms = duration_to_minutes(interval) * 60 * 1000
    end = datetime.now(timezone.utc)
    start_ms = int((end - timedelta(milliseconds=duration_ms * lookback)).timestamp() * 1000)
    end_ms = int(end.timestamp() * 1000)
    response = requests.post(
        HYPERLIQUID_INFO_URL,
        json={
            "type": "candleSnapshot",
            "req": {
                "coin": symbol,
                "interval": interval,
                "startTime": start_ms,
                "endTime": end_ms,
            },
        },
        headers={"Content-Type": "application/json"},
        timeout=20,
    )
    response.raise_for_status()
    data = response.json()
    return sorted(data, key=lambda item: item.get("t", 0)) if isinstance(data, list) else []


def compute_features(candles: list[dict[str, Any]]) -> dict[str, Any]:
    if not candles:
        return {"candle_count": 0}

    closes = [to_float(c.get("c")) for c in candles]
    opens = [to_float(c.get("o")) for c in candles]
    highs = [to_float(c.get("h")) for c in candles]
    lows = [to_float(c.get("l")) for c in candles]
    volumes = [to_float(c.get("v")) for c in candles]
    closes = [value for value in closes if value > 0]
    if not closes:
        return {"candle_count": len(candles)}

    latest_close = closes[-1]
    latest_open = opens[-1] if opens and opens[-1] > 0 else latest_close
    latest_high = highs[-1] if highs and highs[-1] > 0 else latest_close
    latest_low = lows[-1] if lows and lows[-1] > 0 else latest_close
    last_volume = volumes[-1] if volumes else 0.0
    avg_volume_20 = average([v for v in volumes[-21:-1] if v > 0])
    sma_20 = average(closes[-20:])
    sma_50 = average(closes[-50:])

    return {
        "candle_count": len(candles),
        "close": round(latest_close, 8),
        "return_1_pct": pct_change(latest_close, closes[-2]) if len(closes) >= 2 else None,
        "return_3_pct": pct_change(latest_close, closes[-4]) if len(closes) >= 4 else None,
        "return_12_pct": pct_change(latest_close, closes[-13]) if len(closes) >= 13 else None,
        "body_pct": pct_change(latest_close, latest_open),
        "range_pct": pct_change(latest_high, latest_low),
        "close_vs_sma20_pct": pct_change(latest_close, sma_20) if sma_20 else None,
        "close_vs_sma50_pct": pct_change(latest_close, sma_50) if sma_50 else None,
        "rsi_14": rsi(closes, 14),
        "volatility_20_pct": volatility_pct(closes[-21:]),
        "volume_ratio_20": round(last_volume / avg_volume_20, 4) if avg_volume_20 else None,
    }


def label_records(records: list[dict[str, Any]], horizons: list[str]) -> None:
    max_delay_minutes = int(os.getenv("DAY_SWING_LABEL_MAX_DELAY_MINUTES", "45"))
    parsed = [(parse_time(r.get("observed_at")), r) for r in records]
    parsed = [(t, r) for t, r in parsed if t is not None]
    parsed.sort(key=lambda item: item[0])

    for observed_at, record in parsed:
        symbols = record.get("symbols", {})
        if not isinstance(symbols, dict):
            continue
        for horizon in horizons:
            target = observed_at + timedelta(minutes=duration_to_minutes(horizon))
            future_time, future_record = find_future_record(parsed, target)
            if future_time is None or future_record is None:
                continue
            delay = (future_time - target).total_seconds() / 60
            if delay > max_delay_minutes:
                continue
            for symbol, row in symbols.items():
                if not isinstance(row, dict):
                    continue
                future_symbol = future_record.get("symbols", {}).get(symbol, {})
                future_price = to_float(future_symbol.get("price")) if isinstance(future_symbol, dict) else 0.0
                start_price = to_float(row.get("price"))
                if start_price <= 0 or future_price <= 0:
                    continue
                labels = row.setdefault("labels", {})
                if not isinstance(labels, dict):
                    labels = {}
                    row["labels"] = labels
                labels[horizon] = {
                    "return_pct": pct_change(future_price, start_price),
                    "price": round(future_price, 8),
                    "labeled_at": future_time.isoformat(),
                    "delay_minutes": round(delay, 1),
                }


def find_future_record(
    parsed_records: list[tuple[datetime, dict[str, Any]]],
    target: datetime,
) -> tuple[datetime | None, dict[str, Any] | None]:
    for observed_at, record in parsed_records:
        if observed_at >= target:
            return observed_at, record
    return None, None


def summarize_dataset(dataset: dict[str, Any]) -> dict[str, Any]:
    records = dataset.get("records", [])
    if not isinstance(records, list):
        records = []

    label_counts: dict[str, int] = {h: 0 for h in dataset.get("label_horizons", [])}
    latest = records[-1] if records else {}
    for record in records:
        symbols = record.get("symbols", {})
        if not isinstance(symbols, dict):
            continue
        for row in symbols.values():
            labels = row.get("labels", {}) if isinstance(row, dict) else {}
            if not isinstance(labels, dict):
                continue
            for horizon in label_counts:
                if isinstance(labels.get(horizon), dict):
                    label_counts[horizon] += 1

    return {
        "enabled": True,
        "updated_at": dataset.get("updated_at"),
        "record_count": len(records),
        "symbols": dataset.get("symbols", []),
        "intervals": dataset.get("intervals", []),
        "label_horizons": dataset.get("label_horizons", []),
        "label_counts": label_counts,
        "latest_observed_at": latest.get("observed_at") if isinstance(latest, dict) else None,
        "latest_prices": {
            symbol: row.get("price")
            for symbol, row in latest.get("symbols", {}).items()
            if isinstance(row, dict)
        }
        if isinstance(latest.get("symbols"), dict)
        else {},
    }


def build_ai_analysis_pack(dataset: dict[str, Any], summary: dict[str, Any]) -> dict[str, Any]:
    records = dataset.get("records", [])
    if not isinstance(records, list):
        records = []
    latest = records[-1] if records else {}
    horizons = dataset.get("label_horizons", [])
    if not isinstance(horizons, list):
        horizons = []

    return {
        "schema_version": 1,
        "updated_at": dataset.get("updated_at"),
        "purpose": (
            "AI should read this compact pack before loading the full day_swing_dataset.json "
            "to reduce token and quota usage."
        ),
        "recommended_reading_order": [
            "data/reports/latest_ai_analysis_brief.md",
            "data/processed/ai_analysis_pack.json",
            "data/reports/latest_day_swing.md",
            "data/processed/day_swing_dataset.json only when deeper row-level analysis is needed",
        ],
        "source_files": {
            "full_dataset": "data/processed/day_swing_dataset.json",
            "context_history": "data/processed/market_context_history.json",
            "flow_alert_history": "data/processed/flow_alert_history.json",
            "latest_day_swing_report": "data/reports/latest_day_swing.md",
        },
        "dataset_summary": summary,
        "latest_compact": compact_latest_record(latest),
        "horizon_stats": build_horizon_stats(records, horizons),
        "condition_stats": build_condition_stats(records, horizons),
        "usage_note": (
            "Use this pack for readiness checks and first-pass strategy screening. "
            "Request the full dataset only for validating a specific candidate rule."
        ),
    }


def compact_latest_record(record: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(record, dict):
        return {}
    symbols = {}
    for symbol, row in record.get("symbols", {}).items():
        if not isinstance(row, dict):
            continue
        features = row.get("features", {})
        compact_features = {}
        if isinstance(features, dict):
            for interval, values in features.items():
                if not isinstance(values, dict):
                    continue
                compact_features[interval] = {
                    "return_3_pct": values.get("return_3_pct"),
                    "return_12_pct": values.get("return_12_pct"),
                    "rsi_14": values.get("rsi_14"),
                    "close_vs_sma20_pct": values.get("close_vs_sma20_pct"),
                    "close_vs_sma50_pct": values.get("close_vs_sma50_pct"),
                    "volatility_20_pct": values.get("volatility_20_pct"),
                    "volume_ratio_20": values.get("volume_ratio_20"),
                }
        labels = row.get("labels") if isinstance(row.get("labels"), dict) else {}
        symbols[symbol] = {
            "price": row.get("price"),
            "features": compact_features,
            "label_horizons_available": sorted(labels.keys()),
        }

    return {
        "observed_at": record.get("observed_at"),
        "collected_at": record.get("collected_at"),
        "context_scores": record.get("context_scores", {}),
        "flow_alert": record.get("flow_alert", {}),
        "symbols": symbols,
    }


def build_horizon_stats(records: list[dict[str, Any]], horizons: list[str]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for horizon in horizons:
        overall_returns: list[float] = []
        by_symbol: dict[str, list[float]] = {}
        for symbol, forward_return in iter_labeled_returns(records, horizon):
            overall_returns.append(forward_return)
            by_symbol.setdefault(symbol, []).append(forward_return)
        result[horizon] = {
            "overall": return_stats(overall_returns),
            "by_symbol": {
                symbol: return_stats(values)
                for symbol, values in sorted(by_symbol.items())
            },
        }
    return result


def build_condition_stats(records: list[dict[str, Any]], horizons: list[str]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for horizon in horizons:
        grouped: dict[str, dict[str, list[float]]] = {}
        for record in records:
            if not isinstance(record, dict):
                continue
            record_features = {
                "news_risk_score": nested_float(record, ("context_scores", "news_risk_score")),
                "risk_on_score": nested_float(record, ("context_scores", "risk_on_score")),
                "market_context_score": nested_float(record, ("context_scores", "market_context_score")),
                "flow_alert_score": nested_float(record, ("flow_alert", "flow_alert_score")),
            }
            symbols = record.get("symbols", {})
            if not isinstance(symbols, dict):
                continue
            for symbol_row in symbols.values():
                if not isinstance(symbol_row, dict):
                    continue
                label = (symbol_row.get("labels") or {}).get(horizon)
                if not isinstance(label, dict):
                    continue
                forward_return = to_float(label.get("return_pct"))
                features = symbol_row.get("features") or {}
                features_1h = features.get("1h", {}) if isinstance(features, dict) else {}
                features_4h = features.get("4h", {}) if isinstance(features, dict) else {}
                feature_values = {
                    **record_features,
                    "rsi_1h": nested_float(features_1h, ("rsi_14",)),
                    "volume_ratio_1h": nested_float(features_1h, ("volume_ratio_20",)),
                    "return_12_1h": nested_float(features_1h, ("return_12_pct",)),
                    "volatility_4h": nested_float(features_4h, ("volatility_20_pct",)),
                }
                for feature_name, value in feature_values.items():
                    bucket = bucket_feature(feature_name, value)
                    if not bucket:
                        continue
                    grouped.setdefault(feature_name, {}).setdefault(bucket, []).append(forward_return)

        output[horizon] = {
            feature_name: {
                bucket: return_stats(values)
                for bucket, values in sorted(buckets.items())
            }
            for feature_name, buckets in sorted(grouped.items())
        }
    return output


def iter_labeled_returns(records: list[dict[str, Any]], horizon: str) -> list[tuple[str, float]]:
    rows = []
    for record in records:
        if not isinstance(record, dict):
            continue
        symbols = record.get("symbols", {})
        if not isinstance(symbols, dict):
            continue
        for symbol, row in symbols.items():
            if not isinstance(row, dict):
                continue
            label = (row.get("labels") or {}).get(horizon)
            if isinstance(label, dict) and label.get("return_pct") is not None:
                rows.append((symbol, to_float(label.get("return_pct"))))
    return rows


def return_stats(values: list[float]) -> dict[str, Any]:
    clean = [value for value in values if value is not None]
    if not clean:
        return {
            "count": 0,
            "avg_return_pct": None,
            "median_return_pct": None,
            "long_win_rate_pct": None,
            "short_win_rate_pct": None,
            "avg_long_pnl_pct": None,
            "avg_short_pnl_pct": None,
        }
    return {
        "count": len(clean),
        "avg_return_pct": round(sum(clean) / len(clean), 4),
        "median_return_pct": round(median(clean), 4),
        "long_win_rate_pct": round(sum(1 for value in clean if value > 0) / len(clean) * 100, 2),
        "short_win_rate_pct": round(sum(1 for value in clean if value < 0) / len(clean) * 100, 2),
        "avg_long_pnl_pct": round(sum(clean) / len(clean), 4),
        "avg_short_pnl_pct": round(sum(-value for value in clean) / len(clean), 4),
    }


def render_ai_analysis_brief(pack: dict[str, Any]) -> str:
    summary = pack.get("dataset_summary", {})
    labels = "\n".join(
        f"- {horizon}: `{count}`"
        for horizon, count in summary.get("label_counts", {}).items()
    )
    latest_prices = "\n".join(
        f"- {symbol}: `{price}`"
        for symbol, price in summary.get("latest_prices", {}).items()
    )
    horizon_rows = []
    for horizon, values in pack.get("horizon_stats", {}).items():
        overall = values.get("overall", {})
        horizon_rows.append(
            f"- {horizon}: count `{overall.get('count')}`, "
            f"avg `{overall.get('avg_return_pct')}`, "
            f"long win `{overall.get('long_win_rate_pct')}`, "
            f"short win `{overall.get('short_win_rate_pct')}`"
        )

    return (
        "# AI Analysis Brief\n\n"
        "Read this file before loading the full dataset to save AI tokens/quota.\n\n"
        f"- Updated: `{pack.get('updated_at')}`\n"
        f"- Records: `{summary.get('record_count')}`\n"
        f"- Symbols: `{', '.join(summary.get('symbols', []))}`\n"
        f"- Intervals: `{', '.join(summary.get('intervals', []))}`\n\n"
        "## Label Counts\n\n"
        f"{labels or '- No labels yet.'}\n\n"
        "## Latest Prices\n\n"
        f"{latest_prices or '- No prices collected.'}\n\n"
        "## Horizon Stats\n\n"
        f"{chr(10).join(horizon_rows) or '- No labeled returns yet.'}\n\n"
        "## Reading Order\n\n"
        "1. `data/reports/latest_ai_analysis_brief.md`\n"
        "2. `data/processed/ai_analysis_pack.json`\n"
        "3. Full `day_swing_dataset.json` only for validating a specific candidate rule.\n"
    )


def render_report(summary: dict[str, Any], record: dict[str, Any]) -> str:
    prices = "\n".join(
        f"- {symbol}: `{price}`"
        for symbol, price in summary.get("latest_prices", {}).items()
    )
    labels = "\n".join(
        f"- {horizon}: `{count}` labeled symbol observations"
        for horizon, count in summary.get("label_counts", {}).items()
    )
    feature_lines = []
    for symbol, row in record.get("symbols", {}).items():
        features = row.get("features", {}) if isinstance(row, dict) else {}
        one_hour = features.get("1h", {}) if isinstance(features, dict) else {}
        if isinstance(one_hour, dict):
            feature_lines.append(
                f"- {symbol}: 1h rsi `{one_hour.get('rsi_14')}`, "
                f"1h return_12 `{one_hour.get('return_12_pct')}`"
            )

    return (
        "# Latest Day Swing Dataset\n\n"
        f"- Updated: `{summary.get('updated_at')}`\n"
        f"- Latest observed: `{summary.get('latest_observed_at')}`\n"
        f"- Records: `{summary.get('record_count')}`\n"
        f"- Symbols: `{', '.join(summary.get('symbols', []))}`\n"
        f"- Intervals: `{', '.join(summary.get('intervals', []))}`\n"
        f"- Label horizons: `{', '.join(summary.get('label_horizons', []))}`\n\n"
        "## AI Reading\n\n"
        f"- Compact pack: `{summary.get('ai_analysis_pack')}`\n"
        f"- Compact brief: `{summary.get('ai_analysis_brief')}`\n\n"
        "## Latest Prices\n\n"
        f"{prices or '- No prices collected.'}\n\n"
        "## Label Progress\n\n"
        f"{labels or '- No labels yet.'}\n\n"
        "## Quick Features\n\n"
        f"{chr(10).join(feature_lines) or '- No features collected.'}\n"
    )


def load_dataset() -> dict[str, Any]:
    data = load_json(DATASET_FILE, default={})
    if isinstance(data, dict):
        return data
    if isinstance(data, list):
        return {"schema_version": 1, "records": data}
    return {"schema_version": 1, "records": []}


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def parse_csv(value: str) -> list[str]:
    return [part.strip() for part in value.split(",") if part.strip()]


def parse_symbols(value: str) -> list[str]:
    return [part.strip().upper() for part in value.split(",") if part.strip()]


def floor_time(dt: datetime, bucket_minutes: int) -> datetime:
    bucket = max(1, bucket_minutes)
    minute = (dt.minute // bucket) * bucket
    return dt.astimezone(timezone.utc).replace(minute=minute, second=0, microsecond=0)


def parse_time(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return parsed.astimezone(timezone.utc) if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
    except Exception:
        return None


def duration_to_minutes(value: str) -> int:
    text = value.strip().lower()
    if text.endswith("m"):
        return int(text[:-1])
    if text.endswith("h"):
        return int(text[:-1]) * 60
    if text.endswith("d"):
        return int(text[:-1]) * 24 * 60
    raise ValueError(f"Unsupported duration: {value}")


def candle_lookback() -> int:
    return int(os.getenv("DAY_SWING_CANDLE_LOOKBACK", "80"))


def pct_change(new: float, old: float) -> float | None:
    if old == 0:
        return None
    return round((new / old - 1) * 100, 4)


def nested_float(data: dict[str, Any], path: tuple[str, ...]) -> float | None:
    current: Any = data
    for key in path:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    if current is None:
        return None
    return to_float(current)


def bucket_feature(feature_name: str, value: float | None) -> str | None:
    if value is None:
        return None
    if feature_name in {"news_risk_score", "risk_on_score", "market_context_score", "flow_alert_score"}:
        return bucket_ranges(value, [(20, "<20"), (40, "20-40"), (60, "40-60"), (80, "60-80")], ">=80")
    if feature_name == "rsi_1h":
        return bucket_ranges(value, [(30, "<30"), (45, "30-45"), (55, "45-55"), (70, "55-70")], ">=70")
    if feature_name == "volume_ratio_1h":
        return bucket_ranges(value, [(0.75, "<0.75"), (1.25, "0.75-1.25"), (2.0, "1.25-2")], ">=2")
    if feature_name == "return_12_1h":
        return bucket_ranges(value, [(-2, "<-2"), (-0.5, "-2--0.5"), (0.5, "-0.5-0.5"), (2, "0.5-2")], ">=2")
    if feature_name == "volatility_4h":
        return bucket_ranges(value, [(0.5, "<0.5"), (1.0, "0.5-1"), (2.0, "1-2")], ">=2")
    return None


def bucket_ranges(value: float, ranges: list[tuple[float, str]], final_label: str) -> str:
    for upper, label in ranges:
        if value < upper:
            return label
    return final_label


def median(values: list[float]) -> float:
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def rsi(closes: list[float], period: int) -> float | None:
    if len(closes) <= period:
        return None
    gains = []
    losses = []
    for idx in range(len(closes) - period, len(closes)):
        change = closes[idx] - closes[idx - 1]
        gains.append(max(change, 0))
        losses.append(abs(min(change, 0)))
    avg_gain = average(gains)
    avg_loss = average(losses)
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return round(100 - (100 / (1 + rs)), 2)


def volatility_pct(closes: list[float]) -> float | None:
    returns = []
    for idx in range(1, len(closes)):
        if closes[idx - 1] > 0:
            returns.append((closes[idx] / closes[idx - 1] - 1) * 100)
    if len(returns) < 2:
        return None
    avg = sum(returns) / len(returns)
    variance = sum((value - avg) ** 2 for value in returns) / len(returns)
    return round(math.sqrt(variance), 4)


def average(values: list[float]) -> float:
    clean = [value for value in values if value is not None]
    return sum(clean) / len(clean) if clean else 0.0


def to_float(value: Any) -> float:
    try:
        return float(value) if value is not None else 0.0
    except (TypeError, ValueError):
        return 0.0
