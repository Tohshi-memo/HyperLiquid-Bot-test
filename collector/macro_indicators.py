from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import requests

ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = ROOT / "data" / "processed"
REPORT_DIR = ROOT / "data" / "reports"

LATEST_FILE = PROCESSED_DIR / "macro_indicators_latest.json"
HISTORY_FILE = PROCESSED_DIR / "macro_indicators_history.json"
REPORT_FILE = REPORT_DIR / "latest_macro_indicators.md"

BLS_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/{series_id}"
FRED_URL = "https://api.stlouisfed.org/fred/series/observations"
BEA_RELEASE_DATES_URL = "https://apps.bea.gov/API/signup/release_dates.json"
TREASURY_AVG_RATES_URL = (
    "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"
    "v2/accounting/od/avg_interest_rates"
)
FED_FOMC_CALENDAR_URL = "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 public-market-context-collector/1.0 (+https://github.com/Tohshi-memo/HyperLiquid-Bot-test)"
}

BLS_SERIES = {
    "us_unemployment_rate": {
        "series_id": "LNS14000000",
        "name": "US Unemployment Rate",
        "category": "employment",
        "unit": "percent",
        "frequency": "monthly",
    },
    "us_nonfarm_payrolls": {
        "series_id": "CES0000000001",
        "name": "US Nonfarm Payrolls",
        "category": "employment",
        "unit": "thousands",
        "frequency": "monthly",
    },
    "us_average_hourly_earnings": {
        "series_id": "CES0500000003",
        "name": "US Average Hourly Earnings",
        "category": "employment",
        "unit": "usd",
        "frequency": "monthly",
    },
    "us_cpi_u": {
        "series_id": "CUUR0000SA0",
        "name": "US CPI-U",
        "category": "inflation",
        "unit": "index",
        "frequency": "monthly",
    },
    "us_core_cpi_u": {
        "series_id": "CUUR0000SA0L1E",
        "name": "US Core CPI-U",
        "category": "inflation",
        "unit": "index",
        "frequency": "monthly",
    },
    "us_ppi_final_demand": {
        "series_id": "WPUFD4",
        "name": "US PPI Final Demand",
        "category": "inflation",
        "unit": "index",
        "frequency": "monthly",
    },
}

FRED_SERIES = {
    "us_2y_yield": ("DGS2", "US 2Y Treasury Yield", "rates", "percent", "daily"),
    "us_10y_yield": ("DGS10", "US 10Y Treasury Yield", "rates", "percent", "daily"),
    "us_10y_2y_spread": ("T10Y2Y", "US 10Y-2Y Treasury Spread", "rates", "percent", "daily"),
    "fed_funds_effective": ("DFF", "Effective Federal Funds Rate", "rates", "percent", "daily"),
    "fed_target_upper": ("DFEDTARU", "Federal Funds Target Upper Bound", "rates", "percent", "daily"),
    "fed_target_lower": ("DFEDTARL", "Federal Funds Target Lower Bound", "rates", "percent", "daily"),
    "sofr": ("SOFR", "Secured Overnight Financing Rate", "rates", "percent", "daily"),
    "dollar_index_broad": ("DTWEXBGS", "Trade Weighted US Dollar Index", "fx", "index", "daily"),
    "vix": ("VIXCLS", "VIX Close", "risk", "index", "daily"),
    "us_pce_price_index": ("PCEPI", "US PCE Price Index", "inflation", "index", "monthly"),
    "us_core_pce_price_index": ("PCEPILFE", "US Core PCE Price Index", "inflation", "index", "monthly"),
    "germany_10y_yield": ("IRLTLT01DEM156N", "Germany 10Y Government Bond Yield", "rates", "percent", "monthly"),
    "japan_10y_yield": ("IRLTLT01JPM156N", "Japan 10Y Government Bond Yield", "rates", "percent", "monthly"),
    "uk_10y_yield": ("IRLTLT01GBM156N", "United Kingdom 10Y Government Bond Yield", "rates", "percent", "monthly"),
    "canada_10y_yield": ("IRLTLT01CAM156N", "Canada 10Y Government Bond Yield", "rates", "percent", "monthly"),
    "euro_area_unemployment_rate": ("LRHUTTTTEZM156S", "Euro Area Unemployment Rate", "employment", "percent", "monthly"),
    "japan_unemployment_rate": ("LRHUTTTTJPM156S", "Japan Unemployment Rate", "employment", "percent", "monthly"),
    "uk_unemployment_rate": ("LRHUTTTTGBM156S", "United Kingdom Unemployment Rate", "employment", "percent", "monthly"),
}

