# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T01:52:23.634829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0337` n `13`; crypto_alt avg `0.5821` n `239`; crypto_major avg `0.6153` n `8`; equity avg `0.6952` n `158`; fx avg `-0.0261` n `6`; index avg `0.0638` n `27`; metal avg `0.0847` n `20`; unknown avg `1.9167` n `1260`
- 1h: commodity avg `-0.0967` n `13`; crypto_alt avg `0.4194` n `239`; crypto_major avg `0.1948` n `8`; equity avg `0.8528` n `158`; fx avg `0.0023` n `6`; index avg `0.1303` n `27`; metal avg `0.1437` n `20`; unknown avg `0.9686` n `1248`
- 4h: commodity avg `-0.0023` n `13`; crypto_alt avg `0.7236` n `239`; crypto_major avg `-0.373` n `8`; equity avg `0.7605` n `158`; fx avg `-0.0308` n `6`; index avg `0.1567` n `27`; metal avg `0.5422` n `20`; unknown avg `13.909` n `1204`
- 24h: commodity avg `-0.1402` n `13`; crypto_alt avg `-1.4545` n `239`; crypto_major avg `-1.8758` n `8`; equity avg `0.3994` n `158`; fx avg `-0.0397` n `6`; index avg `0.061` n `27`; metal avg `0.4984` n `20`; unknown avg `1.1349` n `994`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
