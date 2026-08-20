# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T20:20:09.527186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `0.1298` n `230`; crypto_major avg `0.1147` n `8`; equity avg `-0.0827` n `121`; fx avg `-0.0004` n `6`; index avg `-0.0139` n `25`; metal avg `-0.0288` n `20`; unknown avg `-0.0671` n `792`
- 1h: commodity avg `-0.0297` n `12`; crypto_alt avg `0.0139` n `230`; crypto_major avg `0.058` n `8`; equity avg `0.2249` n `121`; fx avg `-0.0194` n `6`; index avg `-0.0122` n `25`; metal avg `0.0191` n `20`; unknown avg `-0.232` n `792`
- 4h: commodity avg `0.0532` n `12`; crypto_alt avg `0.1415` n `230`; crypto_major avg `-0.2381` n `8`; equity avg `0.2948` n `121`; fx avg `-0.0261` n `6`; index avg `-0.0515` n `25`; metal avg `0.0663` n `20`; unknown avg `0.9435` n `792`
- 24h: commodity avg `0.3956` n `12`; crypto_alt avg `5.1106` n `230`; crypto_major avg `7.168` n `8`; equity avg `-0.5347` n `121`; fx avg `0.1902` n `6`; index avg `-0.0418` n `25`; metal avg `0.1915` n `20`; unknown avg `2.9957` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2244`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
