from __future__ import annotations

import csv
import io
import json
import math
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = ROOT / "data" / "processed"
REPORT_DIR = ROOT / "data" / "reports"

PRICE_HISTORY_FILE = PROCESSED_DIR / "sector_price_history.json"
LATEST_FILE = PROCESSED_DIR / "sector_reactions_latest.json"
REPORT_FILE = REPORT_DIR / "latest_sector_reactions.md"
MARKET_CONTEXT_HISTORY_FILE = PROCESSED_DIR / "market_context_history.json"
FLOW_ALERT_HISTORY_FILE = PROCESSED_DIR / "flow_alert_history.json"

DEFAULT_SECTOR_PROXIES = {
    "XLK": {"sector": "technology", "name": "Technology Select Sector SPDR"},
    "SMH": {"sector": "semiconductors", "name": "VanEck Semiconductor ETF"},
    "XLF": {"sector": "financials", "name": "Financial Select Sector SPDR"},
    "XLE": {"sector": "energy", "name": "Energy Select Sector SPDR"},
    "XLV": {"sector": "healthcare", "name": "Health Care Select Sector SPDR"},
    "XLI": {"sector": "industrials", "name": "Industrial Select Sector SPDR"},
    "XLY": {"sector": "consumer_discretionary", "name": "Consumer Discretionary Select Sector SPDR"},
    "XLP": {"sector": "consumer_staples", "name": "Consumer Staples Select Sector SPDR"},
    "XLU": {"sector": "utilities", "name": "Utilities Select Sector SPDR"},
    "XLB": {"sector": "materials", "name": "Materials Select Sector SPDR"},
    "XLRE": {"sector": "real_estate", "name": "Real Estate Select Sector SPDR"},
    "XLC": {"sector": "communication_services", "name": "Communication Services Select Sector SPDR"},
    "IWM": {"sector": "small_caps", "name": "iShares Russell 2000 ETF"},
    "IYR": {"sector": "real_estate_broad", "name": "iShares U.S. Real Estate ETF"},
    "XHB": {"sector": "homebuilders", "name": "SPDR S&P Homebuilders ETF"},
    "SPY": {"sector": "broad_market", "name": "SPDR S&P 500 ETF"},
    "QQQ": {"sector": "nasdaq_100", "name": "Invesco QQQ Trust"},
}

HORIZONS = {
    "1d": 1,
    "5d": 5,
    "20d": 20,
    "60d": 60,
    "120d": 120,
    "252d": 252,
}


