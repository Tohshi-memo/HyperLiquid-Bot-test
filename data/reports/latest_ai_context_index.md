# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-07-06T05:22:25.243274+00:00`
- Asset price active records: `672`
- Day/swing records: `5309`
- Macro indicators: `6`
- Flow-alert history records: `8640`
- Correlation status: `ready`
- Asset price archives: `data/archive/asset_price_history_2026-05.jsonl.gz`, `data/archive/asset_price_history_2026-06.jsonl.gz`
- Polymarket outcome archives: `data/archive/polymarket_outcome_history_2026-05.jsonl.gz`, `data/archive/polymarket_outcome_history_2026-06.jsonl.gz`

## First Read Files

- `data/reports/latest_ai_context_index.md` (2348 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (60715 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2398 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (871 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/reports/latest_macro_indicators.md` (1852 bytes): Macro rates, employment, inflation, dollar, and risk overview.
- `data/processed/ai_analysis_pack.json` (48198 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (5697 bytes): Asset-class overview.
- `data/reports/latest_asset_features.md` (2194 bytes): Individual asset screen.
- `data/reports/latest_hip4_outcome.md` (8794 bytes): HIP-4 outcome market overview.
- `data/reports/latest_relationship_scan.md` (3591 bytes): Mechanical relationship candidates.
- `data/reports/latest_sector_reactions.md` (4593 bytes): Delayed sector reaction overview.

## Asset Classes

- commodity: `12`
- crypto_alt: `229`
- crypto_major: `8`
- equity: `88`
- fx: `6`
- index: `25`
- metal: `20`
- unknown: `765`

## Canary Snapshot

- 4h_index_leads_crypto: score `1.0392` - Index perps are stronger than crypto majors; possible risk-on canary.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Use `asset_features_all.json` for full-universe screening before loading raw price history.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
