# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T09:45:34.173628+00:00`
- Correlation status: `ready`
- Asset price records: `158`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0084` n `7`; crypto_alt avg `0.1963` n `223`; crypto_major avg `0.0145` n `7`; equity avg `0.0031` n `42`; fx avg `0.0` n `4`; index avg `0.0003` n `9`; metal avg `0.006` n `7`; unknown avg `-0.0065` n `313`
- 1h: commodity avg `-0.0237` n `7`; crypto_alt avg `0.1554` n `223`; crypto_major avg `0.1588` n `7`; equity avg `0.0863` n `42`; fx avg `0.0005` n `4`; index avg `-0.0282` n `9`; metal avg `0.0206` n `7`; unknown avg `-0.0415` n `313`
- 4h: commodity avg `-0.0686` n `7`; crypto_alt avg `0.6741` n `223`; crypto_major avg `0.3632` n `7`; equity avg `-0.1904` n `42`; fx avg `0.0151` n `4`; index avg `0.01` n `9`; metal avg `0.1226` n `7`; unknown avg `0.0246` n `311`
- 24h: commodity avg `-0.2252` n `7`; crypto_alt avg `1.1643` n `223`; crypto_major avg `-0.0935` n `7`; equity avg `0.2597` n `42`; fx avg `0.1343` n `4`; index avg `0.0599` n `9`; metal avg `0.1138` n `7`; unknown avg `0.1266` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4182`, n `154`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4034`, n `154`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `154`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3899`, n `150`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `154`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3847`, n `150`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3749`, n `150`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3675`, n `150`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3351`, n `154`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3297`, n `154`, moderate_sample_signal