def update_sector_reactions(now: datetime, context: dict[str, Any] | None = None) -> dict[str, Any]:
    if os.getenv("SECTOR_REACTIONS_ENABLED", "true").lower() == "false":
        return {"enabled": False, "reason": "SECTOR_REACTIONS_ENABLED=false"}

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    proxies = sector_proxies()
    refresh_hours = int(os.getenv("SECTOR_REACTION_REFRESH_HOURS", "12"))
    max_price_records = int(os.getenv("SECTOR_PRICE_HISTORY_MAX_RECORDS", "6500"))
    max_reaction_rows = int(os.getenv("SECTOR_REACTION_MAX_ROWS", "5000"))
    min_samples = int(os.getenv("SECTOR_REACTION_MIN_SAMPLES", "20"))
    provider = price_provider()

    price_history = load_json(PRICE_HISTORY_FILE, {})
    if should_refresh_prices(price_history, now, refresh_hours):
        records, fetch_errors = fetch_sector_price_records(proxies, max_price_records)
    else:
        records = price_history.get("records", []) if isinstance(price_history, dict) else []
        fetch_errors = []
    records = [row for row in records if isinstance(row, dict)]
    records.sort(key=lambda row: row.get("date", ""))

    price_output = {
        "schema_version": 1,
        "updated_at": now.isoformat(),
        "source": provider,
        "source_note": (
            "Daily ETF close proxies. Default provider is Yahoo chart endpoint with no key; "
            "Stooq CSV is supported when STOOQ_API_KEY is configured."
        ),
        "proxies": proxies,
        "record_count": len(records),
        "first_date": records[0].get("date") if records else None,
        "last_date": records[-1].get("date") if records else None,
        "records": records,
        "fetch_errors": fetch_errors,
    }
    PRICE_HISTORY_FILE.write_text(json.dumps(price_output, indent=2, ensure_ascii=False), encoding="utf-8")

    context_history = load_json(MARKET_CONTEXT_HISTORY_FILE, [])
    flow_history = load_json(FLOW_ALERT_HISTORY_FILE, [])
    event_points = build_event_points(records, context_history, flow_history)
    reaction_rows = build_reaction_rows(records, event_points, proxies)
    patterns = summarize_patterns(reaction_rows, min_samples)
    sector_snapshot = latest_sector_snapshot(records, proxies)

    latest = {
        "schema_version": 1,
        "generated_at": now.isoformat(),
        "purpose": (
            "Tracks event-condition -> sector/ETF proxy delayed reactions. "
            "Use this for hypothesis discovery, not direct trade decisions."
        ),
        "source": {
            "price_history": "data/processed/sector_price_history.json",
            "provider": provider,
            "provider_url": price_provider_url(provider),
        },
        "horizons": HORIZONS,
        "min_samples": min_samples,
        "proxy_count": len(proxies),
        "price_record_count": len(records),
        "event_point_count": len(event_points),
        "reaction_row_count": len(reaction_rows),
        "stored_reaction_row_count": min(len(reaction_rows), max_reaction_rows),
        "conditions": condition_catalog(),
        "sector_snapshot": sector_snapshot,
        "top_patterns": patterns[: int(os.getenv("SECTOR_REACTION_TOP_LIMIT", "50"))],
        "reaction_rows": reaction_rows[-max_reaction_rows:],
        "fetch_errors": fetch_errors,
    }
    LATEST_FILE.write_text(json.dumps(latest, indent=2, ensure_ascii=False), encoding="utf-8")
    REPORT_FILE.write_text(render_report(latest), encoding="utf-8")

    return {
        "enabled": True,
        "updated_at": now.isoformat(),
        "latest_file": "data/processed/sector_reactions_latest.json",
        "history_file": "data/processed/sector_price_history.json",
        "report_file": "data/reports/latest_sector_reactions.md",
        "proxy_count": len(proxies),
        "price_record_count": len(records),
        "pattern_count": len(patterns),
        "reaction_row_count": len(reaction_rows),
        "top_patterns": patterns[:10],
        "fetch_errors": fetch_errors,
    }


def sector_proxies() -> dict[str, dict[str, str]]:
    symbols = [item.strip().upper() for item in os.getenv("SECTOR_REACTION_SYMBOLS", "").split(",") if item.strip()]
    if not symbols:
        return DEFAULT_SECTOR_PROXIES
    return {
        symbol: DEFAULT_SECTOR_PROXIES.get(symbol, {"sector": symbol.lower(), "name": symbol})
        for symbol in symbols
    }


def should_refresh_prices(price_history: Any, now: datetime, refresh_hours: int) -> bool:
    if not isinstance(price_history, dict) or not price_history.get("records"):
        return True
    updated_at = parse_time(price_history.get("updated_at"))
    if updated_at is None:
        return True
    return now - updated_at >= timedelta(hours=refresh_hours)


def fetch_sector_price_records(
    proxies: dict[str, dict[str, str]],
    max_records: int,
) -> tuple[list[dict[str, Any]], list[str]]:
    by_date: dict[str, dict[str, float]] = {}
    fetch_errors: list[str] = []
    for symbol in proxies:
        try:
            closes = fetch_daily_closes(symbol)
        except Exception as e:
            fetch_errors.append(f"{symbol}: {e}")
            continue
        for date, close in closes[-max_records:]:
            by_date.setdefault(date, {})[symbol] = close

    records = [
        {"date": date, "prices": dict(sorted(prices.items()))}
        for date, prices in sorted(by_date.items())
        if prices
    ]
    return records[-max_records:], fetch_errors


def price_provider() -> str:
    return os.getenv("SECTOR_REACTION_PRICE_PROVIDER", "yahoo_chart").strip().lower() or "yahoo_chart"


def price_provider_url(provider: str) -> str:
    if provider in {"yahoo", "yahoo_chart", "yfinance"}:
        return "https://query1.finance.yahoo.com/"
    return "https://stooq.com/q/d/l/"


