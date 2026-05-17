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
ARCHIVE_DIR = ROOT / "data" / "archive"

AI_INDEX_FILE = PROCESSED_DIR / "ai_context_index.json"
AI_INDEX_REPORT_FILE = REPORT_DIR / "latest_ai_context_index.md"
CANARY_FILE = PROCESSED_DIR / "canary_signals.json"
CANARY_REPORT_FILE = REPORT_DIR / "latest_canary_signals.md"

ASSET_UNIVERSE_FILE = PROCESSED_DIR / "asset_universe_latest.json"
ASSET_PRICE_HISTORY_FILE = PROCESSED_DIR / "asset_price_history.json"
ASSET_FEATURES_FILE = PROCESSED_DIR / "asset_features_latest.json"
ASSET_FEATURES_REPORT_FILE = REPORT_DIR / "latest_asset_features.md"
DAY_SWING_FILE = PROCESSED_DIR / "day_swing_dataset.json"
AI_ANALYSIS_PACK_FILE = PROCESSED_DIR / "ai_analysis_pack.json"
MARKET_CONTEXT_HISTORY_FILE = PROCESSED_DIR / "market_context_history.json"
FLOW_ALERT_FILE = PROCESSED_DIR / "flow_alert.json"
FLOW_ALERT_HISTORY_FILE = PROCESSED_DIR / "flow_alert_history.json"
POLYMARKET_OUTCOME_HISTORY_FILE = PROCESSED_DIR / "polymarket_outcome_history.json"
POLYMARKET_OUTCOME_LATEST_FILE = PROCESSED_DIR / "polymarket_outcome_latest.json"
MACRO_INDICATORS_FILE = PROCESSED_DIR / "macro_indicators_latest.json"
MACRO_INDICATORS_HISTORY_FILE = PROCESSED_DIR / "macro_indicators_history.json"
MACRO_INDICATORS_REPORT_FILE = REPORT_DIR / "latest_macro_indicators.md"
HIP4_OUTCOME_FILE = PROCESSED_DIR / "hip4_outcome_latest.json"
HIP4_OUTCOME_HISTORY_FILE = PROCESSED_DIR / "hip4_outcome_history.json"
HIP4_OUTCOME_REPORT_FILE = REPORT_DIR / "latest_hip4_outcome.md"
RELATIONSHIP_SCAN_FILE = PROCESSED_DIR / "relationship_scan_latest.json"
RELATIONSHIP_SCAN_REPORT_FILE = REPORT_DIR / "latest_relationship_scan.md"
SECTOR_REACTIONS_FILE = PROCESSED_DIR / "sector_reactions_latest.json"
SECTOR_PRICE_HISTORY_FILE = PROCESSED_DIR / "sector_price_history.json"
SECTOR_REACTIONS_REPORT_FILE = REPORT_DIR / "latest_sector_reactions.md"

RETURN_HORIZONS = {
    "15m": timedelta(minutes=15),
    "1h": timedelta(hours=1),
    "4h": timedelta(hours=4),
    "24h": timedelta(hours=24),
}


def update_ai_index(now: datetime, context: dict[str, Any]) -> dict[str, Any]:
    if os.getenv("AI_INDEX_ENABLED", "true").lower() == "false":
        return {"enabled": False, "reason": "AI_INDEX_ENABLED=false"}

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    asset_universe = load_json(ASSET_UNIVERSE_FILE, {})
    asset_features = load_json(ASSET_FEATURES_FILE, {})
    price_history = load_json(ASSET_PRICE_HISTORY_FILE, {})
    day_swing = load_json(DAY_SWING_FILE, {})
    ai_pack = load_json(AI_ANALYSIS_PACK_FILE, {})
    market_history = load_json(MARKET_CONTEXT_HISTORY_FILE, [])
    flow_history = load_json(FLOW_ALERT_HISTORY_FILE, [])
    polymarket_outcome_history = load_json(POLYMARKET_OUTCOME_HISTORY_FILE, [])
    macro_indicators = load_json(MACRO_INDICATORS_FILE, {})
    macro_history = load_json(MACRO_INDICATORS_HISTORY_FILE, [])
    flow_alert = load_json(FLOW_ALERT_FILE, {})
    hip4_outcome = load_json(HIP4_OUTCOME_FILE, {})
    hip4_outcome_history = load_json(HIP4_OUTCOME_HISTORY_FILE, [])
    relationship_scan = load_json(RELATIONSHIP_SCAN_FILE, {})
    sector_reactions = load_json(SECTOR_REACTIONS_FILE, {})

    canary = build_canary_signals(
        now=now,
        context=context,
        flow_alert=flow_alert,
        asset_universe=asset_universe,
        price_history=price_history,
        market_history=market_history,
        flow_history=flow_history,
    )
    CANARY_FILE.write_text(json.dumps(canary, indent=2, ensure_ascii=False), encoding="utf-8")
    CANARY_REPORT_FILE.write_text(render_canary_report(canary), encoding="utf-8")

    index = build_ai_index(
        now=now,
        context=context,
        flow_alert=flow_alert,
        asset_universe=asset_universe,
        asset_features=asset_features,
        price_history=price_history,
        day_swing=day_swing,
        ai_pack=ai_pack,
        market_history=market_history,
        flow_history=flow_history,
        polymarket_outcome_history=polymarket_outcome_history,
        macro_indicators=macro_indicators,
        macro_history=macro_history,
        canary=canary,
        hip4_outcome=hip4_outcome,
        hip4_outcome_history=hip4_outcome_history,
        relationship_scan=relationship_scan,
        sector_reactions=sector_reactions,
    )
    AI_INDEX_FILE.write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
    AI_INDEX_REPORT_FILE.write_text(render_index_report(index), encoding="utf-8")

    return {
        "enabled": True,
        "updated_at": now.isoformat(),
        "index_file": "data/processed/ai_context_index.json",
        "index_report": "data/reports/latest_ai_context_index.md",
        "canary_file": "data/processed/canary_signals.json",
        "canary_report": "data/reports/latest_canary_signals.md",
        "canary_signal_count": len(canary.get("signals", [])),
        "correlation_status": canary.get("correlation_status"),
    }


