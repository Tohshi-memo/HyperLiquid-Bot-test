# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T02:30:31.224169+00:00`
- Correlation status: `ready`
- Asset price records: `129`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `7`; crypto_alt avg `-0.1528` n `223`; crypto_major avg `-0.1686` n `7`; equity avg `-0.019` n `42`; fx avg `0.0` n `4`; index avg `-0.0045` n `9`; metal avg `-0.0089` n `7`; unknown avg `-0.0263` n `313`
- 1h: commodity avg `-0.0303` n `7`; crypto_alt avg `-0.586` n `223`; crypto_major avg `-0.2999` n `7`; equity avg `-0.074` n `42`; fx avg `-0.0003` n `4`; index avg `-0.0442` n `9`; metal avg `0.0129` n `7`; unknown avg `-0.028` n `313`
- 4h: commodity avg `0.0531` n `7`; crypto_alt avg `-1.2925` n `223`; crypto_major avg `-0.8255` n `7`; equity avg `-0.0684` n `42`; fx avg `-0.0061` n `4`; index avg `-0.0192` n `9`; metal avg `0.0034` n `7`; unknown avg `-0.1416` n `313`
- 24h: commodity avg `-0.1655` n `7`; crypto_alt avg `0.5853` n `223`; crypto_major avg `-0.2884` n `7`; equity avg `0.535` n `42`; fx avg `0.003` n `4`; index avg `0.0093` n `9`; metal avg `0.0281` n `7`; unknown avg `0.0964` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.45`, n `125`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4347`, n `125`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.4231`, n `125`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4152`, n `121`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.4134`, n `125`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4129`, n `121`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.4116`, n `125`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4045`, n `121`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.404`, n `125`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3993`, n `121`, moderate_sample_signal
