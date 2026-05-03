# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T07:15:23.285863+00:00`
- Correlation status: `ready`
- Asset price records: `148`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `7`; crypto_alt avg `0.1178` n `223`; crypto_major avg `0.0753` n `7`; equity avg `-0.0124` n `42`; fx avg `0.0034` n `4`; index avg `0.0043` n `9`; metal avg `0.0035` n `7`; unknown avg `0.0151` n `313`
- 1h: commodity avg `-0.0195` n `7`; crypto_alt avg `0.3897` n `223`; crypto_major avg `0.2271` n `7`; equity avg `-0.226` n `42`; fx avg `0.0042` n `4`; index avg `-0.0034` n `9`; metal avg `0.0204` n `7`; unknown avg `0.2799` n `313`
- 4h: commodity avg `-0.0565` n `7`; crypto_alt avg `0.6912` n `223`; crypto_major avg `0.2868` n `7`; equity avg `-0.195` n `42`; fx avg `0.0071` n `4`; index avg `0.0148` n `9`; metal avg `0.0279` n `7`; unknown avg `0.315` n `311`
- 24h: commodity avg `-0.1614` n `7`; crypto_alt avg `1.3185` n `223`; crypto_major avg `-0.083` n `7`; equity avg `0.1836` n `42`; fx avg `0.1341` n `4`; index avg `0.0445` n `9`; metal avg `0.0627` n `7`; unknown avg `0.4965` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4378`, n `144`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4228`, n `144`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4043`, n `144`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3981`, n `140`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3943`, n `140`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3865`, n `144`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3749`, n `140`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3674`, n `140`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3399`, n `144`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3365`, n `144`, moderate_sample_signal