def fetch_daily_closes(symbol: str) -> list[tuple[str, float]]:
    provider = price_provider()
    if provider in {"yahoo", "yahoo_chart", "yfinance"}:
        return fetch_yahoo_chart_closes(symbol)

    api_key = os.getenv("STOOQ_API_KEY", "").strip()
    params = {"s": f"{symbol.lower()}.us", "i": "d"}
    if api_key:
        params["apikey"] = api_key
    response = requests.get(
        "https://stooq.com/q/d/l/",
        params=params,
        timeout=20,
    )
    response.raise_for_status()
    text = response.text.strip()
    lowered = text.lower()
    if not text or lowered.startswith("no data") or "get your apikey" in lowered:
        return []
    rows = csv.DictReader(io.StringIO(text))
    closes: list[tuple[str, float]] = []
    for row in rows:
        date = row.get("Date")
        close = to_float_or_none(row.get("Close"))
        if date and close is not None and close > 0:
            closes.append((date, round(close, 8)))
    return closes


def fetch_yahoo_chart_closes(symbol: str) -> list[tuple[str, float]]:
    period1 = int(datetime(1990, 1, 1, tzinfo=timezone.utc).timestamp())
    period2 = int(datetime.now(timezone.utc).timestamp())
    response = requests.get(
        f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}",
        params={"period1": period1, "period2": period2, "interval": "1d", "events": "history"},
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=20,
    )
    response.raise_for_status()
    payload = response.json()
    results = payload.get("chart", {}).get("result", []) if isinstance(payload, dict) else []
    if not results:
        return []
    result = results[0]
    timestamps = result.get("timestamp", []) if isinstance(result, dict) else []
    indicators = result.get("indicators", {}) if isinstance(result.get("indicators"), dict) else {}
    adjclose = indicators.get("adjclose", [{}])[0] if indicators.get("adjclose") else {}
    quote = indicators.get("quote", [{}])[0] if indicators.get("quote") else {}
    closes = adjclose.get("adjclose") if isinstance(adjclose, dict) else None
    if not isinstance(closes, list):
        closes = quote.get("close", []) if isinstance(quote, dict) else []
    output: list[tuple[str, float]] = []
    for timestamp, close in zip(timestamps, closes):
        parsed = to_float_or_none(close)
        if timestamp is None or parsed is None or parsed <= 0:
            continue
        date = datetime.fromtimestamp(int(timestamp), timezone.utc).strftime("%Y-%m-%d")
        output.append((date, round(parsed, 8)))
    return output


def build_event_points(
    records: list[dict[str, Any]],
    context_history: Any,
    flow_history: Any,
) -> list[dict[str, Any]]:
    context_points = parse_points(context_history)
    flow_points = parse_points(flow_history)
    output = []
    for index, record in enumerate(records):
        date = record.get("date")
        if not date:
            continue
        point_time = parse_date_end(date)
        market = latest_before(context_points, point_time) or {}
        flow = latest_before(flow_points, point_time) or {}
        output.append(
            {
                "date": date,
                "events": evaluate_conditions(records, index, market, flow),
            }
        )
    return output


def condition_catalog() -> dict[str, str]:
    return {
        "news_risk_high": "Collected news risk score is elevated.",
        "macro_risk_high": "Collected macro risk score is elevated.",
        "risk_on_high": "Collected risk-on score is elevated.",
        "market_context_high": "Collected market context score is supportive.",
        "polymarket_volume_spike": "Polymarket 24h volume z-score is elevated.",
        "flow_alert_high": "Flow alert score is elevated.",
        "energy_5d_up": "Energy proxy XLE rose at least 3% over 5 trading days.",
        "semis_5d_up": "Semiconductor proxy SMH rose at least 4% over 5 trading days.",
        "rates_sensitive_rebound": "Homebuilders or real estate rebounded at least 3% over 5 trading days.",
        "defensive_rotation": "Utilities outperformed SPY by at least 2% over 20 trading days.",
        "broad_risk_on_20d": "SPY and QQQ both rose strongly over 20 trading days.",
        "small_caps_5d_up": "IWM rose at least 3% over 5 trading days.",
    }


