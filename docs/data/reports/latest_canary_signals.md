# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T00:37:25.389471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `-0.0769` n `229`; crypto_major avg `-0.0733` n `8`; equity avg `-0.0692` n `91`; fx avg `0.0048` n `6`; index avg `-0.0101` n `25`; metal avg `-0.0178` n `20`; unknown avg `-0.2263` n `765`
- 1h: commodity avg `0.006` n `12`; crypto_alt avg `-0.1361` n `229`; crypto_major avg `-0.1053` n `8`; equity avg `-0.5572` n `91`; fx avg `0.0487` n `6`; index avg `-0.1548` n `25`; metal avg `-0.0486` n `20`; unknown avg `-0.3252` n `765`
- 4h: commodity avg `0.0288` n `12`; crypto_alt avg `-0.4405` n `229`; crypto_major avg `-0.4219` n `8`; equity avg `-0.3534` n `91`; fx avg `0.0671` n `6`; index avg `-0.1438` n `25`; metal avg `-0.0261` n `20`; unknown avg `-0.4841` n `765`
- 24h: commodity avg `-1.0717` n `12`; crypto_alt avg `0.6051` n `229`; crypto_major avg `0.1723` n `8`; equity avg `0.7843` n `91`; fx avg `0.14` n `6`; index avg `0.1534` n `25`; metal avg `0.5523` n `20`; unknown avg `-0.263` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
