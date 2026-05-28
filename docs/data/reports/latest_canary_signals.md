# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T10:22:19.049205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0261` n `12`; crypto_alt avg `-0.4164` n `228`; crypto_major avg `-0.2307` n `8`; equity avg `-0.1475` n `67`; fx avg `-0.0199` n `6`; index avg `-0.0503` n `23`; metal avg `-0.0658` n `18`; unknown avg `0.0371` n `419`
- 1h: commodity avg `-0.0774` n `12`; crypto_alt avg `-0.0338` n `228`; crypto_major avg `0.0075` n `8`; equity avg `-0.2006` n `67`; fx avg `-0.0276` n `6`; index avg `-0.102` n `23`; metal avg `-0.1336` n `18`; unknown avg `-0.0538` n `419`
- 4h: commodity avg `-0.3488` n `12`; crypto_alt avg `0.1172` n `228`; crypto_major avg `0.2696` n `8`; equity avg `-0.0168` n `67`; fx avg `-0.0117` n `6`; index avg `-0.024` n `23`; metal avg `0.2968` n `18`; unknown avg `0.1905` n `419`
- 24h: commodity avg `0.4546` n `12`; crypto_alt avg `-4.8779` n `228`; crypto_major avg `-3.8485` n `8`; equity avg `-1.756` n `67`; fx avg `-0.1003` n `6`; index avg `-1.1145` n `23`; metal avg `-1.6565` n `18`; unknown avg `-1.6004` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1831`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
