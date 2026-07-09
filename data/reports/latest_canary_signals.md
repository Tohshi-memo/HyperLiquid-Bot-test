# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T06:22:26.444671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0724` n `12`; crypto_alt avg `0.0873` n `229`; crypto_major avg `0.1256` n `8`; equity avg `0.1645` n `91`; fx avg `0.0249` n `6`; index avg `0.0212` n `25`; metal avg `0.1398` n `20`; unknown avg `0.1391` n `764`
- 1h: commodity avg `-0.2491` n `12`; crypto_alt avg `0.4822` n `229`; crypto_major avg `0.546` n `8`; equity avg `0.3135` n `91`; fx avg `0.0541` n `6`; index avg `0.0557` n `25`; metal avg `0.4206` n `20`; unknown avg `0.1543` n `748`
- 4h: commodity avg `-0.2357` n `12`; crypto_alt avg `0.6369` n `229`; crypto_major avg `0.7072` n `8`; equity avg `-0.1064` n `91`; fx avg `0.0377` n `6`; index avg `-0.0503` n `25`; metal avg `0.2185` n `20`; unknown avg `0.0242` n `748`
- 24h: commodity avg `-0.0612` n `12`; crypto_alt avg `0.7675` n `229`; crypto_major avg `0.5238` n `8`; equity avg `1.4114` n `91`; fx avg `0.1302` n `6`; index avg `0.1212` n `25`; metal avg `-0.7071` n `20`; unknown avg `0.268` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
