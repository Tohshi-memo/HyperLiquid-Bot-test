# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T19:22:31.820047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `0.1738` n `230`; crypto_major avg `0.2031` n `8`; equity avg `0.0675` n `121`; fx avg `0.0004` n `6`; index avg `-0.0005` n `25`; metal avg `0.0352` n `20`; unknown avg `-0.0485` n `792`
- 1h: commodity avg `0.121` n `12`; crypto_alt avg `0.0054` n `230`; crypto_major avg `-0.5659` n `8`; equity avg `0.2309` n `121`; fx avg `-0.0028` n `6`; index avg `0.0337` n `25`; metal avg `0.0652` n `20`; unknown avg `-0.0056` n `792`
- 4h: commodity avg `0.1691` n `12`; crypto_alt avg `0.1722` n `230`; crypto_major avg `0.3891` n `8`; equity avg `-0.1737` n `121`; fx avg `0.0432` n `6`; index avg `-0.0478` n `25`; metal avg `-0.0185` n `20`; unknown avg `1.538` n `792`
- 24h: commodity avg `0.4507` n `12`; crypto_alt avg `5.5522` n `230`; crypto_major avg `7.3227` n `8`; equity avg `-0.3568` n `121`; fx avg `0.2053` n `6`; index avg `-0.0457` n `25`; metal avg `0.1927` n `20`; unknown avg `3.3995` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2244`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
