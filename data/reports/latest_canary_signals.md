# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T07:37:29.589626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.021` n `13`; crypto_alt avg `0.0332` n `239`; crypto_major avg `0.0088` n `8`; equity avg `0.0052` n `158`; fx avg `0.0075` n `6`; index avg `0.0003` n `27`; metal avg `0.0034` n `20`; unknown avg `0.0057` n `1262`
- 1h: commodity avg `0.0393` n `13`; crypto_alt avg `0.1323` n `239`; crypto_major avg `0.0239` n `8`; equity avg `0.0519` n `158`; fx avg `0.0103` n `6`; index avg `0.0105` n `27`; metal avg `0.0019` n `20`; unknown avg `199.7146` n `1252`
- 4h: commodity avg `0.0512` n `13`; crypto_alt avg `-0.0548` n `239`; crypto_major avg `0.0442` n `8`; equity avg `0.0342` n `158`; fx avg `0.0204` n `6`; index avg `-0.0035` n `27`; metal avg `0.0081` n `20`; unknown avg `-0.1638` n `1208`
- 24h: commodity avg `0.1471` n `13`; crypto_alt avg `-1.7343` n `239`; crypto_major avg `-0.6363` n `8`; equity avg `0.0713` n `158`; fx avg `0.0588` n `6`; index avg `0.043` n `27`; metal avg `-0.0373` n `20`; unknown avg `158.6053` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
