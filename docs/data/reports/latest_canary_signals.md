# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T11:30:23.869765+00:00`
- Correlation status: `ready`
- Asset price records: `165`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0229` n `7`; crypto_alt avg `-0.0537` n `223`; crypto_major avg `-0.0227` n `7`; equity avg `-0.0197` n `42`; fx avg `0.0024` n `4`; index avg `0.0662` n `9`; metal avg `0.0208` n `7`; unknown avg `-0.0124` n `313`
- 1h: commodity avg `-0.0371` n `7`; crypto_alt avg `-0.1424` n `223`; crypto_major avg `-0.0302` n `7`; equity avg `0.1076` n `42`; fx avg `0.0111` n `4`; index avg `0.025` n `9`; metal avg `0.0234` n `7`; unknown avg `-0.1482` n `313`
- 4h: commodity avg `-0.0923` n `7`; crypto_alt avg `0.0516` n `223`; crypto_major avg `0.0435` n `7`; equity avg `0.1073` n `42`; fx avg `0.0231` n `4`; index avg `0.0068` n `9`; metal avg `0.1083` n `7`; unknown avg `-0.3158` n `313`
- 24h: commodity avg `-0.2792` n `7`; crypto_alt avg `1.152` n `223`; crypto_major avg `-0.0208` n `7`; equity avg `0.3268` n `42`; fx avg `0.1561` n `4`; index avg `0.1022` n `9`; metal avg `0.1486` n `7`; unknown avg `-0.0069` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4138`, n `161`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `161`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3993`, n `161`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `161`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3827`, n `157`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3777`, n `157`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3627`, n `157`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3546`, n `157`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3332`, n `161`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3272`, n `161`, moderate_sample_signal