def evaluate_conditions(
    records: list[dict[str, Any]],
    index: int,
    market: dict[str, Any],
    flow: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    scores = market.get("scores", {}) if isinstance(market.get("scores"), dict) else {}
    flow_scores = flow.get("scores", {}) if isinstance(flow.get("scores"), dict) else {}
    poly = flow.get("polymarket", {}) if isinstance(flow.get("polymarket"), dict) else {}

    values = {
        "news_risk_high": to_float(scores.get("news_risk_score")),
        "macro_risk_high": to_float(scores.get("macro_risk_score")),
        "risk_on_high": to_float(scores.get("risk_on_score")),
        "market_context_high": to_float(scores.get("market_context_score")),
        "polymarket_volume_spike": to_float(poly.get("volume_24h_zscore_7d")),
        "flow_alert_high": to_float(flow_scores.get("flow_alert_score")),
        "energy_5d_up": trailing_return(records, index, "XLE", 5),
        "semis_5d_up": trailing_return(records, index, "SMH", 5),
        "rates_sensitive_rebound": max(
            trailing_return(records, index, "XHB", 5) or -999,
            trailing_return(records, index, "IYR", 5) or -999,
        ),
        "defensive_rotation": spread_return(records, index, "XLU", "SPY", 20),
        "broad_risk_on_20d": min(
            trailing_return(records, index, "SPY", 20) or -999,
            trailing_return(records, index, "QQQ", 20) or -999,
        ),
        "small_caps_5d_up": trailing_return(records, index, "IWM", 5),
    }
    active = {
        "news_risk_high": values["news_risk_high"] >= 55,
        "macro_risk_high": values["macro_risk_high"] >= 50,
        "risk_on_high": values["risk_on_high"] >= 55,
        "market_context_high": values["market_context_high"] >= 55,
        "polymarket_volume_spike": values["polymarket_volume_spike"] >= 1,
        "flow_alert_high": values["flow_alert_high"] >= 35,
        "energy_5d_up": values["energy_5d_up"] is not None and values["energy_5d_up"] >= 3,
        "semis_5d_up": values["semis_5d_up"] is not None and values["semis_5d_up"] >= 4,
        "rates_sensitive_rebound": values["rates_sensitive_rebound"] >= 3,
        "defensive_rotation": values["defensive_rotation"] is not None and values["defensive_rotation"] >= 2,
        "broad_risk_on_20d": values["broad_risk_on_20d"] >= 4,
        "small_caps_5d_up": values["small_caps_5d_up"] is not None and values["small_caps_5d_up"] >= 3,
    }
    return {
        key: {"active": bool(is_active), "value": round(to_float(values.get(key)), 4)}
        for key, is_active in active.items()
    }


def build_reaction_rows(
    records: list[dict[str, Any]],
    event_points: list[dict[str, Any]],
    proxies: dict[str, dict[str, str]],
) -> list[dict[str, Any]]:
    event_by_date = {point.get("date"): point.get("events", {}) for point in event_points}
    rows = []
    for index, record in enumerate(records):
        date = record.get("date")
        prices = record.get("prices", {}) if isinstance(record.get("prices"), dict) else {}
        events = event_by_date.get(date, {})
        active_events = [
            (event_key, event_data)
            for event_key, event_data in events.items()
            if isinstance(event_data, dict) and event_data.get("active")
        ]
        if not active_events:
            continue
        for event_key, event_data in active_events:
            for proxy, meta in proxies.items():
                start_price = to_float_or_none(prices.get(proxy))
                if start_price is None or start_price <= 0:
                    continue
                labels = build_labels(records, index, proxy, start_price)
                if not labels:
                    continue
                rows.append(
                    {
                        "event_date": date,
                        "event_key": event_key,
                        "event_value": event_data.get("value"),
                        "proxy": proxy,
                        "sector": meta.get("sector"),
                        "name": meta.get("name"),
                        "start_price": round(start_price, 8),
                        "labels": labels,
                    }
                )
    return rows


def build_labels(
    records: list[dict[str, Any]],
    index: int,
    proxy: str,
    start_price: float,
) -> dict[str, dict[str, Any]]:
    labels = {}
    for horizon, offset in HORIZONS.items():
        future_index = index + offset
        if future_index >= len(records):
            continue
        future = records[future_index]
        future_prices = future.get("prices", {}) if isinstance(future.get("prices"), dict) else {}
        future_price = to_float_or_none(future_prices.get(proxy))
        if future_price is None or future_price <= 0:
            continue
        labels[horizon] = {
            "date": future.get("date"),
            "price": round(future_price, 8),
            "return_pct": round((future_price / start_price - 1) * 100, 4),
        }
    return labels


def summarize_patterns(rows: list[dict[str, Any]], min_samples: int) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str], list[float]] = {}
    for row in rows:
        labels = row.get("labels", {}) if isinstance(row.get("labels"), dict) else {}
        for horizon, label in labels.items():
            if not isinstance(label, dict):
                continue
            ret = to_float_or_none(label.get("return_pct"))
            if ret is None:
                continue
            grouped.setdefault((str(row.get("event_key")), str(row.get("proxy")), horizon), []).append(ret)

    patterns = []
    for (event_key, proxy, horizon), values in grouped.items():
        summary = summarize_returns(values)
        meta = DEFAULT_SECTOR_PROXIES.get(proxy, {"sector": proxy.lower(), "name": proxy})
        summary.update(
            {
                "pattern_id": f"{event_key}->{proxy}_{horizon}",
                "event_key": event_key,
                "proxy": proxy,
                "sector": meta.get("sector"),
                "name": meta.get("name"),
                "horizon": horizon,
                "sample_status": "ready" if summary["sample_count"] >= min_samples else "thin_sample",
                "score": pattern_score(summary, min_samples),
                "worst_return_pct": worst_return(values),
                "p10_return_pct": percentile_return(values, 0.10),
                "longest_loss_streak": longest_loss_streak(values),
            }
        )
        patterns.append(summary)

    patterns.sort(
        key=lambda row: (
            row.get("sample_status") == "ready",
            row.get("score", -999),
            row.get("sample_count", 0),
        ),
        reverse=True,
    )
    return patterns


