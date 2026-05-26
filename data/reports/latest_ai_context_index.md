# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-05-26T18:07:21.213358+00:00`
- Asset price active records: `672`
- Day/swing records: `1749`
- Macro indicators: `11`
- Flow-alert history records: `7542`
- Correlation status: `ready`
- Asset price archives: `data/archive/asset_price_history_2026-05.jsonl.gz`
- Polymarket outcome archives: `data/archive/polymarket_outcome_history_2026-05.jsonl.gz`

## First Read Files

- `data/reports/latest_ai_context_index.md` (2355 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (74091 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2541 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (863 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/reports/latest_macro_indicators.md` (2539 bytes): Macro rates, employment, inflation, dollar, and risk overview.
- `data/processed/ai_analysis_pack.json` (46970 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (5725 bytes): Asset-class overview.
- `data/reports/latest_asset_features.md` (2252 bytes): Individual asset screen.
- `data/reports/latest_hip4_outcome.md` (8326 bytes): HIP-4 outcome market overview.
- `data/reports/latest_relationship_scan.md` (3624 bytes): Mechanical relationship candidates.
- `data/reports/latest_sector_reactions.md` (4616 bytes): Delayed sector reaction overview.

## Asset Classes

- commodity: `12`
- crypto_alt: `228`
- crypto_major: `8`
- equity: `67`
- fx: `6`
- index: `23`
- metal: `18`
- unknown: `418`

## Canary Snapshot

- 4h_index_leads_crypto: score `1.8973` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.8614` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Use `asset_features_all.json` for full-universe screening before loading raw price history.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
