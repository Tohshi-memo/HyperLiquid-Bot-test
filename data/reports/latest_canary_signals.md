# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T18:22:25.950749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.112` n `12`; crypto_alt avg `-0.038` n `229`; crypto_major avg `-0.0813` n `8`; equity avg `-0.1049` n `91`; fx avg `-0.0147` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0545` n `20`; unknown avg `0.3437` n `765`
- 1h: commodity avg `0.0423` n `12`; crypto_alt avg `0.4989` n `229`; crypto_major avg `0.481` n `8`; equity avg `-0.0464` n `91`; fx avg `-0.0217` n `6`; index avg `0.0147` n `25`; metal avg `-0.0199` n `20`; unknown avg `0.3636` n `765`
- 4h: commodity avg `-0.4024` n `12`; crypto_alt avg `0.4391` n `229`; crypto_major avg `0.6515` n `8`; equity avg `0.9732` n `91`; fx avg `-0.0217` n `6`; index avg `0.2273` n `25`; metal avg `0.0979` n `20`; unknown avg `0.1782` n `765`
- 24h: commodity avg `-0.8865` n `12`; crypto_alt avg `1.4538` n `229`; crypto_major avg `0.9001` n `8`; equity avg `2.4899` n `91`; fx avg `0.0462` n `6`; index avg `0.4044` n `25`; metal avg `0.8541` n `20`; unknown avg `1.0493` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
