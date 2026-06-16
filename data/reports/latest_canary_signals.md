# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T10:22:37.056647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0277` n `12`; crypto_alt avg `0.0936` n `228`; crypto_major avg `0.2464` n `8`; equity avg `0.0479` n `77`; fx avg `0.0194` n `6`; index avg `0.1748` n `23`; metal avg `0.0447` n `18`; unknown avg `0.0448` n `687`
- 1h: commodity avg `0.1228` n `12`; crypto_alt avg `-0.0474` n `228`; crypto_major avg `0.1122` n `8`; equity avg `-0.0512` n `77`; fx avg `0.0115` n `6`; index avg `0.19` n `23`; metal avg `0.1098` n `18`; unknown avg `0.1693` n `687`
- 4h: commodity avg `-0.5811` n `12`; crypto_alt avg `1.0161` n `228`; crypto_major avg `1.2113` n `8`; equity avg `0.545` n `77`; fx avg `0.0543` n `6`; index avg `0.3518` n `23`; metal avg `1.0307` n `18`; unknown avg `0.2461` n `687`
- 24h: commodity avg `0.1092` n `12`; crypto_alt avg `1.2411` n `228`; crypto_major avg `3.2243` n `8`; equity avg `1.8027` n `76`; fx avg `-0.0708` n `6`; index avg `0.7025` n `23`; metal avg `0.3277` n `18`; unknown avg `0.0834` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
