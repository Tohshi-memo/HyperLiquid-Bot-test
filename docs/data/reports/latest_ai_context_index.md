# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-07-12T00:09:42.910726+00:00`
- Asset price active records: `672`
- Day/swing records: `5845`
- Macro indicators: `11`
- Flow-alert history records: `8640`
- Correlation status: `ready`
- Asset price archives: `data/archive/asset_price_history_2026-05.jsonl.gz`, `data/archive/asset_price_history_2026-06.jsonl.gz`
- Polymarket outcome archives: `data/archive/polymarket_outcome_history_2026-05.jsonl.gz`, `data/archive/polymarket_outcome_history_2026-06.jsonl.gz`

## First Read Files

- `data/reports/latest_ai_context_index.md` (2855 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (64311 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2871 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (872 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/reports/latest_macro_indicators.md` (2535 bytes): Macro rates, employment, inflation, dollar, and risk overview.
- `data/processed/ai_analysis_pack.json` (48235 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (5607 bytes): Asset-class overview.
- `data/reports/latest_asset_features.md` (2194 bytes): Individual asset screen.
- `data/reports/latest_hip4_outcome.md` (8877 bytes): HIP-4 outcome market overview.
- `data/reports/latest_relationship_scan.md` (3562 bytes): Mechanical relationship candidates.
- `data/reports/latest_sector_reactions.md` (4593 bytes): Delayed sector reaction overview.

## Asset Classes

- commodity: `12`
- crypto_alt: `230`
- crypto_major: `8`
- equity: `92`
- fx: `6`
- index: `25`
- metal: `20`
- unknown: `765`

## Canary Snapshot

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.2674` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.7237` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6503` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.3724` - Index perps are stronger than crypto majors; possible risk-on canary.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Use `asset_features_all.json` for full-universe screening before loading raw price history.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
