# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T06:00:28.540681+00:00`
- Correlation status: `ready`
- Asset price records: `428`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2782` n `7`; crypto_alt avg `0.2129` n `223`; crypto_major avg `0.2557` n `7`; equity avg `0.086` n `47`; fx avg `-0.0232` n `4`; index avg `0.0092` n `6`; metal avg `0.1371` n `7`; unknown avg `0.1132` n `311`
- 1h: commodity avg `-0.1238` n `7`; crypto_alt avg `0.2933` n `223`; crypto_major avg `0.2746` n `7`; equity avg `0.2332` n `47`; fx avg `0.0291` n `4`; index avg `0.0696` n `6`; metal avg `0.1546` n `7`; unknown avg `0.253` n `311`
- 4h: commodity avg `-0.1141` n `7`; crypto_alt avg `0.068` n `223`; crypto_major avg `0.2175` n `7`; equity avg `0.7075` n `47`; fx avg `-0.183` n `4`; index avg `0.243` n `6`; metal avg `0.6686` n `7`; unknown avg `0.5472` n `311`
- 24h: commodity avg `-1.6106` n `7`; crypto_alt avg `2.422` n `223`; crypto_major avg `1.6651` n `7`; equity avg `2.8563` n `47`; fx avg `-0.3979` n `4`; index avg `2.2711` n `6`; metal avg `2.0611` n `7`; unknown avg `1.3641` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1808`, n `424`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1745`, n `424`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1278`, n `424`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1265`, n `424`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1226`, n `424`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1107`, n `424`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1017`, n `420`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0966`, n `420`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `424`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `424`, weak_sample_signal
