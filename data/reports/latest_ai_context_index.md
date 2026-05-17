# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-05-17T09:52:14.813807+00:00`
- Asset price active records: `672`
- Day/swing records: `871`
- Macro indicators: `11`
- Flow-alert history records: `4787`
- Correlation status: `ready`
- Asset price archives: `data/archive/asset_price_history_2026-05.jsonl.gz`
- Polymarket outcome archives: `data/archive/polymarket_outcome_history_2026-05.jsonl.gz`

## First Read Files

- `data/reports/latest_ai_context_index.md` (2377 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (70808 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2560 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (861 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/reports/latest_macro_indicators.md` (2539 bytes): Macro rates, employment, inflation, dollar, and risk overview.
- `data/processed/ai_analysis_pack.json` (46047 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (5652 bytes): Asset-class overview.
- `data/reports/latest_asset_features.md` (2413 bytes): Individual asset screen.
- `data/reports/latest_hip4_outcome.md` (4034 bytes): HIP-4 outcome market overview.
- `data/reports/latest_relationship_scan.md` (3651 bytes): Mechanical relationship candidates.
- `data/reports/latest_sector_reactions.md` (4616 bytes): Delayed sector reaction overview.

## Asset Classes

- commodity: `12`
- crypto_alt: `228`
- crypto_major: `8`
- equity: `65`
- fx: `5`
- index: `23`
- metal: `18`
- unknown: `383`

## Canary Snapshot

- 4h_commodity_crypto_divergence: score `-4.2591` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.3488` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Use `asset_features_all.json` for full-universe screening before loading raw price history.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
