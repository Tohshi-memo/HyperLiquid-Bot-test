# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-05-02T18:32:53.862180+00:00`
- Asset price active records: `97`
- Day/swing records: `110`
- Flow-alert history records: `417`
- Correlation status: `ready`
- Asset price archives: `none yet`

## First Read Files

- `data/reports/latest_ai_context_index.md` (1474 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (13364 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2392 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (849 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/processed/ai_analysis_pack.json` (30164 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (4765 bytes): Asset-class overview.

## Asset Classes

- commodity: `7`
- crypto_alt: `223`
- crypto_major: `7`
- equity: `42`
- fx: `4`
- index: `9`
- metal: `7`
- unknown: `313`

## Canary Snapshot

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
