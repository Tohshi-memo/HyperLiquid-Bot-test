# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T01:07:23.702746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `13`; crypto_alt avg `0.1227` n `239`; crypto_major avg `0.0846` n `8`; equity avg `0.2176` n `158`; fx avg `0.0091` n `6`; index avg `0.029` n `27`; metal avg `0.0096` n `20`; unknown avg `4.4258` n `1257`
- 1h: commodity avg `-0.0139` n `13`; crypto_alt avg `0.3254` n `239`; crypto_major avg `0.1534` n `8`; equity avg `0.2507` n `158`; fx avg `0.0036` n `6`; index avg `0.0306` n `27`; metal avg `0.0084` n `20`; unknown avg `3.9735` n `1255`
- 4h: commodity avg `0.061` n `13`; crypto_alt avg `-0.0324` n `239`; crypto_major avg `0.2729` n `8`; equity avg `0.2134` n `158`; fx avg `-0.0025` n `6`; index avg `0.0062` n `27`; metal avg `0.036` n `20`; unknown avg `134.5851` n `1197`
- 24h: commodity avg `0.1062` n `13`; crypto_alt avg `1.1211` n `239`; crypto_major avg `-0.2664` n `8`; equity avg `2.0754` n `158`; fx avg `-0.0854` n `6`; index avg `0.3138` n `27`; metal avg `0.017` n `20`; unknown avg `8.2128` n `1024`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