def build_ai_index(
    now: datetime,
    context: dict[str, Any],
    flow_alert: dict[str, Any],
    asset_universe: dict[str, Any],
    asset_features: dict[str, Any],
    price_history: dict[str, Any],
    day_swing: dict[str, Any],
    ai_pack: dict[str, Any],
    market_history: list[Any],
    flow_history: list[Any],
    polymarket_outcome_history: list[Any],
    macro_indicators: dict[str, Any],
    macro_history: list[Any],
    canary: dict[str, Any],
    hip4_outcome: dict[str, Any] | None = None,
    hip4_outcome_history: list[Any] | None = None,
    relationship_scan: dict[str, Any] | None = None,
    sector_reactions: dict[str, Any] | None = None,
) -> dict[str, Any]:
    hip4_outcome = hip4_outcome if isinstance(hip4_outcome, dict) else {}
    hip4_outcome_history = hip4_outcome_history if isinstance(hip4_outcome_history, list) else []
    relationship_scan = relationship_scan if isinstance(relationship_scan, dict) else {}
    sector_reactions = sector_reactions if isinstance(sector_reactions, dict) else {}
    polymarket_outcome_history = (
        polymarket_outcome_history if isinstance(polymarket_outcome_history, list) else []
    )
    macro_indicators = macro_indicators if isinstance(macro_indicators, dict) else {}
    macro_history = macro_history if isinstance(macro_history, list) else []
    records = price_history.get("records", []) if isinstance(price_history, dict) else []
    if not isinstance(records, list):
        records = []
    day_records = day_swing.get("records", []) if isinstance(day_swing, dict) else []
    if not isinstance(day_records, list):
        day_records = []

    latest_record = records[-1] if records and isinstance(records[-1], dict) else {}
    asset_price_archive_files = sorted(
        f"data/archive/{path.name}"
        for path in ARCHIVE_DIR.glob("asset_price_history_*.jsonl.gz")
    )
    polymarket_outcome_archive_files = sorted(
        f"data/archive/{path.name}"
        for path in ARCHIVE_DIR.glob("polymarket_outcome_history_*.jsonl.gz")
    )
    archive_files = asset_price_archive_files + polymarket_outcome_archive_files
    label_counts = (
        ai_pack.get("dataset_summary", {}).get("label_counts")
        if isinstance(ai_pack.get("dataset_summary"), dict)
        else None
    )

    return {
        "schema_version": 1,
        "updated_at": now.isoformat(),
        "purpose": (
            "Read this index first. It points AI analysis to compact summaries and "
            "precomputed canary signals before any large row-level JSON is loaded."
        ),
        "recommended_reading_order": [
            "data/reports/latest_ai_context_index.md",
            "data/processed/ai_context_index.json",
            "data/reports/latest_canary_signals.md",
            "data/processed/canary_signals.json",
            "data/reports/latest_ai_analysis_brief.md",
            "data/reports/latest_macro_indicators.md",
            "data/processed/ai_analysis_pack.json",
            "data/reports/latest_asset_universe.md",
            "data/reports/latest_relationship_scan.md",
            "data/reports/latest_sector_reactions.md",
            "Load full JSON files only for validating a specific candidate rule.",
        ],
        "source_repository": "https://github.com/Tohshi-memo/HyperLiquid-Bot-test.git",
        "private_strategy_repository": "https://github.com/Tohshi-memo/hyperliquid-swing-trader.git",
        "files": build_file_catalog(archive_files),
        "dataset_health": {
            "market_context_history_records": len(market_history) if isinstance(market_history, list) else 0,
            "flow_alert_history_records": len(flow_history) if isinstance(flow_history, list) else 0,
            "polymarket_outcome_history_records": len(polymarket_outcome_history),
            "macro_indicator_count": macro_indicators.get("indicator_count"),
            "macro_indicator_history_records": len(macro_history),
            "asset_price_active_records": len(records),
            "asset_price_active_window": {
                "first_observed_at": records[0].get("observed_at") if records and isinstance(records[0], dict) else None,
                "last_observed_at": records[-1].get("observed_at") if records and isinstance(records[-1], dict) else None,
            },
            "asset_price_archive_files": asset_price_archive_files,
            "polymarket_outcome_archive_files": polymarket_outcome_archive_files,
            "archive_files": archive_files,
            "asset_count": asset_universe.get("asset_count") if isinstance(asset_universe, dict) else None,
            "asset_feature_count": asset_features.get("asset_count") if isinstance(asset_features, dict) else None,
            "priced_asset_count": latest_record.get("priced_asset_count"),
            "asset_class_counts": (
                asset_universe.get("asset_class_counts") if isinstance(asset_universe, dict) else {}
            ),
            "day_swing_records": len(day_records),
            "day_swing_label_counts": label_counts or {},
            "hip4_outcome_count": hip4_outcome.get("outcome_count"),
            "hip4_side_count": hip4_outcome.get("side_count"),
            "hip4_outcome_history_records": len(hip4_outcome_history),
            "hip4_outcome_by_underlying": hip4_outcome.get("by_underlying", {}),
            "hip4_outcome_by_class": hip4_outcome.get("by_class", {}),
            "hip4_outcome_request_errors": hip4_outcome.get("request_errors", []),
            "hip4_outcome_request_warnings": hip4_outcome.get("request_warnings", []),
            "relationship_pattern_count": relationship_scan.get("pattern_count"),
            "relationship_min_samples": relationship_scan.get("min_samples"),
            "sector_reaction_price_records": sector_reactions.get("price_record_count"),
            "sector_reaction_rows": sector_reactions.get("reaction_row_count"),
            "sector_reaction_proxy_count": sector_reactions.get("proxy_count"),
        },
        "latest_market_snapshot": {
            "generated_at": context.get("generated_at"),
            "scores": context.get("scores", {}),
            "news": {
                "article_count": context.get("news", {}).get("article_count"),
                "risk_keyword_hits": context.get("news", {}).get("risk_keyword_hits"),
                "sentiment_score": context.get("news", {}).get("sentiment_score"),
            },
            "polymarket_market_count": context.get("polymarket", {}).get("market_count"),
            "macro_indicators": {
                "generated_at": macro_indicators.get("generated_at"),
                "indicator_count": macro_indicators.get("indicator_count"),
                "summary": macro_indicators.get("summary", {}),
                "providers": macro_indicators.get("providers", []),
            },
            "flow_alert": {
                "generated_at": flow_alert.get("generated_at"),
                "scores": flow_alert.get("scores", {}),
                "large_flows": flow_alert.get("large_flows", {}),
                "polymarket": flow_alert.get("polymarket", {}),
            },
            "hip4_outcome": {
                "generated_at": hip4_outcome.get("generated_at"),
                "outcome_count": hip4_outcome.get("outcome_count"),
                "side_count": hip4_outcome.get("side_count"),
                "by_underlying": hip4_outcome.get("by_underlying", {}),
                "by_class": hip4_outcome.get("by_class", {}),
                "by_status": hip4_outcome.get("by_status", {}),
                "request_errors": hip4_outcome.get("request_errors", []),
                "request_warnings": hip4_outcome.get("request_warnings", []),
            },
            "relationship_scan": {
                "generated_at": relationship_scan.get("generated_at"),
                "pattern_count": relationship_scan.get("pattern_count"),
                "min_samples": relationship_scan.get("min_samples"),
                "top_patterns": relationship_scan.get("top_patterns", [])[:5],
                "top_symbol_patterns": relationship_scan.get("top_symbol_patterns", [])[:5],
            },
            "sector_reactions": {
                "generated_at": sector_reactions.get("generated_at"),
                "price_record_count": sector_reactions.get("price_record_count"),
                "reaction_row_count": sector_reactions.get("reaction_row_count"),
                "top_patterns": sector_reactions.get("top_patterns", [])[:5],
                "sector_snapshot": sector_reactions.get("sector_snapshot", [])[:8],
            },
            "asset_features": {
                "generated_at": asset_features.get("generated_at"),
                "observed_at": asset_features.get("observed_at"),
                "asset_count": asset_features.get("asset_count"),
                "top_assets": asset_features.get("top_assets", [])[:10],
            },
        },
        "canary_summary": {
            "status": canary.get("correlation_status"),
            "sample_status": canary.get("sample_status"),
            "signals": canary.get("signals", [])[: int(os.getenv("CANARY_TOP_LIMIT", "10"))],
            "class_returns": canary.get("class_returns", {}),
            "correlations": canary.get("correlations", []),
        },
        "analysis_policy": {
            "normal_first_pass": (
                "Use index, canary report, AI analysis pack, and markdown reports only."
            ),
            "read_full_latest_assets_when": (
                "Checking individual symbol asset_class, asset_id, funding, open interest, "
                "volume, HIP-3 dex, or order feasibility."
            ),
            "read_asset_features_when": (
                "Checking individual equity, commodity, metal, index, FX, or crypto candidates "
                "without loading full all-symbol history."
            ),
            "read_macro_indicators_when": (
                "Checking rates, employment, inflation, dollar, VIX, or macro-release context "
                "before validating price behavior."
            ),
            "read_full_price_history_when": (
                "Testing cross-asset lead/lag, Polymarket/news/flow correlation, or a "
                "specific class-level signal."
            ),
            "read_archives_when": (
                "The active window is insufficient for a candidate rule and older samples "
                "are required. Archives are compressed to reduce repo bloat and AI reading."
            ),
            "read_hip4_outcome_when": (
                "Checking HyperLiquid prediction-market probabilities, outcome-side drift, "
                "or lead/lag versus Polymarket, news, or asset-class price moves."
            ),
            "read_polymarket_outcome_history_when": (
                "Checking candidate/person probability drift inside Polymarket event groups, "
                "especially Yes/No markets where the person name is stored as subject_name."
            ),
            "read_relationship_scan_when": (
                "Selecting public, mechanically discovered A/B -> future-return candidates "
                "for private AI hypothesis review and strategy validation."
            ),
            "read_sector_reactions_when": (
                "Checking delayed sector/ETF reactions over 1d, 5d, 20d, 60d, 120d, "
                "or 252d after public event conditions."
            ),
        },
    }


