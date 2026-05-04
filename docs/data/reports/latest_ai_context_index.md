# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-05-04T13:45:27.722931+00:00`
- Asset price active records: `270`
- Day/swing records: `283`
- Flow-alert history records: `959`
- Correlation status: `ready`
- Asset price archives: `none yet`

## First Read Files

- `data/reports/latest_ai_context_index.md` (1559 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (14635 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2391 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (858 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/processed/ai_analysis_pack.json` (42579 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (4797 bytes): Asset-class overview.
- `data/reports/latest_hip4_outcome.md` (783 bytes): HIP-4 outcome market overview.

## Asset Classes

- commodity: `7`
- crypto_alt: `223`
- crypto_major: `7`
- equity: `42`
- fx: `4`
- index: `9`
- metal: `7`
- unknown: `314`

## Canary Snapshot

- 4h_index_leads_crypto: score `1.643` - Index perps are stronger than crypto majors; possible risk-on canary.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
