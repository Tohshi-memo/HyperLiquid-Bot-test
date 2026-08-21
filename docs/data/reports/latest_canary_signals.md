# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T05:02:58.933689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0412` n `12`; crypto_alt avg `-0.0654` n `230`; crypto_major avg `-0.0684` n `8`; equity avg `0.0203` n `121`; fx avg `-0.0029` n `6`; index avg `-0.0077` n `25`; metal avg `-0.03` n `20`; unknown avg `0.2499` n `793`
- 1h: commodity avg `-0.051` n `12`; crypto_alt avg `0.2772` n `230`; crypto_major avg `0.168` n `8`; equity avg `0.0558` n `121`; fx avg `-0.0141` n `6`; index avg `0.0039` n `25`; metal avg `-0.0016` n `20`; unknown avg `0.1004` n `793`
- 4h: commodity avg `-0.0754` n `12`; crypto_alt avg `1.0644` n `230`; crypto_major avg `0.8064` n `8`; equity avg `0.5156` n `121`; fx avg `-0.0704` n `6`; index avg `0.1237` n `25`; metal avg `0.19` n `20`; unknown avg `-0.0488` n `793`
- 24h: commodity avg `0.2394` n `12`; crypto_alt avg `5.7695` n `230`; crypto_major avg `6.7889` n `8`; equity avg `-0.5002` n `121`; fx avg `-0.0403` n `6`; index avg `-0.0716` n `25`; metal avg `0.4891` n `20`; unknown avg `2.6481` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1812`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
