# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T23:45:54.000509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `-0.0883` n `230`; crypto_major avg `-0.0784` n `8`; equity avg `-0.0251` n `121`; fx avg `-0.0139` n `6`; index avg `-0.0229` n `25`; metal avg `-0.0015` n `20`; unknown avg `-0.1129` n `793`
- 1h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.2914` n `230`; crypto_major avg `0.3825` n `8`; equity avg `-0.0928` n `121`; fx avg `0.0189` n `6`; index avg `-0.0595` n `25`; metal avg `0.0059` n `20`; unknown avg `-0.3282` n `793`
- 4h: commodity avg `-0.0454` n `12`; crypto_alt avg `1.2794` n `230`; crypto_major avg `1.0575` n `8`; equity avg `0.1298` n `121`; fx avg `-0.0105` n `6`; index avg `-0.0454` n `25`; metal avg `0.0187` n `20`; unknown avg `-0.3312` n `792`
- 24h: commodity avg `0.3457` n `12`; crypto_alt avg `4.9307` n `230`; crypto_major avg `5.8415` n `8`; equity avg `-1.1874` n `121`; fx avg `0.1869` n `6`; index avg `-0.169` n `25`; metal avg `0.1721` n `20`; unknown avg `2.6764` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
