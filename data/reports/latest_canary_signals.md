# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T14:00:30.114837+00:00`
- Correlation status: `ready`
- Asset price records: `366`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1974` n `7`; crypto_alt avg `0.0203` n `223`; crypto_major avg `-0.2031` n `7`; equity avg `-0.4171` n `47`; fx avg `0.0024` n `4`; index avg `-0.2413` n `6`; metal avg `0.1885` n `7`; unknown avg `-0.4142` n `312`
- 1h: commodity avg `-0.3721` n `7`; crypto_alt avg `-0.0994` n `223`; crypto_major avg `-0.0731` n `7`; equity avg `-0.4404` n `47`; fx avg `0.007` n `4`; index avg `0.1172` n `6`; metal avg `0.2662` n `7`; unknown avg `0.2193` n `312`
- 4h: commodity avg `-0.6151` n `7`; crypto_alt avg `0.5117` n `223`; crypto_major avg `0.9115` n `7`; equity avg `0.0038` n `47`; fx avg `0.0502` n `4`; index avg `0.469` n `6`; metal avg `0.3192` n `7`; unknown avg `0.0982` n `312`
- 24h: commodity avg `-0.1605` n `7`; crypto_alt avg `2.3317` n `223`; crypto_major avg `2.4602` n `7`; equity avg `-0.0168` n `47`; fx avg `0.0752` n `4`; index avg `0.7335` n `6`; metal avg `0.4645` n `7`; unknown avg `0.1071` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2081`, n `362`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2009`, n `362`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1339`, n `362`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1299`, n `362`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `362`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `362`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `362`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1029`, n `362`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.093`, n `358`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0886`, n `362`, weak_sample_signal