def build_file_catalog(archive_files: list[str]) -> dict[str, Any]:
    return {
        "first_read": [
            file_entry("data/reports/latest_ai_context_index.md", AI_INDEX_REPORT_FILE, "Human-readable map."),
            file_entry("data/processed/ai_context_index.json", AI_INDEX_FILE, "Machine-readable map."),
            file_entry("data/reports/latest_canary_signals.md", CANARY_REPORT_FILE, "Current canary signals."),
            file_entry("data/reports/latest_ai_analysis_brief.md", REPORT_DIR / "latest_ai_analysis_brief.md", "BTC/ETH/HYPE/SOL compact stats."),
            file_entry("data/reports/latest_macro_indicators.md", MACRO_INDICATORS_REPORT_FILE, "Macro rates, employment, inflation, dollar, and risk overview."),
            file_entry("data/processed/ai_analysis_pack.json", AI_ANALYSIS_PACK_FILE, "Compact strategy stats."),
            file_entry("data/reports/latest_asset_universe.md", REPORT_DIR / "latest_asset_universe.md", "Asset-class overview."),
            file_entry("data/reports/latest_asset_features.md", ASSET_FEATURES_REPORT_FILE, "Individual asset screen."),
            file_entry("data/reports/latest_hip4_outcome.md", HIP4_OUTCOME_REPORT_FILE, "HIP-4 outcome market overview."),
            file_entry("data/reports/latest_relationship_scan.md", RELATIONSHIP_SCAN_REPORT_FILE, "Mechanical relationship candidates."),
            file_entry("data/reports/latest_sector_reactions.md", SECTOR_REACTIONS_REPORT_FILE, "Delayed sector reaction overview."),
        ],
        "conditional": [
            file_entry("data/processed/asset_universe_latest.json", ASSET_UNIVERSE_FILE, "Latest all-symbol rows."),
            file_entry("data/processed/asset_features_latest.json", ASSET_FEATURES_FILE, "Individual returns, volume, OI, funding, and best relationship candidates."),
            file_entry("data/processed/asset_price_history.json", ASSET_PRICE_HISTORY_FILE, "Active all-symbol 15m price window."),
            file_entry("data/processed/day_swing_dataset.json", DAY_SWING_FILE, "Full BTC/ETH/HYPE/SOL feature and label rows."),
            file_entry("data/processed/market_context_history.json", MARKET_CONTEXT_HISTORY_FILE, "News/context history."),
            file_entry("data/processed/flow_alert_history.json", FLOW_ALERT_HISTORY_FILE, "Polymarket/flow history."),
            file_entry("data/processed/polymarket_outcome_latest.json", POLYMARKET_OUTCOME_LATEST_FILE, "Latest per-outcome Polymarket probability rows for the report site."),
            file_entry("data/processed/polymarket_outcome_history.json", POLYMARKET_OUTCOME_HISTORY_FILE, "Per-outcome Polymarket probability history with subject/person names."),
            file_entry("data/processed/macro_indicators_latest.json", MACRO_INDICATORS_FILE, "Latest macro indicators from BLS, Treasury, and optional FRED."),
            file_entry("data/processed/macro_indicators_history.json", MACRO_INDICATORS_HISTORY_FILE, "Macro indicator history for lead/lag checks."),
            file_entry("data/processed/hip4_outcome_latest.json", HIP4_OUTCOME_FILE, "Latest HIP-4 outcome rows with implied probabilities."),
            file_entry("data/processed/hip4_outcome_history.json", HIP4_OUTCOME_HISTORY_FILE, "HIP-4 outcome history with per-bucket implied probabilities."),
            file_entry("data/processed/relationship_scan_latest.json", RELATIONSHIP_SCAN_FILE, "Mechanical A/B -> future-return candidate patterns."),
            file_entry("data/processed/sector_reactions_latest.json", SECTOR_REACTIONS_FILE, "Event-condition -> sector ETF delayed reaction patterns."),
            file_entry("data/processed/sector_price_history.json", SECTOR_PRICE_HISTORY_FILE, "Daily sector ETF proxy price history."),
        ],
        "archives": [
            {"path": path, "when_to_read": "Only for longer backtests after a specific rule is selected."}
            for path in archive_files
        ],
    }


