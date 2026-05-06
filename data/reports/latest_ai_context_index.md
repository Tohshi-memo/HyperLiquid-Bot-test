# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-05-06T15:07:25.938669+00:00`
- Asset price active records: `464`
- Day/swing records: `477`
- Flow-alert history records: `1565`
- Correlation status: `ready`
- Asset price archives: `none yet`

## First Read Files

- `data/reports/latest_ai_context_index.md` (1989 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (35707 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2622 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (861 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/processed/ai_analysis_pack.json` (45668 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (5638 bytes): Asset-class overview.
- `data/reports/latest_asset_features.md` (2135 bytes): Individual asset screen.
- `data/reports/latest_hip4_outcome.md` (1211 bytes): HIP-4 outcome market overview.
- `data/reports/latest_relationship_scan.md` (3645 bytes): Mechanical relationship candidates.

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

- polymarket_volume_spike: score `10.17` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-3.0484` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.2227` - Index perps are stronger than crypto majors; possible risk-on canary.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
