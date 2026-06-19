from __future__ import annotations

import json
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
SOURCE_FILES = [
    ({"context"}, "data/processed/ai_context_index.json", "docs/data/processed/ai_context_index.json"),
    ({"context"}, "data/processed/canary_signals.json", "docs/data/processed/canary_signals.json"),
    ({"context"}, "data/processed/ai_analysis_pack.json", "docs/data/processed/ai_analysis_pack.json"),
    ({"context"}, "data/processed/market_context.json", "docs/data/processed/market_context.json"),
    ({"context"}, "data/processed/polymarket_outcome_latest.json", "docs/data/processed/polymarket_outcome_latest.json"),
    ({"flow_alert"}, "data/processed/flow_alert.json", "docs/data/processed/flow_alert.json"),
    ({"macro"}, "data/processed/macro_indicators_latest.json", "docs/data/processed/macro_indicators_latest.json"),
    ({"context"}, "data/processed/asset_features_latest.json", "docs/data/processed/asset_features_latest.json"),
    ({"context"}, "data/processed/asset_features_all.json", "docs/data/processed/asset_features_all.json"),
    ({"context"}, "data/processed/hip4_outcome_latest.json", "docs/data/processed/hip4_outcome_latest.json"),
    ({"context"}, "data/processed/relationship_scan_latest.json", "docs/data/processed/relationship_scan_latest.json"),
    ({"context"}, "data/processed/sector_reactions_latest.json", "docs/data/processed/sector_reactions_latest.json"),
    ({"context"}, "data/processed/sector_price_history.json", "docs/data/processed/sector_price_history.json"),
    ({"context"}, "data/reports/latest_hip4_outcome.md", "docs/data/reports/latest_hip4_outcome.md"),
    ({"context"}, "data/reports/latest_relationship_scan.md", "docs/data/reports/latest_relationship_scan.md"),
    ({"context"}, "data/reports/latest_sector_reactions.md", "docs/data/reports/latest_sector_reactions.md"),
    ({"context"}, "data/reports/latest_ai_context_index.md", "docs/data/reports/latest_ai_context_index.md"),
    ({"context"}, "data/reports/latest_canary_signals.md", "docs/data/reports/latest_canary_signals.md"),
    ({"context"}, "data/reports/latest_ai_analysis_brief.md", "docs/data/reports/latest_ai_analysis_brief.md"),
    ({"macro"}, "data/reports/latest_macro_indicators.md", "docs/data/reports/latest_macro_indicators.md"),
    ({"context"}, "data/reports/latest_asset_features.md", "docs/data/reports/latest_asset_features.md"),
    ({"context"}, "data/reports/latest_asset_universe.md", "docs/data/reports/latest_asset_universe.md"),
    ({"context"}, "data/reports/latest_day_swing.md", "docs/data/reports/latest_day_swing.md"),
    ({"context"}, "data/reports/latest_context.md", "docs/data/reports/latest_context.md"),
    ({"flow_alert"}, "data/reports/latest_flow_alert.md", "docs/data/reports/latest_flow_alert.md"),
]


def main() -> None:
    profile = selected_profile()
    for groups, source_name, target_name in SOURCE_FILES:
        if profile != "all" and profile not in groups:
            continue
        source = ROOT / source_name
        target = ROOT / target_name
        if not source.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)

    if os.getenv("REPORT_SITE_WRITE_MANIFEST", "false").lower() == "true":
        manifest = {
            "source_files": [
                {
                    "groups": sorted(groups),
                    "source": source_name,
                    "target": target_name,
                }
                for groups, source_name, target_name in SOURCE_FILES
            ],
        }
        manifest_path = DOCS_DIR / "data" / "manifest.json"
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def selected_profile() -> str:
    value = os.getenv("REPORT_SITE_PROFILE") or os.getenv("COLLECTOR_PROFILE") or "all"
    value = value.strip().lower().replace("-", "_")
    if value in {"flow", "flow_alert", "flow_alerts", "alert", "alerts"}:
        return "flow_alert"
    if value in {"macro", "macro_indicators"}:
        return "macro"
    if value in {"context", "public_context"}:
        return "context"
    return "all"


if __name__ == "__main__":
    main()