def latest_sector_snapshot(records: list[dict[str, Any]], proxies: dict[str, dict[str, str]]) -> list[dict[str, Any]]:
    if not records:
        return []
    latest_index = len(records) - 1
    latest = records[latest_index]
    prices = latest.get("prices", {}) if isinstance(latest.get("prices"), dict) else {}
    rows = []
    for proxy, meta in proxies.items():
        price = to_float_or_none(prices.get(proxy))
        if price is None:
            continue
        rows.append(
            {
                "proxy": proxy,
                "sector": meta.get("sector"),
                "name": meta.get("name"),
                "date": latest.get("date"),
                "price": price,
                "return_5d_pct": trailing_return(records, latest_index, proxy, 5),
                "return_20d_pct": trailing_return(records, latest_index, proxy, 20),
                "return_60d_pct": trailing_return(records, latest_index, proxy, 60),
            }
        )
    rows.sort(key=lambda row: abs(to_float(row.get("return_20d_pct"))), reverse=True)
    return rows


def trailing_return(records: list[dict[str, Any]], index: int, symbol: str, offset: int) -> float | None:
    previous_index = index - offset
    if previous_index < 0:
        return None
    current_prices = records[index].get("prices", {}) if isinstance(records[index].get("prices"), dict) else {}
    previous_prices = records[previous_index].get("prices", {}) if isinstance(records[previous_index].get("prices"), dict) else {}
    current = to_float_or_none(current_prices.get(symbol))
    previous = to_float_or_none(previous_prices.get(symbol))
    if current is None or previous is None or previous <= 0:
        return None
    return round((current / previous - 1) * 100, 4)


def spread_return(records: list[dict[str, Any]], index: int, left: str, right: str, offset: int) -> float | None:
    left_return = trailing_return(records, index, left, offset)
    right_return = trailing_return(records, index, right, offset)
    if left_return is None or right_return is None:
        return None
    return round(left_return - right_return, 4)


