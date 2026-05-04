# AI Context Index

Read this first to save AI quota. It tells the analysis which compact files are enough, and when a full JSON file is justified.

- Updated: `2026-05-04T10:15:20.359223+00:00`
- Asset price active records: `256`
- Day/swing records: `269`
- Flow-alert history records: `915`
- Correlation status: `ready`
- Asset price archives: `none yet`

## First Read Files

- `data/reports/latest_ai_context_index.md` (1559 bytes): Human-readable map.
- `data/processed/ai_context_index.json` (14644 bytes): Machine-readable map.
- `data/reports/latest_canary_signals.md` (2555 bytes): Current canary signals.
- `data/reports/latest_ai_analysis_brief.md` (854 bytes): BTC/ETH/HYPE/SOL compact stats.
- `data/processed/ai_analysis_pack.json` (42267 bytes): Compact strategy stats.
- `data/reports/latest_asset_universe.md` (4780 bytes): Asset-class overview.
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

- 4h_commodity_crypto_divergence: score `-3.3899` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `-2.6298` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Full JSON Rule

- Do not load `asset_universe_latest.json` until symbol-level fields are needed.
- Do not load `asset_price_history.json` until checking cross-asset lead/lag or correlation.
- Do not load `day_swing_dataset.json` until validating one specific strategy rule.
- Do not load compressed archives unless the active window is too short for that rule.
