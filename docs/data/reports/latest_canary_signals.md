# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T17:07:27.366466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `0.1697` n `229`; crypto_major avg `0.2229` n `8`; equity avg `0.0421` n `91`; fx avg `-0.0002` n `6`; index avg `0.0175` n `25`; metal avg `-0.0782` n `20`; unknown avg `0.0447` n `765`
- 1h: commodity avg `-0.0826` n `12`; crypto_alt avg `-0.1104` n `229`; crypto_major avg `-0.0598` n `8`; equity avg `-0.1543` n `91`; fx avg `0.0021` n `6`; index avg `0.008` n `25`; metal avg `-0.0616` n `20`; unknown avg `-0.1268` n `765`
- 4h: commodity avg `-0.9597` n `12`; crypto_alt avg `-0.1656` n `229`; crypto_major avg `0.1152` n `8`; equity avg `0.5753` n `91`; fx avg `-0.0127` n `6`; index avg `0.1494` n `25`; metal avg `0.2` n `20`; unknown avg `-0.0235` n `765`
- 24h: commodity avg `-1.1052` n `12`; crypto_alt avg `0.7959` n `229`; crypto_major avg `0.4839` n `8`; equity avg `2.6966` n `91`; fx avg `0.0459` n `6`; index avg `0.3917` n `25`; metal avg `0.9725` n `20`; unknown avg `0.9511` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
