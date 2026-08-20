# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T23:37:24.714908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `0.1826` n `230`; crypto_major avg `0.2057` n `8`; equity avg `-0.0569` n `121`; fx avg `0.0056` n `6`; index avg `-0.0223` n `25`; metal avg `-0.0143` n `20`; unknown avg `-0.0371` n `793`
- 1h: commodity avg `0.0061` n `12`; crypto_alt avg `0.4781` n `230`; crypto_major avg `0.5813` n `8`; equity avg `-0.0284` n `121`; fx avg `0.0142` n `6`; index avg `-0.0101` n `25`; metal avg `0.0437` n `20`; unknown avg `-0.2445` n `793`
- 4h: commodity avg `-0.0365` n `12`; crypto_alt avg `1.2212` n `230`; crypto_major avg `0.9659` n `8`; equity avg `0.125` n `121`; fx avg `-0.0007` n `6`; index avg `-0.0225` n `25`; metal avg `0.0635` n `20`; unknown avg `-0.3214` n `792`
- 24h: commodity avg `0.3666` n `12`; crypto_alt avg `4.8669` n `230`; crypto_major avg `5.3328` n `8`; equity avg `-1.1911` n `121`; fx avg `0.1996` n `6`; index avg `-0.1659` n `25`; metal avg `0.1703` n `20`; unknown avg `2.622` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1808`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
