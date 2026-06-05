# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-06-05T06:37:24.593765+00:00`
- Asset price active records: `672`
- Day/swing records: `2653`
- Macro indicators: `11`
- Flow-alert history records: `8640`
- Correlation status: `ready`
- Asset price archives: `data/archive/asset_price_history_2026-05.jsonl.gz`
- Polymarket outcome archives: `data/archive/polymarket_outcome_history_2026-05.jsonl.gz`, `data/archive/polymarket_outcome_history_2026-06.jsonl.gz`

## First Read Files

- `data/reports/latest_ai_context_index.md` (3157 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (68071 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (3287 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (869 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/reports/latest_macro_indicators.md` (2537 bytes): Macro rates, employment, inflation, dollar, and risk overview.
- `data/processed/ai_analysis_pack.json` (47169 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (5752 bytes): Asset-class overview.
- `data/reports/latest_asset_features.md` (2333 bytes): Individual asset screen.
- `data/reports/latest_hip4_outcome.md` (9109 bytes): HIP-4 outcome market overview.
- `data/reports/latest_relationship_scan.md` (3629 bytes): Mechanical relationship candidates.
- `data/reports/latest_sector_reactions.md` (4616 bytes): Delayed sector reaction overview.

## Asset Classes

- commodity: `12`
- crypto_alt: `228`
- crypto_major: `8`
- equity: `74`
- fx: `6`
- index: `23`
- metal: `18`
- unknown: `424`

## Canary Snapshot

- 4h_crypto_metal_divergence: score `-3.6684` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.5786` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.5545` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.8596` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `-2.6604` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.6069` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.4908` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `-1.8815` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Use `asset_features_all.json` for full-universe screening before loading raw price history.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
