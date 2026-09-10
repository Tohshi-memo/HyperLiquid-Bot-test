# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T14:22:35.236295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0359` n `12`; crypto_alt avg `-0.015` n `233`; crypto_major avg `0.1322` n `8`; equity avg `0.2184` n `135`; fx avg `0.0144` n `6`; index avg `0.0604` n `26`; metal avg `0.0417` n `20`; unknown avg `-0.0358` n `796`
- 1h: commodity avg `-0.1296` n `12`; crypto_alt avg `0.3307` n `233`; crypto_major avg `0.3303` n `8`; equity avg `0.6404` n `135`; fx avg `0.0039` n `6`; index avg `0.0344` n `26`; metal avg `0.0684` n `20`; unknown avg `0.605` n `794`
- 4h: commodity avg `0.3464` n `12`; crypto_alt avg `-0.7298` n `233`; crypto_major avg `-1.23` n `8`; equity avg `-0.8716` n `135`; fx avg `0.0096` n `6`; index avg `-0.2691` n `26`; metal avg `-0.6093` n `20`; unknown avg `-0.1889` n `788`
- 24h: commodity avg `0.2698` n `12`; crypto_alt avg `-4.7373` n `233`; crypto_major avg `-3.7136` n `8`; equity avg `-1.9036` n `135`; fx avg `0.0894` n `6`; index avg `-0.3201` n `26`; metal avg `-0.9594` n `20`; unknown avg `-0.6338` n `672`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
