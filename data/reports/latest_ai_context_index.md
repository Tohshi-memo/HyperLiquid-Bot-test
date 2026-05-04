# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-05-04T03:30:32.645734+00:00`
- Asset price active records: `229`
- Day/swing records: `242`
- Flow-alert history records: `831`
- Correlation status: `ready`
- Asset price archives: `none yet`

## First Read Files

- `data/reports/latest_ai_context_index.md` (1603 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (14686 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2426 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (847 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/processed/ai_analysis_pack.json` (35510 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (4771 bytes): Asset-class overview.
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

- 4h_crypto_metal_divergence: score `2.0037` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