def file_entry(path: str, full_path: Path, note: str) -> dict[str, Any]:
    return {
        "path": path,
        "bytes": full_path.stat().st_size if full_path.exists() else 0,
        "note": note,
    }


def build_canary_signals(
    now: datetime,
    context: dict[str, Any],
    flow_alert: dict[str, Any],
    asset_universe: dict[str, Any],
    price_history: dict[str, Any],
    market_history: list[Any],
    flow_history: list[Any],
) -> dict[str, Any]:
    records = price_history.get("records", []) if isinstance(price_history, dict) else []
    if not isinstance(records, list):
        records = []
    records = [record for record in records if isinstance(record, dict)]
    records.sort(key=lambda item: item.get("observed_at", ""))

    class_map = build_class_map(asset_universe)
    class_returns = compute_class_returns(records, class_map)
    signals = current_signals(context, flow_alert, class_returns)
    sample_min = int(os.getenv("CANARY_MIN_SAMPLES", "24"))
    correlations = compute_correlations(records, class_map, market_history, flow_history, sample_min)
    top_limit = int(os.getenv("CANARY_TOP_LIMIT", "10"))

    return {
        "schema_version": 1,
        "updated_at": now.isoformat(),
        "purpose": (
            "Small cross-market canary pack for detecting early links among news, "
            "Polymarket flow, large-flow alerts, and HyperLiquid asset-class prices."
        ),
        "sample_status": sample_status(records, market_history, flow_history, sample_min),
        "correlation_status": "ready" if any(item.get("sample_count", 0) >= sample_min for item in correlations) else "insufficient_samples",
        "signals": signals[:top_limit],
        "class_returns": class_returns,
        "correlations": correlations[:top_limit],
        "watch_rules": [
            "High flow_alert_score followed by crypto_major or crypto_alt class move.",
            "Polymarket 24h volume z-score spike before crypto or equity/index perp move.",
            "News risk spike with metal outperformance or crypto underperformance.",
            "Index/equity perp strength leading crypto_major strength or weakness.",
            "FX/commodity stress moving before broad crypto volatility.",
        ],
        "source_files": [
            "data/processed/asset_price_history.json",
            "data/processed/market_context_history.json",
            "data/processed/flow_alert_history.json",
            "data/processed/asset_universe_latest.json",
        ],
    }


