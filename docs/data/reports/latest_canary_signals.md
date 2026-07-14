# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T07:22:30.618200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0697` n `12`; crypto_alt avg `0.0071` n `230`; crypto_major avg `-0.0198` n `8`; equity avg `0.0384` n `92`; fx avg `-0.0263` n `6`; index avg `0.0228` n `25`; metal avg `-0.022` n `20`; unknown avg `0.0339` n `766`
- 1h: commodity avg `0.1035` n `12`; crypto_alt avg `-0.047` n `230`; crypto_major avg `-0.1572` n `8`; equity avg `0.0663` n `92`; fx avg `-0.0122` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0051` n `20`; unknown avg `-0.069` n `766`
- 4h: commodity avg `0.0601` n `12`; crypto_alt avg `0.9156` n `230`; crypto_major avg `0.6756` n `8`; equity avg `1.713` n `92`; fx avg `0.0274` n `6`; index avg `0.4322` n `25`; metal avg `0.2621` n `20`; unknown avg `0.0685` n `750`
- 24h: commodity avg `1.1847` n `12`; crypto_alt avg `-0.5392` n `230`; crypto_major avg `-0.7133` n `8`; equity avg `-0.3464` n `92`; fx avg `-0.1531` n `6`; index avg `-0.0577` n `25`; metal avg `0.0615` n `20`; unknown avg `-0.2481` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
