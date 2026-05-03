# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T19:45:19.866743+00:00`
- Correlation status: `ready`
- Asset price records: `198`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `7`; crypto_alt avg `0.0775` n `223`; crypto_major avg `0.0445` n `7`; equity avg `-0.002` n `42`; fx avg `0.0011` n `4`; index avg `0.0036` n `9`; metal avg `-0.0049` n `7`; unknown avg `0.0063` n `314`
- 1h: commodity avg `-0.003` n `7`; crypto_alt avg `0.2016` n `223`; crypto_major avg `0.2377` n `7`; equity avg `0.0457` n `42`; fx avg `0.0346` n `4`; index avg `0.0242` n `9`; metal avg `-0.0293` n `7`; unknown avg `0.0754` n `314`
- 4h: commodity avg `0.2335` n `7`; crypto_alt avg `0.4704` n `223`; crypto_major avg `0.2877` n `7`; equity avg `0.2777` n `42`; fx avg `-0.0097` n `4`; index avg `0.0622` n `9`; metal avg `0.1837` n `7`; unknown avg `0.3729` n `313`
- 24h: commodity avg `-0.093` n `7`; crypto_alt avg `-0.1039` n `223`; crypto_major avg `0.1832` n `7`; equity avg `0.4079` n `42`; fx avg `0.0676` n `4`; index avg `0.0577` n `9`; metal avg `0.4644` n `7`; unknown avg `-0.0075` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3991`, n `194`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3813`, n `194`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3786`, n `190`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3727`, n `194`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3714`, n `190`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3595`, n `194`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3326`, n `194`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3142`, n `194`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3056`, n `194`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2503`, n `190`, moderate_sample_signal
