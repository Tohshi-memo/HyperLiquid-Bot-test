# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T22:06:23.344261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0551` n `12`; crypto_alt avg `-0.0225` n `229`; crypto_major avg `-0.0221` n `8`; equity avg `0.0274` n `91`; fx avg `-0.0028` n `6`; index avg `0.0084` n `25`; metal avg `0.0018` n `20`; unknown avg `-0.2217` n `765`
- 1h: commodity avg `-0.0498` n `12`; crypto_alt avg `-0.2148` n `229`; crypto_major avg `-0.1745` n `8`; equity avg `0.0019` n `91`; fx avg `-0.0023` n `6`; index avg `0.0032` n `25`; metal avg `0.0109` n `20`; unknown avg `-0.325` n `765`
- 4h: commodity avg `0.0619` n `12`; crypto_alt avg `-0.366` n `229`; crypto_major avg `-0.3426` n `8`; equity avg `-0.4115` n `91`; fx avg `-0.0244` n `6`; index avg `-0.0265` n `25`; metal avg `-0.2412` n `20`; unknown avg `-0.4604` n `765`
- 24h: commodity avg `-1.1616` n `12`; crypto_alt avg `0.9457` n `229`; crypto_major avg `0.5484` n `8`; equity avg `1.6165` n `91`; fx avg `0.0223` n `6`; index avg `0.3633` n `25`; metal avg `0.6462` n `20`; unknown avg `-0.2083` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
