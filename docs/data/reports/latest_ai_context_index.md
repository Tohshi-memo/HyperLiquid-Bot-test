# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-05-08T10:22:14.916788+00:00`
- Asset price active records: `637`
- Day/swing records: `650`
- Macro indicators: `11`
- Flow-alert history records: `2103`
- Correlation status: `ready`
- Asset price archives: `none yet`

## First Read Files

- `data/reports/latest_ai_context_index.md` (1886 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (52891 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2373 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (863 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/reports/latest_macro_indicators.md` (1600 bytes): Macro rates, employment, inflation, dollar, and risk overview.
- `data/processed/ai_analysis_pack.json` (45763 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (5702 bytes): Asset-class overview.
- `data/reports/latest_asset_features.md` (2233 bytes): Individual asset screen.
- `data/reports/latest_hip4_outcome.md` (4131 bytes): HIP-4 outcome market overview.
- `data/reports/latest_relationship_scan.md` (3644 bytes): Mechanical relationship candidates.

## Asset Classes

- commodity: `12`
- crypto_alt: `228`
- crypto_major: `8`
- equity: `65`
- fx: `5`
- index: `23`
- metal: `18`
- unknown: `375`

## Canary Snapshot

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
