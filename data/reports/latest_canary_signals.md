# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T15:03:15.872212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0283` n `12`; crypto_alt avg `-0.2077` n `233`; crypto_major avg `-0.1281` n `8`; equity avg `-0.0389` n `135`; fx avg `-0.0137` n `6`; index avg `-0.004` n `26`; metal avg `-0.0133` n `20`; unknown avg `-0.1162` n `794`
- 1h: commodity avg `0.0821` n `12`; crypto_alt avg `-0.1584` n `233`; crypto_major avg `0.0451` n `8`; equity avg `0.5363` n `135`; fx avg `0.0253` n `6`; index avg `0.0705` n `26`; metal avg `-0.05` n `20`; unknown avg `0.0194` n `766`
- 4h: commodity avg `0.4384` n `12`; crypto_alt avg `-0.7043` n `233`; crypto_major avg `-1.0979` n `8`; equity avg `-0.3775` n `135`; fx avg `0.0001` n `6`; index avg `-0.2017` n `26`; metal avg `-0.3805` n `20`; unknown avg `-0.7601` n `760`
- 24h: commodity avg `0.3746` n `12`; crypto_alt avg `-4.4067` n `233`; crypto_major avg `-3.4112` n `8`; equity avg `-1.6689` n `135`; fx avg `0.0802` n `6`; index avg `-0.2722` n `26`; metal avg `-0.9777` n `20`; unknown avg `-0.8737` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
