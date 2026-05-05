# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-05-05T17:15:19.823956+00:00`
- Asset price active records: `377`
- Day/swing records: `390`
- Flow-alert history records: `1294`
- Correlation status: `ready`
- Asset price archives: `none yet`

## First Read Files

- `data/reports/latest_ai_context_index.md` (1560 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (14654 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2411 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (857 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/processed/ai_analysis_pack.json` (43951 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (4668 bytes): Asset-class overview.
- `data/reports/latest_hip4_outcome.md` (783 bytes): HIP-4 outcome market overview.

## Asset Classes

- commodity: `7`
- crypto_alt: `223`
- crypto_major: `7`
- equity: `47`
- fx: `4`
- index: `6`
- metal: `7`
- unknown: `313`

## Canary Snapshot

- 4h_index_leads_crypto: score `1.0452` - Index perps are stronger than crypto majors; possible risk-on canary.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
