# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-07-08T05:07:26.313853+00:00`
- Asset price active records: `672`
- Day/swing records: `5499`
- Macro indicators: `11`
- Flow-alert history records: `8640`
- Correlation status: `ready`
- Asset price archives: `data/archive/asset_price_history_2026-05.jsonl.gz`, `data/archive/asset_price_history_2026-06.jsonl.gz`, `data/archive/asset_price_history_2026-07.jsonl.gz`
- Polymarket outcome archives: `data/archive/polymarket_outcome_history_2026-05.jsonl.gz`, `data/archive/polymarket_outcome_history_2026-06.jsonl.gz`

## First Read Files

- `data/reports/latest_ai_context_index.md` (2527 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (64030 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2512 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (870 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/reports/latest_macro_indicators.md` (2535 bytes): Macro rates, employment, inflation, dollar, and risk overview.
- `data/processed/ai_analysis_pack.json` (48211 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (5699 bytes): Asset-class overview.
- `data/reports/latest_asset_features.md` (2172 bytes): Individual asset screen.
- `data/reports/latest_hip4_outcome.md` (8867 bytes): HIP-4 outcome market overview.
- `data/reports/latest_relationship_scan.md` (3560 bytes): Mechanical relationship candidates.
- `data/reports/latest_sector_reactions.md` (4593 bytes): Delayed sector reaction overview.

## Asset Classes

- commodity: `12`
- crypto_alt: `229`
- crypto_major: `8`
- equity: `91`
- fx: `6`
- index: `25`
- metal: `20`
- unknown: `763`

## Canary Snapshot

- 4h_crypto_metal_divergence: score `-1.665` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.0342` - Index perps are stronger than crypto majors; possible risk-on canary.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Use `asset_features_all.json` for full-universe screening before loading raw price history.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
