# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-11-23T17:37:42.910311+00:00`
- Asset price active records: `672`
- Day/swing records: `12000`
- Macro indicators: `11`
- Flow-alert history records: `8640`
- Correlation status: `ready`
- Asset price archives: `data/archive/asset_price_history_2026-05.jsonl.gz`, `data/archive/asset_price_history_2026-06.jsonl.gz`, `data/archive/asset_price_history_2026-11.jsonl.gz`
- Polymarket outcome archives: `data/archive/polymarket_outcome_history_2026-05.jsonl.gz`, `data/archive/polymarket_outcome_history_2026-06.jsonl.gz`

## First Read Files

- `data/reports/latest_ai_context_index.md` (2667 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (62413 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2557 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (875 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/reports/latest_macro_indicators.md` (2100 bytes): Macro rates, employment, inflation, dollar, and risk overview.
- `data/processed/ai_analysis_pack.json` (50536 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (5716 bytes): Asset-class overview.
- `data/reports/latest_asset_features.md` (2207 bytes): Individual asset screen.
- `data/reports/latest_hip4_outcome.md` (10585 bytes): HIP-4 outcome market overview.
- `data/reports/latest_relationship_scan.md` (3531 bytes): Mechanical relationship candidates.
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

- 4h_crypto_equity_divergence: score `-2.8976` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.1913` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Use `asset_features_all.json` for full-universe screening before loading raw price history.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