FRED_COUNTRY_BY_KEY = {
    "germany_10y_yield": "DE",
    "japan_10y_yield": "JP",
    "uk_10y_yield": "GB",
    "canada_10y_yield": "CA",
    "euro_area_unemployment_rate": "EZ",
    "japan_unemployment_rate": "JP",
    "uk_unemployment_rate": "GB",
}

BLS_RELEASE_SOURCES = [
    {
        "key": "us_employment_situation",
        "name": "US Employment Situation",
        "category": "employment",
        "source": "BLS",
        "source_url": "https://www.bls.gov/ces/",
        "headline": "Employment Situation",
        "affects": ["us_unemployment_rate", "us_nonfarm_payrolls", "us_average_hourly_earnings"],
        "fallback_reference_period": "May 2026",
        "fallback_scheduled_for": "2026-06-05T08:30:00-04:00",
    },
    {
        "key": "us_cpi",
        "name": "US Consumer Price Index",
        "category": "inflation",
        "source": "BLS",
        "source_url": "https://www.bls.gov/cpi/",
        "headline": "Consumer Price Index",
        "affects": ["us_cpi_u", "us_core_cpi_u"],
        "fallback_reference_period": "May 2026",
        "fallback_scheduled_for": "2026-06-10T08:30:00-04:00",
    },
    {
        "key": "us_ppi",
        "name": "US Producer Price Index",
        "category": "inflation",
        "source": "BLS",
        "source_url": "https://www.bls.gov/ppi/",
        "headline": "Producer Price Index",
        "affects": ["us_ppi_final_demand"],
        "fallback_reference_period": "May 2026",
        "fallback_scheduled_for": "2026-06-11T08:30:00-04:00",
    },
]

BEA_RELEASE_SOURCES = [
    {
        "key": "us_pce",
        "name": "US Personal Income and Outlays / PCE",
        "category": "inflation",
        "source": "BEA",
        "source_url": "https://www.bea.gov/news/schedule",
        "release_name": "Personal Income and Outlays",
        "affects": ["us_pce_price_index", "us_core_pce_price_index"],
    },
    {
        "key": "us_gdp",
        "name": "US Gross Domestic Product",
        "category": "growth",
        "source": "BEA",
        "source_url": "https://www.bea.gov/news/schedule",
        "release_name": "Gross Domestic Product",
        "affects": [],
    },
]

FOMC_MEETINGS = [
    ("2026-01-28T14:00:00-05:00", "January 27-28, 2026", False),
    ("2026-03-18T14:00:00-04:00", "March 17-18, 2026", True),
    ("2026-04-29T14:00:00-04:00", "April 28-29, 2026", False),
    ("2026-06-17T14:00:00-04:00", "June 16-17, 2026", True),
    ("2026-07-29T14:00:00-04:00", "July 28-29, 2026", False),
    ("2026-09-16T14:00:00-04:00", "September 15-16, 2026", True),
    ("2026-10-28T14:00:00-04:00", "October 27-28, 2026", False),
    ("2026-12-09T14:00:00-05:00", "December 8-9, 2026", True),
]

GDP_REFERENCE_BY_DATE = {
    "2026-05-28": "Q1 2026 second estimate",
    "2026-06-25": "Q1 2026 third estimate",
    "2026-07-30": "Q2 2026 advance estimate",
    "2026-08-26": "Q2 2026 second estimate",
    "2026-09-30": "Q2 2026 third estimate",
    "2026-10-29": "Q3 2026 advance estimate",
    "2026-11-25": "Q3 2026 second estimate",
    "2026-12-23": "Q3 2026 third estimate",
}


