# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T04:08:31.343778+00:00`
- Correlation status: `ready`
- Asset price records: `135`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `7`; crypto_alt avg `-0.0008` n `223`; crypto_major avg `-0.0027` n `7`; equity avg `0.0344` n `42`; fx avg `0.0013` n `4`; index avg `-0.0004` n `9`; metal avg `-0.0002` n `7`; unknown avg `-0.034` n `313`
- 1h: commodity avg `0.0578` n `7`; crypto_alt avg `-0.0344` n `223`; crypto_major avg `0.0334` n `7`; equity avg `0.0388` n `42`; fx avg `0.0034` n `4`; index avg `0.0004` n `9`; metal avg `0.0119` n `7`; unknown avg `-0.0317` n `313`
- 4h: commodity avg `0.0307` n `7`; crypto_alt avg `-1.1907` n `223`; crypto_major avg `-0.6441` n `7`; equity avg `-0.04` n `42`; fx avg `-0.0019` n `4`; index avg `-0.0296` n `9`; metal avg `0.0021` n `7`; unknown avg `-0.1019` n `313`
- 24h: commodity avg `-0.1284` n `7`; crypto_alt avg `0.646` n `223`; crypto_major avg `-0.3393` n `7`; equity avg `0.6224` n `42`; fx avg `0.0202` n `4`; index avg `-0.0056` n `9`; metal avg `0.0556` n `7`; unknown avg `0.0864` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4476`, n `131`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4324`, n `131`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.4232`, n `131`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.4161`, n `131`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.413`, n `127`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.4118`, n `131`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4105`, n `127`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.404`, n `131`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3996`, n `127`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3945`, n `127`, moderate_sample_signal
