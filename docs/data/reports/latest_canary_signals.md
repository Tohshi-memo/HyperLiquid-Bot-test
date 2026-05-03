# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T03:30:28.690284+00:00`
- Correlation status: `ready`
- Asset price records: `133`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `7`; crypto_alt avg `0.0453` n `223`; crypto_major avg `0.0447` n `7`; equity avg `-0.0165` n `42`; fx avg `-0.0016` n `4`; index avg `0.0018` n `9`; metal avg `-0.0029` n `7`; unknown avg `0.0153` n `313`
- 1h: commodity avg `0.0346` n `7`; crypto_alt avg `-0.0604` n `223`; crypto_major avg `0.0879` n `7`; equity avg `-0.0039` n `42`; fx avg `-0.0003` n `4`; index avg `-0.0099` n `9`; metal avg `0.0199` n `7`; unknown avg `-0.0019` n `313`
- 4h: commodity avg `0.0201` n `7`; crypto_alt avg `-1.4445` n `223`; crypto_major avg `-0.8839` n `7`; equity avg `-0.1053` n `42`; fx avg `-0.0026` n `4`; index avg `-0.0227` n `9`; metal avg `0.0149` n `7`; unknown avg `0.1444` n `313`
- 24h: commodity avg `-0.1327` n `7`; crypto_alt avg `0.5137` n `223`; crypto_major avg `-0.3668` n `7`; equity avg `0.6028` n `42`; fx avg `0.0094` n `4`; index avg `-0.0008` n `9`; metal avg `0.0491` n `7`; unknown avg `0.075` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4489`, n `129`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.4352`, n `129`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4337`, n `129`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.4265`, n `129`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.4252`, n `129`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.413`, n `125`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4105`, n `125`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.404`, n `129`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4029`, n `125`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3978`, n `125`, moderate_sample_signal
