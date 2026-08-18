# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T07:07:29.539555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0699` n `12`; crypto_alt avg `-0.0374` n `230`; crypto_major avg `0.023` n `8`; equity avg `0.0605` n `114`; fx avg `-0.0154` n `6`; index avg `0.0314` n `25`; metal avg `-0.0015` n `20`; unknown avg `-0.0092` n `793`
- 1h: commodity avg `-0.0833` n `12`; crypto_alt avg `0.3949` n `230`; crypto_major avg `0.4221` n `8`; equity avg `0.4533` n `114`; fx avg `-0.0045` n `6`; index avg `0.1168` n `25`; metal avg `0.1071` n `20`; unknown avg `0.2177` n `793`
- 4h: commodity avg `0.0142` n `12`; crypto_alt avg `0.4672` n `230`; crypto_major avg `0.4625` n `8`; equity avg `0.1239` n `114`; fx avg `0.026` n `6`; index avg `-0.0614` n `25`; metal avg `0.04` n `20`; unknown avg `0.0773` n `761`
- 24h: commodity avg `0.7353` n `12`; crypto_alt avg `-1.2125` n `230`; crypto_major avg `0.0702` n `8`; equity avg `-1.5296` n `114`; fx avg `-0.0242` n `6`; index avg `-0.3986` n `25`; metal avg `-0.1683` n `20`; unknown avg `0.0138` n `760`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
