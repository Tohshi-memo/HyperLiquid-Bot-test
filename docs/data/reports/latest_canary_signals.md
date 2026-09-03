# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T23:52:29.816257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.013` n `232`; crypto_major avg `0.024` n `8`; equity avg `0.0171` n `133`; fx avg `-0.012` n `6`; index avg `0.0019` n `26`; metal avg `-0.005` n `20`; unknown avg `1.3145` n `792`
- 1h: commodity avg `0.0187` n `12`; crypto_alt avg `0.3488` n `232`; crypto_major avg `0.4134` n `8`; equity avg `0.07` n `133`; fx avg `-0.0228` n `6`; index avg `0.0016` n `26`; metal avg `-0.0019` n `20`; unknown avg `3.3303` n `790`
- 4h: commodity avg `0.0686` n `12`; crypto_alt avg `-0.2809` n `232`; crypto_major avg `-0.2878` n `8`; equity avg `-0.0063` n `133`; fx avg `-0.0008` n `6`; index avg `-0.0149` n `26`; metal avg `-0.0248` n `20`; unknown avg `3.9877` n `766`
- 24h: commodity avg `-0.0684` n `12`; crypto_alt avg `4.0088` n `232`; crypto_major avg `5.1357` n `8`; equity avg `1.2467` n `133`; fx avg `-0.2524` n `6`; index avg `0.1483` n `26`; metal avg `0.7876` n `20`; unknown avg `2.7372` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