def build_class_map(asset_universe: dict[str, Any]) -> dict[str, str]:
    if not isinstance(asset_universe, dict):
        return {}
    rows = asset_universe.get("assets", [])
    if not isinstance(rows, list):
        return {}
    mapping = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        symbol = row.get("symbol")
        asset_class = row.get("asset_class")
        if symbol and asset_class:
            mapping[str(symbol)] = str(asset_class)
    return mapping


def compute_class_returns(records: list[dict[str, Any]], class_map: dict[str, str]) -> dict[str, Any]:
    if len(records) < 2:
        return {}

    latest = records[-1]
    latest_time = parse_time(latest.get("observed_at"))
    latest_prices = latest.get("prices", {}) if isinstance(latest.get("prices"), dict) else {}
    if latest_time is None or not latest_prices:
        return {}

    output: dict[str, Any] = {}
    for horizon_name, delta in RETURN_HORIZONS.items():
        previous = find_record_at_or_before(records, latest_time - delta)
        previous_prices = previous.get("prices", {}) if isinstance(previous, dict) else {}
        rows_by_class: dict[str, list[float]] = {}
        for symbol, current_price in latest_prices.items():
            previous_price = to_float(previous_prices.get(symbol))
            current = to_float(current_price)
            if previous_price <= 0 or current <= 0:
                continue
            asset_class = class_map.get(str(symbol), "unknown")
            rows_by_class.setdefault(asset_class, []).append((current / previous_price - 1) * 100)

        output[horizon_name] = {
            asset_class: return_summary(values)
            for asset_class, values in sorted(rows_by_class.items())
        }
    return output


