from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
SOURCE_FILES = [
    ("data/processed/ai_context_index.json", "docs/data/processed/ai_context_index.json"),
    ("data/processed/canary_signals.json", "docs/data/processed/canary_signals.json"),
    ("data/processed/ai_analysis_pack.json", "docs/data/processed/ai_analysis_pack.json"),
    ("data/processed/market_context.json", "docs/data/processed/market_context.json"),
    ("data/processed/polymarket_outcome_latest.json", "docs/data/processed/polymarket_outcome_latest.json"),
    ("data/processed/flow_alert.json", "docs/data/processed/flow_alert.json"),
    ("data/processed/macro_indicators_latest.json", "docs/data/processed/macro_indicators_latest.json"),
    ("data/processed/asset_features_latest.json", "docs/data/processed/asset_features_latest.json"),
    ("data/processed/hip4_outcome_latest.json", "docs/data/processed/hip4_outcome_latest.json"),
    ("data/processed/relationship_scan_latest.json", "docs/data/processed/relationship_scan_latest.json"),
    ("data/processed/sector_reactions_latest.json", "docs/data/processed/sector_reactions_latest.json"),
    ("data/processed/sector_price_history.json", "docs/data/processed/sector_price_history.json"),
    ("data/reports/latest_hip4_outcome.md", "docs/data/reports/latest_hip4_outcome.md"),
    ("data/reports/latest_relationship_scan.md", "docs/data/reports/latest_relationship_scan.md"),
    ("data/reports/latest_sector_reactions.md", "docs/data/reports/latest_sector_reactions.md"),
    ("data/reports/latest_ai_context_index.md", "docs/data/reports/latest_ai_context_index.md"),
    ("data/reports/latest_canary_signals.md", "docs/data/reports/latest_canary_signals.md"),
    ("data/reports/latest_ai_analysis_brief.md", "docs/data/reports/latest_ai_analysis_brief.md"),
    ("data/reports/latest_macro_indicators.md", "docs/data/reports/latest_macro_indicators.md"),
    ("data/reports/latest_asset_features.md", "docs/data/reports/latest_asset_features.md"),
    ("data/reports/latest_asset_universe.md", "docs/data/reports/latest_asset_universe.md"),
    ("data/reports/latest_context.md", "docs/data/reports/latest_context.md"),
    ("data/reports/latest_flow_alert.md", "docs/data/reports/latest_flow_alert.md"),
]


def main() -> None:
    copied = []
    for source_name, target_name in SOURCE_FILES:
        source = ROOT / source_name
        target = ROOT / target_name
        if not source.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        copied.append({"source": source_name, "target": target_name})

    manifest = {
        "copied_files": copied,
    }
    manifest_path = DOCS_DIR / "data" / "manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
