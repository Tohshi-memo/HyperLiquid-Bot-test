# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T19:51:02.833582+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `-0.1462` n `230`; crypto_major avg `-0.1678` n `8`; equity avg `-0.03` n `121`; fx avg `-0.004` n `6`; index avg `0.0` n `25`; metal avg `0.0431` n `20`; unknown avg `0.005` n `792`
- 1h: commodity avg `-0.0363` n `12`; crypto_alt avg `-0.1143` n `230`; crypto_major avg `-0.248` n `8`; equity avg `0.3282` n `121`; fx avg `-0.0088` n `6`; index avg `0.0469` n `25`; metal avg `0.0912` n `20`; unknown avg `-0.1577` n `792`
- 4h: commodity avg `0.0621` n `12`; crypto_alt avg `-0.3193` n `230`; crypto_major avg `-0.4537` n `8`; equity avg `0.0777` n `121`; fx avg `0.0211` n `6`; index avg `-0.0157` n `25`; metal avg `0.0652` n `20`; unknown avg `1.074` n `792`
- 24h: commodity avg `0.4276` n `12`; crypto_alt avg `4.9566` n `230`; crypto_major avg `7.0073` n `8`; equity avg `-0.4384` n `121`; fx avg `0.1998` n `6`; index avg `-0.0059` n `25`; metal avg `0.217` n `20`; unknown avg `3.0576` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2247`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
