# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T17:30:22.199253+00:00`
- Correlation status: `ready`
- Asset price records: `189`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1213` n `7`; crypto_alt avg `0.0947` n `223`; crypto_major avg `0.0701` n `7`; equity avg `0.0683` n `42`; fx avg `-0.0035` n `4`; index avg `0.0217` n `9`; metal avg `0.031` n `7`; unknown avg `0.0585` n `314`
- 1h: commodity avg `-0.0069` n `7`; crypto_alt avg `0.1739` n `223`; crypto_major avg `0.1406` n `7`; equity avg `0.0649` n `42`; fx avg `-0.0072` n `4`; index avg `0.0217` n `9`; metal avg `0.1092` n `7`; unknown avg `0.2252` n `313`
- 4h: commodity avg `-0.4129` n `7`; crypto_alt avg `0.154` n `223`; crypto_major avg `0.1131` n `7`; equity avg `0.2185` n `42`; fx avg `-0.0039` n `4`; index avg `0.0923` n `9`; metal avg `0.2267` n `7`; unknown avg `0.2431` n `313`
- 24h: commodity avg `-0.6027` n `7`; crypto_alt avg `-0.0824` n `223`; crypto_major avg `0.0844` n `7`; equity avg `0.5404` n `42`; fx avg `0.0763` n `4`; index avg `0.1164` n `9`; metal avg `0.4025` n `7`; unknown avg `0.1222` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4002`, n `185`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3877`, n `181`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3824`, n `185`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3816`, n `181`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3789`, n `185`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3653`, n `185`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3261`, n `185`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3084`, n `181`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3067`, n `185`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3063`, n `185`, moderate_sample_signal
