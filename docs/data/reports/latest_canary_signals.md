# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T16:28:56.982859+00:00`
- Correlation status: `ready`
- Asset price records: `184`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0761` n `7`; crypto_alt avg `-0.0992` n `223`; crypto_major avg `-0.0365` n `7`; equity avg `0.1117` n `42`; fx avg `0.0035` n `4`; index avg `0.0376` n `9`; metal avg `0.0069` n `7`; unknown avg `0.0511` n `313`
- 1h: commodity avg `-0.2285` n `7`; crypto_alt avg `-0.2544` n `223`; crypto_major avg `-0.155` n `7`; equity avg `0.1174` n `42`; fx avg `0.0014` n `4`; index avg `0.0785` n `9`; metal avg `0.0649` n `7`; unknown avg `0.029` n `313`
- 4h: commodity avg `-0.4412` n `7`; crypto_alt avg `-0.3315` n `223`; crypto_major avg `-0.2472` n `7`; equity avg `0.17` n `42`; fx avg `0.0149` n `4`; index avg `0.0524` n `9`; metal avg `0.1446` n `7`; unknown avg `-0.0206` n `313`
- 24h: commodity avg `-0.6422` n `7`; crypto_alt avg `-0.2198` n `223`; crypto_major avg `-0.1335` n `7`; equity avg `0.4729` n `42`; fx avg `0.1195` n `4`; index avg `0.091` n `9`; metal avg `0.2993` n `7`; unknown avg `-0.0164` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4021`, n `180`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3844`, n `180`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3808`, n `180`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3805`, n `176`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3752`, n `176`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3671`, n `180`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3242`, n `180`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3211`, n `176`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3096`, n `176`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.306`, n `180`, moderate_sample_signal
