# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T17:38:14.920541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0966` n `12`; crypto_alt avg `0.0243` n `229`; crypto_major avg `-0.0137` n `8`; equity avg `-0.0405` n `91`; fx avg `-0.0092` n `6`; index avg `0.0029` n `25`; metal avg `0.0478` n `20`; unknown avg `-0.1195` n `765`
- 1h: commodity avg `-0.148` n `12`; crypto_alt avg `0.128` n `229`; crypto_major avg `0.0824` n `8`; equity avg `0.2743` n `91`; fx avg `0.0054` n `6`; index avg `0.0776` n `25`; metal avg `-0.0562` n `20`; unknown avg `-0.0998` n `765`
- 4h: commodity avg `-0.696` n `12`; crypto_alt avg `0.0022` n `229`; crypto_major avg `0.0376` n `8`; equity avg `0.3925` n `91`; fx avg `-0.0013` n `6`; index avg `0.0819` n `25`; metal avg `0.1325` n `20`; unknown avg `-0.1922` n `765`
- 24h: commodity avg `-1.1132` n `12`; crypto_alt avg `0.6464` n `229`; crypto_major avg `0.0723` n `8`; equity avg `2.4719` n `91`; fx avg `0.0461` n `6`; index avg `0.3656` n `25`; metal avg `0.9475` n `20`; unknown avg `0.834` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
