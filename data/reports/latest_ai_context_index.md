# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-05-21T16:22:21.626766+00:00`
- Asset price active records: `672`
- Day/swing records: `1279`
- Macro indicators: `11`
- Flow-alert history records: `6057`
- Correlation status: `ready`
- Asset price archives: `data/archive/asset_price_history_2026-05.jsonl.gz`
- Polymarket outcome archives: `data/archive/polymarket_outcome_history_2026-05.jsonl.gz`

## First Read Files

- `data/reports/latest_ai_context_index.md` (2210 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (73607 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2368 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (866 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/reports/latest_macro_indicators.md` (2539 bytes): Macro rates, employment, inflation, dollar, and risk overview.
- `data/processed/ai_analysis_pack.json` (46929 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (5770 bytes): Asset-class overview.
- `data/reports/latest_asset_features.md` (2290 bytes): Individual asset screen.
- `data/reports/latest_hip4_outcome.md` (4034 bytes): HIP-4 outcome market overview.
- `data/reports/latest_relationship_scan.md` (3638 bytes): Mechanical relationship candidates.
- `data/reports/latest_sector_reactions.md` (4616 bytes): Delayed sector reaction overview.

## Asset Classes

- commodity: `12`
- crypto_alt: `228`
- crypto_major: `8`
- equity: `67`
- fx: `6`
- index: `23`
- metal: `18`
- unknown: `385`

## Canary Snapshot

- polymarket_volume_spike: score `3.99` - Polymarket crypto volume is unusually high.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Use `asset_features_all.json` for full-universe screening before loading raw price history.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
