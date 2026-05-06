# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-05-06T13:37:27.419077+00:00`
- Asset price active records: `458`
- Day/swing records: `471`
- Flow-alert history records: `1547`
- Correlation status: `ready`
- Asset price archives: `none yet`

## First Read Files

- `data/reports/latest_ai_context_index.md` (1564 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (14975 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2499 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (858 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/processed/ai_analysis_pack.json` (45639 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (5641 bytes): Asset-class overview.
- `data/reports/latest_hip4_outcome.md` (1217 bytes): HIP-4 outcome market overview.
- `data/reports/latest_relationship_scan.md` (3613 bytes): Mechanical relationship candidates.

## Asset Classes

- commodity: `12`
- crypto_alt: `228`
- crypto_major: `8`
- equity: `65`
- fx: `4`
- index: `23`
- metal: `18`
- unknown: `356`

## Canary Snapshot

- polymarket_volume_spike: score `24.29` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.0455` - Index perps are stronger than crypto majors; possible risk-on canary.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
