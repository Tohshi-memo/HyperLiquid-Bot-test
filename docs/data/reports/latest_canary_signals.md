# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T02:00:28.757636+00:00`
- Correlation status: `ready`
- Asset price records: `127`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `7`; crypto_alt avg `0.039` n `223`; crypto_major avg `-0.0139` n `7`; equity avg `-0.0275` n `42`; fx avg `-0.0082` n `4`; index avg `-0.0156` n `9`; metal avg `0.0013` n `7`; unknown avg `0.1236` n `313`
- 1h: commodity avg `0.0196` n `7`; crypto_alt avg `-0.6468` n `223`; crypto_major avg `-0.3593` n `7`; equity avg `-0.0559` n `42`; fx avg `-0.0114` n `4`; index avg `-0.0321` n `9`; metal avg `0.0064` n `7`; unknown avg `0.2483` n `313`
- 4h: commodity avg `0.1007` n `7`; crypto_alt avg `-1.1562` n `223`; crypto_major avg `-0.8748` n `7`; equity avg `-0.1108` n `42`; fx avg `-0.0183` n `4`; index avg `-0.0183` n `9`; metal avg `-0.0006` n `7`; unknown avg `-0.0634` n `313`
- 24h: commodity avg `-0.117` n `7`; crypto_alt avg `0.7995` n `223`; crypto_major avg `-0.2238` n `7`; equity avg `0.6324` n `42`; fx avg `-0.0243` n `4`; index avg `0.0435` n `9`; metal avg `0.0205` n `7`; unknown avg `0.1271` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4536`, n `123`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4381`, n `123`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.419`, n `119`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4168`, n `119`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4039`, n `123`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4037`, n `119`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3984`, n `119`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3881`, n `119`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3861`, n `123`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.3736`, n `119`, moderate_sample_signal
