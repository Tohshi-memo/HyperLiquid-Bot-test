# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T21:07:38.728538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `13`; crypto_alt avg `-0.2036` n `239`; crypto_major avg `-0.1832` n `8`; equity avg `-0.17` n `160`; fx avg `0.009` n `6`; index avg `0.0002` n `27`; metal avg `-0.0197` n `20`; unknown avg `3.5389` n `1223`
- 1h: commodity avg `0.2099` n `13`; crypto_alt avg `-0.2059` n `239`; crypto_major avg `0.0605` n `8`; equity avg `-0.2237` n `160`; fx avg `0.0238` n `6`; index avg `0.0249` n `27`; metal avg `-0.0121` n `20`; unknown avg `3.5609` n `1221`
- 4h: commodity avg `-0.1296` n `13`; crypto_alt avg `-0.393` n `239`; crypto_major avg `-0.063` n `8`; equity avg `-0.1121` n `160`; fx avg `-0.0006` n `6`; index avg `0.103` n `27`; metal avg `0.2395` n `20`; unknown avg `23.1344` n `1211`
- 24h: commodity avg `-0.3211` n `13`; crypto_alt avg `0.3978` n `239`; crypto_major avg `-2.2078` n `8`; equity avg `4.0855` n `160`; fx avg `-0.1256` n `6`; index avg `0.5735` n `27`; metal avg `0.6525` n `20`; unknown avg `4.8066` n `1058`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
