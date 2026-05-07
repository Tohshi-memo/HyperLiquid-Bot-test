# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-05-07T15:22:23.494072+00:00`
- Asset price active records: `561`
- Day/swing records: `574`
- Flow-alert history records: `1866`
- Correlation status: `ready`
- Asset price archives: `none yet`

## First Read Files

- `data/reports/latest_ai_context_index.md` (1740 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (36516 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2527 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (863 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/processed/ai_analysis_pack.json` (45747 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (5679 bytes): Asset-class overview.
- `data/reports/latest_asset_features.md` (2221 bytes): Individual asset screen.
- `data/reports/latest_hip4_outcome.md` (4092 bytes): HIP-4 outcome market overview.
- `data/reports/latest_relationship_scan.md` (3649 bytes): Mechanical relationship candidates.

## Asset Classes

- commodity: `12`
- crypto_alt: `228`
- crypto_major: `8`
- equity: `65`
- fx: `5`
- index: `23`
- metal: `18`
- unknown: `365`

## Canary Snapshot

- 4h_crypto_metal_divergence: score `-1.67` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.1223` - Index perps are stronger than crypto majors; possible risk-on canary.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
