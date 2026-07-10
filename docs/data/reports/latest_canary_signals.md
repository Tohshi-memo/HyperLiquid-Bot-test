# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T01:07:24.699463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0157` n `12`; crypto_alt avg `0.1002` n `229`; crypto_major avg `0.0748` n `8`; equity avg `0.0549` n `91`; fx avg `-0.0296` n `6`; index avg `0.0271` n `25`; metal avg `0.0154` n `20`; unknown avg `-0.05` n `765`
- 1h: commodity avg `-0.0145` n `12`; crypto_alt avg `-0.0242` n `229`; crypto_major avg `-0.0032` n `8`; equity avg `-0.0045` n `91`; fx avg `-0.013` n `6`; index avg `-0.0101` n `25`; metal avg `0.0478` n `20`; unknown avg `0.0681` n `765`
- 4h: commodity avg `-0.0283` n `12`; crypto_alt avg `-0.399` n `229`; crypto_major avg `-0.43` n `8`; equity avg `-0.123` n `91`; fx avg `-0.0116` n `6`; index avg `-0.0869` n `25`; metal avg `0.0297` n `20`; unknown avg `-0.4309` n `765`
- 24h: commodity avg `-1.048` n `12`; crypto_alt avg `0.7156` n `229`; crypto_major avg `0.0869` n `8`; equity avg `0.949` n `91`; fx avg `0.0508` n `6`; index avg `0.1998` n `25`; metal avg `0.7519` n `20`; unknown avg `-0.2816` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