def current_signals(
    context: dict[str, Any],
    flow_alert: dict[str, Any],
    class_returns: dict[str, Any],
) -> list[dict[str, Any]]:
    signals: list[dict[str, Any]] = []
    scores = context.get("scores", {}) if isinstance(context.get("scores"), dict) else {}
    flow_scores = flow_alert.get("scores", {}) if isinstance(flow_alert.get("scores"), dict) else {}
    large_flows = flow_alert.get("large_flows", {}) if isinstance(flow_alert.get("large_flows"), dict) else {}
    poly = flow_alert.get("polymarket", {}) if isinstance(flow_alert.get("polymarket"), dict) else {}

    news_risk = to_float(scores.get("news_risk_score"))
    risk_on = to_float(scores.get("risk_on_score"))
    flow_score = to_float(flow_scores.get("flow_alert_score"))
    inflow_z = to_float(large_flows.get("inflow_zscore_7d"))
    poly_z = to_float(poly.get("volume_24h_zscore_7d"))

    if flow_score >= 35:
        signals.append(signal("flow_attention", flow_score, "Flow alert is elevated; watch crypto and HIP-3 risk assets."))
    if inflow_z >= 2:
        signals.append(signal("large_usdc_inflow_spike", inflow_z, "Large-flow z-score is high; treat as an attention canary, not proof."))
    if poly_z >= 2:
        signals.append(signal("polymarket_volume_spike", poly_z, "Polymarket crypto volume is unusually high."))
    if news_risk >= 70:
        signals.append(signal("news_risk_spike", news_risk, "News risk is high; compare crypto drawdown vs metal/index behavior."))
    if risk_on >= 70:
        signals.append(signal("risk_on_context", risk_on, "Risk-on score is high; shorts need stricter confirmation."))

    one_hour = class_returns.get("1h", {}) if isinstance(class_returns.get("1h"), dict) else {}
    four_hour = class_returns.get("4h", {}) if isinstance(class_returns.get("4h"), dict) else {}
    add_divergence_signals(signals, one_hour, "1h")
    add_divergence_signals(signals, four_hour, "4h")

    if not signals:
        signals.append(signal("baseline", 0, "No elevated canary signal. Continue collecting samples."))
    return sorted(signals, key=lambda item: abs(to_float(item.get("score"))), reverse=True)


def add_divergence_signals(signals: list[dict[str, Any]], class_rows: dict[str, Any], horizon: str) -> None:
    crypto = nested_avg(class_rows, "crypto_major")
    equity = nested_avg(class_rows, "equity")
    index = nested_avg(class_rows, "index")
    metal = nested_avg(class_rows, "metal")
    commodity = nested_avg(class_rows, "commodity")

    if crypto is not None and metal is not None and abs(crypto - metal) >= 1.5:
        signals.append(
            signal(
                f"{horizon}_crypto_metal_divergence",
                crypto - metal,
                "Crypto majors and metals are diverging; useful for risk/hedge regime checks.",
            )
        )
    if crypto is not None and equity is not None and abs(crypto - equity) >= 1.5:
        signals.append(
            signal(
                f"{horizon}_crypto_equity_divergence",
                crypto - equity,
                "Crypto majors and equity perps are diverging; watch lead/lag rotation.",
            )
        )
    if crypto is not None and index is not None and index - crypto >= 1:
        signals.append(
            signal(
                f"{horizon}_index_leads_crypto",
                index - crypto,
                "Index perps are stronger than crypto majors; possible risk-on canary.",
            )
        )
    if crypto is not None and commodity is not None and abs(crypto - commodity) >= 2:
        signals.append(
            signal(
                f"{horizon}_commodity_crypto_divergence",
                crypto - commodity,
                "Commodity perps and crypto are moving differently; check macro-linked stress.",
            )
        )


