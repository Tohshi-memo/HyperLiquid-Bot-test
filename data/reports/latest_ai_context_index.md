# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-06-04T02:22:21.056660+00:00`
- Asset price active records: `672`
- Day/swing records: `2540`
- Macro indicators: `11`
- Flow-alert history records: `8640`
- Correlation status: `ready`
- Asset price archives: `data/archive/asset_price_history_2026-05.jsonl.gz`
- Polymarket outcome archives: `data/archive/polymarket_outcome_history_2026-05.jsonl.gz`, `data/archive/polymarket_outcome_history_2026-06.jsonl.gz`

## First Read Files

- `data/reports/latest_ai_context_index.md` (3158 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (65768 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2808 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (868 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/reports/latest_macro_indicators.md` (2536 bytes): Macro rates, employment, inflation, dollar, and risk overview.
- `data/processed/ai_analysis_pack.json` (47085 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (5755 bytes): Asset-class overview.
- `data/reports/latest_asset_features.md` (2321 bytes): Individual asset screen.
- `data/reports/latest_hip4_outcome.md` (9463 bytes): HIP-4 outcome market overview.
- `data/reports/latest_relationship_scan.md` (3632 bytes): Mechanical relationship candidates.
- `data/reports/latest_sector_reactions.md` (4616 bytes): Delayed sector reaction overview.

## Asset Classes

- commodity: `12`
- crypto_alt: `228`
- crypto_major: `8`
- equity: `73`
- fx: `6`
- index: `23`
- metal: `18`
- unknown: `420`

## Canary Snapshot

- 4h_crypto_metal_divergence: score `-3.6838` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.9352` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.6482` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.4062` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Use `asset_features_all.json` for full-universe screening before loading raw price history.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
