# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-11-23T15:52:31.651546+00:00`
- Asset price active records: `672`
- Day/swing records: `12000`
- Macro indicators: `11`
- Flow-alert history records: `8640`
- Correlation status: `ready`
- Asset price archives: `data/archive/asset_price_history_2026-05.jsonl.gz`, `data/archive/asset_price_history_2026-06.jsonl.gz`, `data/archive/asset_price_history_2026-11.jsonl.gz`
- Polymarket outcome archives: `data/archive/polymarket_outcome_history_2026-05.jsonl.gz`, `data/archive/polymarket_outcome_history_2026-06.jsonl.gz`

## First Read Files

- `data/reports/latest_ai_context_index.md` (2984 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (62961 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2765 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (874 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/reports/latest_macro_indicators.md` (2100 bytes): Macro rates, employment, inflation, dollar, and risk overview.
- `data/processed/ai_analysis_pack.json` (50517 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (5721 bytes): Asset-class overview.
- `data/reports/latest_asset_features.md` (2205 bytes): Individual asset screen.
- `data/reports/latest_hip4_outcome.md` (10590 bytes): HIP-4 outcome market overview.
- `data/reports/latest_relationship_scan.md` (3529 bytes): Mechanical relationship candidates.
- `data/reports/latest_sector_reactions.md` (4593 bytes): Delayed sector reaction overview.

## Asset Classes

- commodity: `13`
- crypto_alt: `239`
- crypto_major: `8`
- equity: `166`
- fx: `6`
- index: `27`
- metal: `20`
- unknown: `1286`

## Canary Snapshot

- 4h_commodity_crypto_divergence: score `3.9683` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.729` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- polymarket_volume_spike: score `2.32` - Polymarket crypto volume is unusually high.
- 1h_crypto_equity_divergence: score `-1.772` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Use `asset_features_all.json` for full-universe screening before loading raw price history.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