def compute_correlations(
    records: list[dict[str, Any]],
    class_map: dict[str, str],
    market_history: list[Any],
    flow_history: list[Any],
    sample_min: int,
) -> list[dict[str, Any]]:
    if len(records) < sample_min:
        return []

    market_points = parse_points(market_history)
    flow_points = parse_points(flow_history)
    class_series = build_class_return_series(records, class_map, timedelta(hours=1))
    correlations: list[dict[str, Any]] = []

    for asset_class, points in class_series.items():
        signal_pairs = {
            "news_risk_score": [],
            "risk_on_score": [],
            "market_context_score": [],
            "flow_alert_score": [],
            "large_usdc_inflow": [],
            "polymarket_volume_24h": [],
        }
        for point_time, return_pct in points:
            market = latest_before(market_points, point_time)
            flow = latest_before(flow_points, point_time)
            if market:
                scores = market.get("scores", {}) if isinstance(market.get("scores"), dict) else {}
                append_pair(signal_pairs["news_risk_score"], scores.get("news_risk_score"), return_pct)
                append_pair(signal_pairs["risk_on_score"], scores.get("risk_on_score"), return_pct)
                append_pair(signal_pairs["market_context_score"], scores.get("market_context_score"), return_pct)
            if flow:
                scores = flow.get("scores", {}) if isinstance(flow.get("scores"), dict) else {}
                large = flow.get("large_flows", {}) if isinstance(flow.get("large_flows"), dict) else {}
                poly = flow.get("polymarket", {}) if isinstance(flow.get("polymarket"), dict) else {}
                append_pair(signal_pairs["flow_alert_score"], scores.get("flow_alert_score"), return_pct)
                append_pair(signal_pairs["large_usdc_inflow"], large.get("large_usdc_inflow"), return_pct)
                append_pair(signal_pairs["polymarket_volume_24h"], poly.get("volume_24h"), return_pct)

        for signal_name, pairs in signal_pairs.items():
            xs = [x for x, _ in pairs]
            ys = [y for _, y in pairs]
            if len(xs) < sample_min:
                continue
            corr_value = correlation(xs, ys)
            if corr_value is None:
                continue
            correlations.append(
                {
                    "signal": signal_name,
                    "target": f"{asset_class}_forward_1h_return_pct",
                    "sample_count": len(xs),
                    "correlation": round(corr_value, 4),
                    "strength": classify_correlation(corr_value),
                }
            )

    correlations.sort(key=lambda item: abs(to_float(item.get("correlation"))), reverse=True)
    return correlations


