# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T14:15:20.490486+00:00`
- Correlation status: `ready`
- Asset price records: `176`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `7`; crypto_alt avg `0.114` n `223`; crypto_major avg `0.1221` n `7`; equity avg `-0.0361` n `42`; fx avg `-0.0053` n `4`; index avg `-0.0005` n `9`; metal avg `0.0213` n `7`; unknown avg `0.0365` n `313`
- 1h: commodity avg `-0.0245` n `7`; crypto_alt avg `-0.0621` n `223`; crypto_major avg `-0.0398` n `7`; equity avg `-0.0355` n `42`; fx avg `0.0101` n `4`; index avg `-0.0421` n `9`; metal avg `0.0194` n `7`; unknown avg `-0.1668` n `313`
- 4h: commodity avg `-0.1204` n `7`; crypto_alt avg `0.0535` n `223`; crypto_major avg `0.3653` n `7`; equity avg `0.1461` n `42`; fx avg `0.0207` n `4`; index avg `0.0043` n `9`; metal avg `0.0772` n `7`; unknown avg `-0.2238` n `313`
- 24h: commodity avg `-0.3187` n `7`; crypto_alt avg `0.6902` n `223`; crypto_major avg `0.2806` n `7`; equity avg `0.2922` n `42`; fx avg `0.1644` n `4`; index avg `0.0193` n `9`; metal avg `0.2003` n `7`; unknown avg `0.1414` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4031`, n `172`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3853`, n `172`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3846`, n `172`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3791`, n `168`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3742`, n `168`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3709`, n `172`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.357`, n `168`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3475`, n `168`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3222`, n `172`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3055`, n `172`, moderate_sample_signal
