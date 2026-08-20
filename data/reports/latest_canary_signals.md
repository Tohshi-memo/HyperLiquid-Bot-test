# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T23:22:23.232251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.168` n `230`; crypto_major avg `0.3053` n `8`; equity avg `0.0465` n `121`; fx avg `0.0032` n `6`; index avg `-0.0077` n `25`; metal avg `0.0093` n `20`; unknown avg `-0.0796` n `793`
- 1h: commodity avg `0.0183` n `12`; crypto_alt avg `0.2678` n `230`; crypto_major avg `0.3297` n `8`; equity avg `0.0918` n `121`; fx avg `0.0301` n `6`; index avg `0.0212` n `25`; metal avg `0.0827` n `20`; unknown avg `-0.2428` n `793`
- 4h: commodity avg `-0.0489` n `12`; crypto_alt avg `0.9365` n `230`; crypto_major avg `0.731` n `8`; equity avg `0.3462` n `121`; fx avg `-0.0068` n `6`; index avg `0.0147` n `25`; metal avg `0.0903` n `20`; unknown avg `-0.3619` n `792`
- 24h: commodity avg `0.3299` n `12`; crypto_alt avg `4.8912` n `230`; crypto_major avg `5.4344` n `8`; equity avg `-1.0868` n `121`; fx avg `0.1995` n `6`; index avg `-0.1414` n `25`; metal avg `0.1581` n `20`; unknown avg `2.6573` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.18`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
