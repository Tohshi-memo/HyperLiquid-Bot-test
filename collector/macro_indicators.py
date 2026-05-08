from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = ROOT / "data" / "processed"
REPORT_DIR = ROOT / "data" / "reports"

LATEST_FILE = PROCESSED_DIR / "macro_indicators_latest.json"
HISTORY_FILE = PROCESSED_DIR / "macro_indicators_history.json"
REPORT_FILE = REPORT_DIR / "latest_macro_indicators.md"

BLS_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/{series_id}"
FRED_URL = "https://api.stlouisfed.org/fred/series/observations"
TREASURY_AVG_RATES_URL = (
    "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"
    "v2/accounting/od/avg_interest_rates"
)

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

    latest = {
        "schema_version": 1,
        "generated_at": now.isoformat(),
        "purpose": (
            "Macro indicator snapshot for rates, employment, inflation, dollar, "
            "and broad risk context. These are public macro inputs, not trade signals."
        ),
        "providers": provider_results,
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
    return (
        "# Latest Macro Indicators\n\n"
        "Public macro indicators for rates, employment, inflation, dollar, and risk context. "
        "These are inputs for analysis, not trade signals.\n\n"
        f"- Generated: `{latest.get('generated_at')}`\n"
        f"- Indicators: `{latest.get('indicator_count')}`\n\n"
        "## Providers\n\n"
        f"{provider_lines or '- No providers.'}\n\n"
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
