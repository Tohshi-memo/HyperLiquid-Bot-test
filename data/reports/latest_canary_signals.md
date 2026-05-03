# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T13:45:19.849854+00:00`
- Correlation status: `ready`
- Asset price records: `174`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0103` n `7`; crypto_alt avg `-0.0157` n `223`; crypto_major avg `-0.0845` n `7`; equity avg `-0.0088` n `42`; fx avg `0.0043` n `4`; index avg `-0.0092` n `9`; metal avg `-0.0093` n `7`; unknown avg `-0.1073` n `313`
- 1h: commodity avg `-0.0086` n `7`; crypto_alt avg `-0.2656` n `223`; crypto_major avg `-0.2213` n `7`; equity avg `-0.0327` n `42`; fx avg `0.0154` n `4`; index avg `-0.06` n `9`; metal avg `-0.0035` n `7`; unknown avg `-0.2218` n `313`
- 4h: commodity avg `-0.0777` n `7`; crypto_alt avg `-0.0066` n `223`; crypto_major avg `0.0324` n `7`; equity avg `0.1463` n `42`; fx avg `0.026` n `4`; index avg `0.0052` n `9`; metal avg `0.053` n `7`; unknown avg `-0.2962` n `313`
- 24h: commodity avg `-0.2538` n `7`; crypto_alt avg `0.8346` n `223`; crypto_major avg `-0.0013` n `7`; equity avg `0.2853` n `42`; fx avg `0.1778` n `4`; index avg `0.0166` n `9`; metal avg `0.1803` n `7`; unknown avg `-0.075` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.403`, n `170`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3853`, n `170`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3845`, n `170`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3776`, n `166`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3721`, n `166`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3708`, n `170`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3594`, n `166`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3506`, n `166`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3229`, n `170`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3082`, n `170`, moderate_sample_signal
