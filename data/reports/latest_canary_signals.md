# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T21:07:30.728624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `-0.3332` n `234`; crypto_major avg `-0.4068` n `8`; equity avg `0.023` n `140`; fx avg `0.0048` n `6`; index avg `0.0162` n `26`; metal avg `0.0115` n `20`; unknown avg `-0.0378` n `942`
- 1h: commodity avg `0.0158` n `12`; crypto_alt avg `-0.078` n `234`; crypto_major avg `0.2198` n `8`; equity avg `-0.0266` n `140`; fx avg `-0.0031` n `6`; index avg `0.0092` n `26`; metal avg `0.0094` n `20`; unknown avg `51.8808` n `888`
- 4h: commodity avg `0.0677` n `12`; crypto_alt avg `-0.0753` n `234`; crypto_major avg `0.7995` n `8`; equity avg `0.2041` n `140`; fx avg `0.0049` n `6`; index avg `0.057` n `26`; metal avg `0.0563` n `20`; unknown avg `31.1553` n `852`
- 24h: commodity avg `-1.03` n `12`; crypto_alt avg `4.0904` n `234`; crypto_major avg `6.1723` n `8`; equity avg `2.807` n `140`; fx avg `-0.0914` n `6`; index avg `0.6092` n `26`; metal avg `0.057` n `20`; unknown avg `10.2161` n `731`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
