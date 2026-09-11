# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T21:37:30.805111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.27` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0141` n `12`; crypto_alt avg `-0.2111` n `233`; crypto_major avg `-0.1443` n `8`; equity avg `-0.0118` n `136`; fx avg `-0.011` n `6`; index avg `-0.0004` n `26`; metal avg `0.0005` n `20`; unknown avg `-0.0368` n `822`
- 1h: commodity avg `-0.0838` n `12`; crypto_alt avg `-0.179` n `233`; crypto_major avg `-0.1036` n `8`; equity avg `0.006` n `136`; fx avg `-0.0133` n `6`; index avg `0.004` n `26`; metal avg `0.0072` n `20`; unknown avg `-0.0279` n `820`
- 4h: commodity avg `0.0444` n `12`; crypto_alt avg `-0.7874` n `233`; crypto_major avg `-0.5537` n `8`; equity avg `-0.4141` n `136`; fx avg `-0.0069` n `6`; index avg `-0.06` n `26`; metal avg `-0.0682` n `20`; unknown avg `-0.005` n `770`
- 24h: commodity avg `-0.7921` n `12`; crypto_alt avg `0.324` n `233`; crypto_major avg `1.1859` n `8`; equity avg `0.7519` n `136`; fx avg `-0.1746` n `6`; index avg `0.3013` n `26`; metal avg `0.2533` n `20`; unknown avg `1.1487` n `668`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
