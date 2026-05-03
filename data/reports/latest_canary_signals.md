# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T07:30:24.901188+00:00`
- Correlation status: `ready`
- Asset price records: `149`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0116` n `7`; crypto_alt avg `0.0635` n `223`; crypto_major avg `0.082` n `7`; equity avg `0.0079` n `42`; fx avg `0.004` n `4`; index avg `0.0463` n `9`; metal avg `0.0242` n `7`; unknown avg `0.0383` n `313`
- 1h: commodity avg `0.0168` n `7`; crypto_alt avg `0.3552` n `223`; crypto_major avg `0.3254` n `7`; equity avg `-0.0361` n `42`; fx avg `0.0077` n `4`; index avg `0.0354` n `9`; metal avg `0.0354` n `7`; unknown avg `0.3037` n `313`
- 4h: commodity avg `-0.0443` n `7`; crypto_alt avg `0.7183` n `223`; crypto_major avg `0.3242` n `7`; equity avg `-0.1706` n `42`; fx avg `0.0127` n `4`; index avg `0.0593` n `9`; metal avg `0.055` n `7`; unknown avg `0.3575` n `311`
- 24h: commodity avg `-0.1501` n `7`; crypto_alt avg `1.3217` n `223`; crypto_major avg `-0.0227` n `7`; equity avg `0.1802` n `42`; fx avg `0.1611` n `4`; index avg `0.1008` n `9`; metal avg `0.0869` n `7`; unknown avg `0.5775` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4317`, n `145`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4168`, n `145`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4042`, n `145`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3953`, n `141`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.391`, n `141`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3864`, n `145`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3753`, n `141`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3678`, n `141`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3501`, n `145`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3464`, n `145`, moderate_sample_signal