def build_class_return_series(
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
        prices = record.get("prices", {}) if isinstance(record.get("prices"), dict) else {}
        future_prices = future.get("prices", {}) if isinstance(future.get("prices"), dict) else {}
        by_class: dict[str, list[float]] = {}
        for symbol, price in prices.items():
            start = to_float(price)
            end = to_float(future_prices.get(symbol))
            if start <= 0 or end <= 0:
                continue
            asset_class = class_map.get(str(symbol), "unknown")
            by_class.setdefault(asset_class, []).append((end / start - 1) * 100)
        for asset_class, values in by_class.items():
            if values:
                output.setdefault(asset_class, []).append((point_time, sum(values) / len(values)))
    return output


def sample_status(
    records: list[dict[str, Any]],
    market_history: list[Any],
    flow_history: list[Any],
    sample_min: int,
) -> dict[str, Any]:
    return {
        "asset_price_records": len(records),
        "market_context_records": len(market_history) if isinstance(market_history, list) else 0,
        "flow_alert_records": len(flow_history) if isinstance(flow_history, list) else 0,
        "minimum_for_correlation": sample_min,
        "ready_for_correlation": len(records) >= sample_min,
    }


def render_index_report(index: dict[str, Any]) -> str:
    health = index.get("dataset_health", {})
    canary = index.get("canary_summary", {})
    file_rows = "\n".join(
        f"- `{item['path']}` ({item['bytes']} bytes): {item['note']}"
        for item in index.get("files", {}).get("first_read", [])
    )
    class_counts = render_mapping(health.get("asset_class_counts", {}))
    signals = render_signal_lines(canary.get("signals", []))
    asset_archives = health.get("asset_price_archive_files") or []
    polymarket_archives = health.get("polymarket_outcome_archive_files") or []
    asset_archive_line = ", ".join(f"`{path}`" for path in asset_archives) if asset_archives else "`none yet`"
    polymarket_archive_line = (
        ", ".join(f"`{path}`" for path in polymarket_archives) if polymarket_archives else "`none yet`"
    )

    return (
        "# AI Context Index\n\n"
        "Read this first to save AI quota. It tells the analysis which compact files are enough, "
        "and when a full JSON file is justified.\n\n"
        f"- Updated: `{index.get('updated_at')}`\n"
        f"- Asset price active records: `{health.get('asset_price_active_records')}`\n"
        f"- Day/swing records: `{health.get('day_swing_records')}`\n"
        f"- Macro indicators: `{health.get('macro_indicator_count')}`\n"
        f"- Flow-alert history records: `{health.get('flow_alert_history_records')}`\n"
        f"- Correlation status: `{canary.get('status')}`\n"
        f"- Asset price archives: {asset_archive_line}\n"
        f"- Polymarket outcome archives: {polymarket_archive_line}\n\n"
        "## First Read Files\n\n"
        f"{file_rows or '- No files.'}\n\n"
        "## Asset Classes\n\n"
        f"{class_counts}\n\n"
        "## Canary Snapshot\n\n"
        f"{signals}\n\n"
        "## Full JSON Rule\n\n"
        "- Do not load `asset_universe_latest.json` until symbol-level fields are needed.\n"
        "- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.\n"
        "- Do not load `day_swing_dataset.json` until validating one specific strategy rule.\n"
        "- Do not load compressed archives unless the active window is too short for that rule.\n"
    )


def render_canary_report(canary: dict[str, Any]) -> str:
    signals = render_signal_lines(canary.get("signals", []))
    class_returns = render_class_returns(canary.get("class_returns", {}))
    correlations = render_correlations(canary.get("correlations", []))
    sample = canary.get("sample_status", {})
    return (
        "# Latest Canary Signals\n\n"
        "These are early-warning indicators for cross-market relationships. "
        "They are hypotheses to test, not trade signals by themselves.\n\n"
        f"- Updated: `{canary.get('updated_at')}`\n"
        f"- Correlation status: `{canary.get('correlation_status')}`\n"
        f"- Asset price records: `{sample.get('asset_price_records')}`\n"
        f"- Minimum samples for correlation: `{sample.get('minimum_for_correlation')}`\n\n"
        "## Current Signals\n\n"
        f"{signals}\n\n"
        "## Class Returns\n\n"
        f"{class_returns}\n\n"
        "## Correlations\n\n"
        f"{correlations}\n"
    )


def render_signal_lines(signals: list[Any]) -> str:
    if not signals:
        return "- No signals."
    rows = []
    for item in signals:
        if not isinstance(item, dict):
            continue
        rows.append(f"- {item.get('name')}: score `{item.get('score')}` - {item.get('message')}")
    return "\n".join(rows) if rows else "- No signals."


def render_class_returns(class_returns: dict[str, Any]) -> str:
    if not isinstance(class_returns, dict) or not class_returns:
        return "- Not enough price history yet."
    lines = []
    for horizon in ("15m", "1h", "4h", "24h"):
        rows = class_returns.get(horizon)
        if not isinstance(rows, dict) or not rows:
            continue
        parts = []
        for asset_class, summary in sorted(rows.items()):
            if isinstance(summary, dict):
                parts.append(f"{asset_class} avg `{summary.get('avg_return_pct')}` n `{summary.get('count')}`")
        if parts:
            lines.append(f"- {horizon}: " + "; ".join(parts))
    return "\n".join(lines) if lines else "- Not enough price history yet."


def render_correlations(correlations: list[Any]) -> str:
    if not correlations:
        return "- Insufficient samples. Keep collecting before drawing correlation conclusions."
    return "\n".join(
        f"- {item.get('signal')} -> {item.get('target')}: "
        f"corr `{item.get('correlation')}`, n `{item.get('sample_count')}`, {item.get('strength')}"
        for item in correlations
        if isinstance(item, dict)
    )


def render_mapping(value: Any) -> str:
    if not isinstance(value, dict) or not value:
        return "- No counts."
    return "\n".join(f"- {key}: `{count}`" for key, count in sorted(value.items()))


def parse_points(rows: list[Any]) -> list[dict[str, Any]]:
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


def find_record_at_or_after(records: list[dict[str, Any]], target: datetime) -> dict[str, Any] | None:
    for record in records:
        observed_at = parse_time(record.get("observed_at"))
        if observed_at is not None and observed_at >= target:
            return record
    return None


def return_summary(values: list[float]) -> dict[str, Any]:
    clean = [value for value in values if value is not None]
    if not clean:
        return {"count": 0, "avg_return_pct": None, "median_return_pct": None, "up_pct": None}
    return {
        "count": len(clean),
        "avg_return_pct": round(sum(clean) / len(clean), 4),
        "median_return_pct": round(median(clean), 4),
        "up_pct": round(sum(1 for value in clean if value > 0) / len(clean) * 100, 2),
    }


def signal(name: str, score: float, message: str) -> dict[str, Any]:
    return {"name": name, "score": round(score, 4), "message": message}


def nested_avg(class_rows: dict[str, Any], asset_class: str) -> float | None:
    row = class_rows.get(asset_class) if isinstance(class_rows, dict) else None
    if not isinstance(row, dict):
        return None
    value = row.get("avg_return_pct")
    if value is None:
        return None
    return to_float(value)


def append_pair(pairs: list[tuple[float, float]], x: Any, y: Any) -> None:
    x_value = to_float_or_none(x)
    y_value = to_float_or_none(y)
    if x_value is not None and y_value is not None:
        pairs.append((x_value, y_value))


def correlation(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) != len(ys) or len(xs) < 2:
        return None
    avg_x = sum(xs) / len(xs)
    avg_y = sum(ys) / len(ys)
    dx = [x - avg_x for x in xs]
    dy = [y - avg_y for y in ys]
    denom_x = math.sqrt(sum(value * value for value in dx))
    denom_y = math.sqrt(sum(value * value for value in dy))
    if denom_x == 0 or denom_y == 0:
        return None
    return sum(a * b for a, b in zip(dx, dy)) / (denom_x * denom_y)


def classify_correlation(value: float) -> str:
    magnitude = abs(value)
    if magnitude >= 0.5:
        return "strong_sample_signal"
    if magnitude >= 0.25:
        return "moderate_sample_signal"
    return "weak_sample_signal"


def median(values: list[float]) -> float:
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


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
        return float(value) if value is not None else None
    except (TypeError, ValueError):
        return None
