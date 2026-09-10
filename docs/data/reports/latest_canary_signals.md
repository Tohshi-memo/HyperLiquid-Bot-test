# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T19:07:34.340766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0926` n `12`; crypto_alt avg `-0.1419` n `233`; crypto_major avg `0.0229` n `8`; equity avg `-0.1906` n `135`; fx avg `0.0029` n `6`; index avg `-0.0483` n `26`; metal avg `-0.127` n `20`; unknown avg `3.5089` n `795`
- 1h: commodity avg `-0.026` n `12`; crypto_alt avg `0.1242` n `233`; crypto_major avg `0.1764` n `8`; equity avg `-0.2133` n `135`; fx avg `-0.0023` n `6`; index avg `-0.0318` n `26`; metal avg `-0.1609` n `20`; unknown avg `0.7106` n `795`
- 4h: commodity avg `0.4429` n `12`; crypto_alt avg `0.0231` n `233`; crypto_major avg `-0.0139` n `8`; equity avg `-0.8104` n `135`; fx avg `0.0224` n `6`; index avg `-0.1314` n `26`; metal avg `-0.3239` n `20`; unknown avg `0.1903` n `788`
- 24h: commodity avg `0.9731` n `12`; crypto_alt avg `-4.0612` n `233`; crypto_major avg `-3.1132` n `8`; equity avg `-2.1247` n `135`; fx avg `0.0969` n `6`; index avg `-0.3473` n `26`; metal avg `-1.3019` n `20`; unknown avg `-0.4919` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