def update_macro_indicators(now: datetime) -> dict[str, Any]:
    if os.getenv("MACRO_INDICATORS_ENABLED", "true").lower() == "false":
        return {"enabled": False, "reason": "MACRO_INDICATORS_ENABLED=false"}

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    provider_results = []
    indicators = []

    bls = collect_bls_indicators()
    provider_results.append(bls["provider"])
    indicators.extend(bls["indicators"])

    treasury = collect_treasury_average_rates()
    provider_results.append(treasury["provider"])
    indicators.extend(treasury["indicators"])

    fred = collect_fred_indicators()
    provider_results.append(fred["provider"])
    indicators.extend(fred["indicators"])

    release_calendar = collect_release_calendar(now)
    apply_next_releases(indicators, release_calendar)

    latest = {
        "schema_version": 1,
        "generated_at": now.isoformat(),
        "purpose": (
            "Macro indicator snapshot for rates, employment, inflation, dollar, "
            "and broad risk context. These are public macro inputs, not trade signals."
        ),
        "providers": provider_results,
        "release_calendar": release_calendar,
        "indicator_count": len(indicators),
        "indicators": sorted(indicators, key=lambda row: (row.get("country", ""), row.get("category", ""), row.get("key", ""))),
        "by_key": {row["key"]: row for row in indicators if row.get("key")},
        "summary": summarize_indicators(indicators),
    }

    LATEST_FILE.write_text(json.dumps(latest, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    append_history(latest)
    REPORT_FILE.write_text(render_report(latest), encoding="utf-8")

    return {
        "enabled": True,
        "updated_at": now.isoformat(),
        "latest_file": "data/processed/macro_indicators_latest.json",
        "history_file": "data/processed/macro_indicators_history.json",
        "report_file": "data/reports/latest_macro_indicators.md",
        "indicator_count": latest["indicator_count"],
        "providers": provider_results,
    }


def collect_release_calendar(now: datetime) -> list[dict[str, Any]]:
    releases = []
    for meta in BLS_RELEASE_SOURCES:
        release = collect_bls_release(meta)
        if release:
            releases.append(release)
        else:
            release = fallback_release(meta)
            release["source_fetch_status"] = "blocked_or_unavailable"
            releases.append(release)

    bea_releases, _ = collect_bea_releases(now)
    releases.extend(bea_releases)

    fomc = next_fomc_release(now)
    if fomc:
        releases.append(fomc)

    releases = sorted(
        releases,
        key=lambda row: row.get("scheduled_utc") or row.get("scheduled_for") or "",
    )
    return releases


def collect_bls_release(meta: dict[str, Any]) -> dict[str, Any] | None:
    try:
        response = requests.get(meta["source_url"], headers=REQUEST_HEADERS, timeout=20)
        response.raise_for_status()
    except Exception:
        return None
    text = html_to_text(response.text)
    pattern = (
        rf"The {re.escape(meta['headline'])} for (?P<period>.*?) is scheduled to be released on "
        r"(?P<date>[A-Z][a-z]+ \d{1,2}, \d{4}), at "
        r"(?P<time>\d{1,2}:\d{2}\s*(?:a\.m\.|p\.m\.|A\.M\.|P\.M\.)) Eastern Time"
    )
    match = re.search(pattern, text)
    if not match:
        return None
    scheduled = parse_eastern_datetime(match.group("date"), match.group("time"))
    return release_row(
        meta=meta,
        reference_period=match.group("period").strip(),
        scheduled_for=scheduled,
        calendar_status="official",
    )


def collect_bea_releases(now: datetime) -> tuple[list[dict[str, Any]], list[str]]:
    try:
        response = requests.get(BEA_RELEASE_DATES_URL, timeout=20)
        response.raise_for_status()
        payload = response.json()
    except Exception:
        return [fallback_bea_release(meta, now) for meta in BEA_RELEASE_SOURCES], [meta["key"] for meta in BEA_RELEASE_SOURCES]

    now_utc = ensure_utc(now)
    releases = []
    errors = []
    for meta in BEA_RELEASE_SOURCES:
        release_dates = payload.get(meta["release_name"], {}).get("release_dates", [])
        future_dates = []
        for value in release_dates:
            parsed = parse_iso_datetime(value)
            if parsed and parsed > now_utc:
                future_dates.append(parsed)
        if not future_dates:
            releases.append(fallback_bea_release(meta, now))
            errors.append(meta["key"])
            continue
        scheduled = min(future_dates)
        releases.append(
            release_row(
                meta=meta,
                reference_period=infer_bea_reference_period(meta["key"], scheduled),
                scheduled_for=scheduled.astimezone(ZoneInfo("America/New_York")),
                calendar_status="official",
            )
        )
    return releases, errors


def next_fomc_release(now: datetime) -> dict[str, Any] | None:
    now_utc = ensure_utc(now)
    for scheduled_text, meeting_label, has_sep in FOMC_MEETINGS:
        scheduled = parse_iso_datetime(scheduled_text)
        if not scheduled or scheduled <= now_utc:
            continue
        return release_row(
            meta={
                "key": "fomc_policy_decision",
                "name": "FOMC Policy Decision",
                "category": "rates",
                "source": "Federal Reserve",
                "source_url": FED_FOMC_CALENDAR_URL,
                "affects": ["fed_funds_effective", "fed_target_upper", "fed_target_lower"],
            },
            reference_period=meeting_label + (" / SEP" if has_sep else ""),
            scheduled_for=scheduled.astimezone(ZoneInfo("America/New_York")),
            calendar_status="official",
        )
    return None


def fallback_release(meta: dict[str, Any]) -> dict[str, Any]:
    return release_row(
        meta=meta,
        reference_period=meta.get("fallback_reference_period"),
        scheduled_for=parse_iso_datetime(meta.get("fallback_scheduled_for")),
        calendar_status="official_static",
    )


def fallback_bea_release(meta: dict[str, Any], now: datetime) -> dict[str, Any]:
    scheduled = None
    if meta["key"] == "us_pce":
        scheduled = parse_iso_datetime("2026-05-28T08:30:00-04:00")
        reference_period = "April 2026"
    else:
        scheduled = parse_iso_datetime("2026-05-28T08:30:00-04:00")
        reference_period = "Q1 2026 second estimate"
    if scheduled and scheduled <= ensure_utc(now):
        scheduled = None
        reference_period = None
    return release_row(meta=meta, reference_period=reference_period, scheduled_for=scheduled, calendar_status="official_static")


def release_row(
    meta: dict[str, Any],
    reference_period: str | None,
    scheduled_for: datetime | None,
    calendar_status: str,
) -> dict[str, Any]:
    scheduled_utc = ensure_utc(scheduled_for) if scheduled_for else None
    return {
        "key": meta.get("key"),
        "name": meta.get("name"),
        "category": meta.get("category"),
        "source": meta.get("source"),
        "source_url": meta.get("source_url"),
        "reference_period": reference_period,
        "scheduled_for": scheduled_for.isoformat() if scheduled_for else None,
        "scheduled_utc": scheduled_utc.isoformat() if scheduled_utc else None,
        "timezone": "America/New_York",
        "affects": meta.get("affects", []),
        "importance": "high",
        "calendar_status": calendar_status,
    }


def apply_next_releases(indicators: list[dict[str, Any]], releases: list[dict[str, Any]]) -> None:
    by_indicator: dict[str, dict[str, Any]] = {}
    for release in releases:
        for key in release.get("affects", []):
            by_indicator.setdefault(key, release)
    for row in indicators:
        release = by_indicator.get(row.get("key"))
        if not release:
            continue
        row["next_release"] = {
            "key": release.get("key"),
            "name": release.get("name"),
            "reference_period": release.get("reference_period"),
            "scheduled_for": release.get("scheduled_for"),
            "scheduled_utc": release.get("scheduled_utc"),
            "source_url": release.get("source_url"),
        }


def collect_bls_indicators() -> dict[str, Any]:
    indicators = []
    errors = []
    for key, meta in BLS_SERIES.items():
        try:
            response = requests.get(BLS_URL.format(series_id=meta["series_id"]), params={"latest": "true"}, timeout=20)
            response.raise_for_status()
            payload = response.json()
            row = parse_bls_latest(key, meta, payload)
            if row:
                indicators.append(row)
        except Exception as exc:
            errors.append(f"{key}: {exc}")
    return {
        "provider": {
            "name": "bls",
            "source": "https://api.bls.gov/publicAPI/v2/timeseries/data/",
            "enabled": True,
            "indicator_count": len(indicators),
            "errors": errors[:5],
        },
        "indicators": indicators,
    }


def parse_bls_latest(key: str, meta: dict[str, Any], payload: dict[str, Any]) -> dict[str, Any] | None:
    series = payload.get("Results", {}).get("series", [])
    if not series:
        return None
    data = series[0].get("data", [])
    if not data:
        return None
    latest = data[0]
    observed_at = f"{latest.get('year')}-{period_to_month(latest.get('period'))}-01"
    return indicator(
        key=key,
        name=meta["name"],
        country="US",
        category=meta["category"],
        source="BLS",
        source_id=meta["series_id"],
        frequency=meta["frequency"],
        unit=meta["unit"],
        observed_at=observed_at,
        value=to_float_or_none(latest.get("value")),
        status="latest" if latest.get("latest") == "true" else "observed",
    )


def collect_treasury_average_rates() -> dict[str, Any]:
    params = {
        "sort": "-record_date",
        "page[size]": "40",
        "fields": "record_date,security_type_desc,security_desc,avg_interest_rate_amt",
    }
    try:
        response = requests.get(TREASURY_AVG_RATES_URL, params=params, timeout=20)
        response.raise_for_status()
        rows = response.json().get("data", [])
    except Exception as exc:
        return {
            "provider": {
                "name": "treasury_avg_interest_rates",
                "source": TREASURY_AVG_RATES_URL,
                "enabled": True,
                "indicator_count": 0,
                "errors": [str(exc)],
            },
            "indicators": [],
        }

    keep = {
        "Treasury Bills": "us_treasury_avg_bill_rate",
        "Treasury Notes": "us_treasury_avg_note_rate",
        "Treasury Bonds": "us_treasury_avg_bond_rate",
        "Total Marketable": "us_treasury_avg_marketable_rate",
        "Total Interest-bearing Debt": "us_treasury_avg_interest_bearing_debt_rate",
    }
    indicators = []
    seen = set()
    for row in rows:
        desc = row.get("security_desc")
        key = keep.get(desc)
        if not key or key in seen:
            continue
        seen.add(key)
        indicators.append(
            indicator(
                key=key,
                name=f"US Treasury Average {desc} Rate",
                country="US",
                category="rates",
                source="US Treasury Fiscal Data",
                source_id=desc,
                frequency="monthly",
                unit="percent",
                observed_at=row.get("record_date"),
                value=to_float_or_none(row.get("avg_interest_rate_amt")),
                status="observed",
            )
        )

    return {
        "provider": {
            "name": "treasury_avg_interest_rates",
            "source": TREASURY_AVG_RATES_URL,
            "enabled": True,
            "indicator_count": len(indicators),
            "errors": [],
        },
        "indicators": indicators,
    }


def collect_fred_indicators() -> dict[str, Any]:
    api_key = os.getenv("FRED_API_KEY", "").strip()
    if not api_key:
        return {
            "provider": {
                "name": "fred",
                "source": FRED_URL,
                "enabled": False,
                "reason": "FRED_API_KEY is not set",
                "indicator_count": 0,
                "errors": [],
            },
            "indicators": [],
        }

    indicators = []
    errors = []
    for key, (series_id, name, category, unit, frequency) in FRED_SERIES.items():
        try:
            params = {
                "series_id": series_id,
                "api_key": api_key,
                "file_type": "json",
                "sort_order": "desc",
                "limit": "3",
            }
            response = requests.get(FRED_URL, params=params, timeout=20)
            response.raise_for_status()
            observations = [
                row for row in response.json().get("observations", [])
                if row.get("value") not in {None, "."}
            ]
            if not observations:
                continue
            latest = observations[0]
            previous = observations[1] if len(observations) > 1 else {}
            indicators.append(
                indicator(
                    key=key,
                    name=name,
                    country=FRED_COUNTRY_BY_KEY.get(key, "US"),
                    category=category,
                    source="FRED",
                    source_id=series_id,
                    frequency=frequency,
                    unit=unit,
                    observed_at=latest.get("date"),
                    value=to_float_or_none(latest.get("value")),
                    previous_value=to_float_or_none(previous.get("value")),
                    previous_observed_at=previous.get("date"),
                    status="observed",
                )
            )
        except Exception as exc:
            errors.append(f"{key}: {exc}")

    return {
        "provider": {
            "name": "fred",
            "source": FRED_URL,
            "enabled": True,
            "indicator_count": len(indicators),
            "errors": errors[:5],
        },
        "indicators": indicators,
    }


def indicator(
    key: str,
    name: str,
    country: str,
    category: str,
    source: str,
    source_id: str,
    frequency: str,
    unit: str,
    observed_at: Any,
    value: float | None,
    status: str,
    previous_value: float | None = None,
    previous_observed_at: Any = None,
) -> dict[str, Any]:
    change = None
    change_pct = None
    if value is not None and previous_value not in {None, 0}:
        change = round(value - previous_value, 6)
        change_pct = round((value / previous_value - 1) * 100, 6)
    return {
        "key": key,
        "name": name,
        "country": country,
        "category": category,
        "source": source,
        "source_id": source_id,
        "frequency": frequency,
        "unit": unit,
        "observed_at": observed_at,
        "value": value,
        "previous_observed_at": previous_observed_at,
        "previous_value": previous_value,
        "change": change,
        "change_pct": change_pct,
        "status": status,
    }


def summarize_indicators(indicators: list[dict[str, Any]]) -> dict[str, Any]:
    by_category: dict[str, int] = {}
    by_country: dict[str, int] = {}
    for row in indicators:
        by_category[row.get("category", "unknown")] = by_category.get(row.get("category", "unknown"), 0) + 1
        by_country[row.get("country", "unknown")] = by_country.get(row.get("country", "unknown"), 0) + 1
    return {
        "by_category": by_category,
        "by_country": by_country,
        "top_rates": [
            row for row in indicators
            if row.get("category") == "rates"
        ][:10],
        "employment": [
            row for row in indicators
            if row.get("category") == "employment"
        ][:10],
        "inflation": [
            row for row in indicators
            if row.get("category") == "inflation"
        ][:10],
    }


def append_history(latest: dict[str, Any]) -> None:
    max_records = int(os.getenv("MACRO_INDICATORS_HISTORY_MAX_RECORDS", "8640"))
    history = load_json(HISTORY_FILE, [])
    if not isinstance(history, list):
        history = []
    compact = {
        "generated_at": latest.get("generated_at"),
        "indicator_count": latest.get("indicator_count"),
        "values": {
            row["key"]: {
                "observed_at": row.get("observed_at"),
                "value": row.get("value"),
                "change": row.get("change"),
                "unit": row.get("unit"),
            }
            for row in latest.get("indicators", [])
            if row.get("key")
        },
    }
    history.append(compact)
    HISTORY_FILE.write_text(json.dumps(history[-max_records:], indent=2, ensure_ascii=False), encoding="utf-8")


def render_report(latest: dict[str, Any]) -> str:
    indicators = latest.get("indicators", [])
    releases = latest.get("release_calendar", [])
    provider_lines = "\n".join(
        f"- `{provider.get('name')}`: enabled `{provider.get('enabled')}`, indicators `{provider.get('indicator_count')}`"
        + (f", reason `{provider.get('reason')}`" if provider.get("reason") else "")
        for provider in latest.get("providers", [])
    )
    rows = "\n".join(
        f"- `{row.get('key')}` {row.get('name')}: `{row.get('value')}` {row.get('unit')} "
        f"at `{row.get('observed_at')}` ({row.get('source')})"
        for row in indicators[:40]
    )
    release_rows = "\n".join(
        f"- `{row.get('key')}` {row.get('name')}: `{row.get('reference_period')}` "
        f"scheduled `{row.get('scheduled_for')}` / UTC `{row.get('scheduled_utc')}` "
        f"({row.get('source')}, {row.get('calendar_status')})"
        for row in releases[:20]
    )
    return (
        "# Latest Macro Indicators\n\n"
        "Public macro indicators for rates, employment, inflation, dollar, and risk context. "
        "These are inputs for analysis, not trade signals.\n\n"
        f"- Generated: `{latest.get('generated_at')}`\n"
        f"- Indicators: `{latest.get('indicator_count')}`\n\n"
        "## Providers\n\n"
        f"{provider_lines or '- No providers.'}\n\n"
        "## Upcoming Releases\n\n"
        f"{release_rows or '- No upcoming releases collected.'}\n\n"
        "## Indicators\n\n"
        f"{rows or '- No indicators collected.'}\n"
    )


def period_to_month(period: Any) -> str:
    value = str(period or "").upper()
    if len(value) == 3 and value.startswith("M") and value[1:].isdigit():
        return value[1:]
    return "01"


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def to_float_or_none(value: Any) -> float | None:
    try:
        return float(value) if value not in {None, ""} else None
    except (TypeError, ValueError):
        return None


def html_to_text(value: str) -> str:
    text = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", unescape(text)).strip()


def parse_eastern_datetime(date_text: str, time_text: str) -> datetime:
    date_part = datetime.strptime(date_text.replace(".", ""), "%B %d, %Y")
    time_clean = time_text.lower().replace(".", "").strip()
    time_part = datetime.strptime(time_clean, "%I:%M %p").time()
    return datetime.combine(date_part.date(), time_part, tzinfo=ZoneInfo("America/New_York"))


def parse_iso_datetime(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed


def ensure_utc(value: datetime | None) -> datetime:
    if value is None:
        return datetime.min.replace(tzinfo=timezone.utc)
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def infer_bea_reference_period(key: str, scheduled: datetime) -> str | None:
    if key == "us_pce":
        month = scheduled.month - 1
        year = scheduled.year
        if month == 0:
            month = 12
            year -= 1
        return datetime(year, month, 1).strftime("%B %Y")
    if key == "us_gdp":
        return GDP_REFERENCE_BY_DATE.get(scheduled.date().isoformat(), "next scheduled GDP release")
    return None


def main() -> None:
    update_macro_indicators(datetime.now(timezone.utc))


if __name__ == "__main__":
    main()