def summarize_returns(values: list[float]) -> dict[str, Any]:
    clean = [value for value in values if value is not None and not math.isnan(value)]
    if not clean:
        return {"sample_count": 0, "avg_return_pct": 0.0, "median_return_pct": 0.0, "up_rate_pct": 0.0}
    ordered = sorted(clean)
    mid = len(ordered) // 2
    median = ordered[mid] if len(ordered) % 2 else (ordered[mid - 1] + ordered[mid]) / 2
    return {
        "sample_count": len(clean),
        "avg_return_pct": round(sum(clean) / len(clean), 4),
        "median_return_pct": round(median, 4),
        "up_rate_pct": round(sum(1 for value in clean if value > 0) / len(clean) * 100, 4),
    }


def pattern_score(row: dict[str, Any], min_samples: int) -> float:
    sample_count = int(row.get("sample_count") or 0)
    sample_factor = min(1.0, sample_count / max(1, min_samples))
    return round(
        (
            to_float(row.get("avg_return_pct")) * 16
            + (to_float(row.get("up_rate_pct")) - 50) * 0.08
        )
        * sample_factor,
        4,
    )


def worst_return(values: list[float]) -> float:
    clean = sorted(value for value in values if value is not None and not math.isnan(value))
    return round(clean[0], 4) if clean else 0.0


def percentile_return(values: list[float], percentile: float) -> float:
    clean = sorted(value for value in values if value is not None and not math.isnan(value))
    if not clean:
        return 0.0
    index = min(len(clean) - 1, max(0, int((len(clean) - 1) * percentile)))
    return round(clean[index], 4)


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


def render_report(latest: dict[str, Any]) -> str:
    snapshot_rows = "\n".join(
        f"- `{row.get('proxy')}` {row.get('sector')}: 5d `{row.get('return_5d_pct')}`, "
        f"20d `{row.get('return_20d_pct')}`, 60d `{row.get('return_60d_pct')}`"
        for row in latest.get("sector_snapshot", [])[:12]
    )
    pattern_rows = "\n".join(
        f"- `{row.get('pattern_id')}` score `{row.get('score')}`, n `{row.get('sample_count')}`, "
        f"avg `{row.get('avg_return_pct')}`, up `{row.get('up_rate_pct')}`, status `{row.get('sample_status')}`"
        for row in latest.get("top_patterns", [])[:25]
    )
    condition_rows = "\n".join(
        f"- `{key}`: {value}"
        for key, value in latest.get("conditions", {}).items()
    )
    return (
        "# Latest Sector Reactions\n\n"
        "Sector reaction data tracks how ETF sector proxies moved after public conditions. "
        "It is a hypothesis dataset, not a trade signal.\n\n"
        f"- Generated: `{latest.get('generated_at')}`\n"
        f"- Price records: `{latest.get('price_record_count')}`\n"
        f"- Reaction rows: `{latest.get('reaction_row_count')}`\n"
        f"- Stored reaction rows: `{latest.get('stored_reaction_row_count')}`\n"
        f"- Minimum samples: `{latest.get('min_samples')}`\n"
        f"- Horizons: `{', '.join(latest.get('horizons', {}).keys())}`\n\n"
        "## Sector Snapshot\n\n"
        f"{snapshot_rows or '- No sector prices yet.'}\n\n"
        "## Top Delayed-Reaction Patterns\n\n"
        f"{pattern_rows or '- No patterns yet.'}\n\n"
        "## Conditions\n\n"
        f"{condition_rows or '- No conditions.'}\n"
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
    points.sort(key=lambda row: row["_time"])
    return points


def latest_before(points: list[dict[str, Any]], point_time: datetime) -> dict[str, Any] | None:
    current = None
    for point in points:
        if point["_time"] <= point_time:
            current = point
        else:
            break
    return current


def parse_date_end(value: str) -> datetime:
    parsed = datetime.fromisoformat(value).replace(tzinfo=timezone.utc)
    return parsed + timedelta(hours=23, minutes=59, seconds=59)


def parse_time(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return parsed.astimezone(timezone.utc) if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
    except Exception:
        return None


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def to_float(value: Any) -> float:
    try:
        return float(value) if value is not None else 0.0
    except (TypeError, ValueError):
        return 0.0


def to_float_or_none(value: Any) -> float | None:
    try:
        return float(value) if value is not None and value != "" else None
    except (TypeError, ValueError):
        return None


if __name__ == "__main__":
    update_sector_reactions(datetime.now(timezone.utc))
