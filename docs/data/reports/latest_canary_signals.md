# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T22:22:27.768222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `13`; crypto_alt avg `-0.2036` n `239`; crypto_major avg `-0.0974` n `8`; equity avg `-0.0614` n `158`; fx avg `0.0049` n `6`; index avg `0.0016` n `27`; metal avg `0.013` n `20`; unknown avg `0.8658` n `1261`
- 1h: commodity avg `0.0582` n `13`; crypto_alt avg `-0.3792` n `239`; crypto_major avg `0.0814` n `8`; equity avg `0.0662` n `158`; fx avg `-0.0026` n `6`; index avg `0.0005` n `27`; metal avg `0.0442` n `20`; unknown avg `-0.2397` n `1221`
- 4h: commodity avg `0.1629` n `13`; crypto_alt avg `-0.279` n `239`; crypto_major avg `0.0923` n `8`; equity avg `0.9693` n `158`; fx avg `0.0235` n `6`; index avg `0.0535` n `27`; metal avg `0.0583` n `20`; unknown avg `0.04` n `1181`
- 24h: commodity avg `0.0094` n `13`; crypto_alt avg `1.7143` n `239`; crypto_major avg `-0.0462` n `8`; equity avg `3.0219` n `158`; fx avg `-0.0829` n `6`; index avg `0.4315` n `27`; metal avg `0.0552` n `20`; unknown avg `0.2092` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
