# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T01:07:29.514962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1493` n `12`; crypto_alt avg `0.4417` n `230`; crypto_major avg `0.4169` n `8`; equity avg `0.722` n `102`; fx avg `0.0179` n `6`; index avg `0.1686` n `25`; metal avg `0.2` n `20`; unknown avg `2.1672` n `778`
- 1h: commodity avg `-0.0784` n `12`; crypto_alt avg `0.1854` n `230`; crypto_major avg `0.0243` n `8`; equity avg `0.7077` n `102`; fx avg `-0.0041` n `6`; index avg `0.1501` n `25`; metal avg `0.06` n `20`; unknown avg `4.6203` n `778`
- 4h: commodity avg `-0.1989` n `12`; crypto_alt avg `1.6435` n `230`; crypto_major avg `1.2941` n `8`; equity avg `1.9634` n `102`; fx avg `-0.0139` n `6`; index avg `0.3937` n `25`; metal avg `0.2575` n `20`; unknown avg `1.5841` n `778`
- 24h: commodity avg `0.488` n `12`; crypto_alt avg `-1.7891` n `230`; crypto_major avg `-0.3102` n `8`; equity avg `-2.834` n `102`; fx avg `0.0052` n `6`; index avg `-0.4669` n `25`; metal avg `0.5023` n `20`; unknown avg `-0.555` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
