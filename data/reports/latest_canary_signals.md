# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T14:07:30.887090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `13`; crypto_alt avg `-0.04` n `239`; crypto_major avg `-0.0687` n `8`; equity avg `-0.1543` n `158`; fx avg `0.004` n `6`; index avg `-0.0266` n `27`; metal avg `-0.0356` n `20`; unknown avg `3.0687` n `1259`
- 1h: commodity avg `0.0194` n `13`; crypto_alt avg `-0.2002` n `239`; crypto_major avg `-0.3028` n `8`; equity avg `-0.1374` n `158`; fx avg `0.0016` n `6`; index avg `-0.0007` n `27`; metal avg `-0.0075` n `20`; unknown avg `3.0616` n `1257`
- 4h: commodity avg `-0.465` n `13`; crypto_alt avg `1.4294` n `239`; crypto_major avg `0.5403` n `8`; equity avg `0.6912` n `158`; fx avg `-0.0278` n `6`; index avg `0.0887` n `27`; metal avg `0.1036` n `20`; unknown avg `35.5507` n `1251`
- 24h: commodity avg `-0.4678` n `13`; crypto_alt avg `0.0974` n `239`; crypto_major avg `-3.0915` n `8`; equity avg `0.2891` n `158`; fx avg `-0.1102` n `6`; index avg `0.0461` n `27`; metal avg `0.3818` n `20`; unknown avg `4.1129` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
