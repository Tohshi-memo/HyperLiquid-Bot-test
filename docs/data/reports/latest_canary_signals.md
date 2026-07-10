# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T00:22:28.659211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0233` n `12`; crypto_alt avg `-0.0373` n `229`; crypto_major avg `0.0351` n `8`; equity avg `-0.2109` n `91`; fx avg `0.0436` n `6`; index avg `-0.0551` n `25`; metal avg `0.0038` n `20`; unknown avg `-0.0582` n `765`
- 1h: commodity avg `0.0175` n `12`; crypto_alt avg `-0.0182` n `229`; crypto_major avg `-0.0019` n `8`; equity avg `-0.4638` n `91`; fx avg `0.0534` n `6`; index avg `-0.14` n `25`; metal avg `-0.0354` n `20`; unknown avg `-0.1067` n `765`
- 4h: commodity avg `0.0146` n `12`; crypto_alt avg `-0.2908` n `229`; crypto_major avg `-0.2213` n `8`; equity avg `-0.2416` n `91`; fx avg `0.0623` n `6`; index avg `-0.1326` n `25`; metal avg `0.0123` n `20`; unknown avg `-0.4675` n `765`
- 24h: commodity avg `-1.0645` n `12`; crypto_alt avg `0.6846` n `229`; crypto_major avg `0.4154` n `8`; equity avg `0.7909` n `91`; fx avg `0.1332` n `6`; index avg `0.1468` n `25`; metal avg `0.5852` n `20`; unknown avg `-0.2147` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
