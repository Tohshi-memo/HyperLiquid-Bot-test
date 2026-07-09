# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T23:52:28.067867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `0.027` n `229`; crypto_major avg `0.0523` n `8`; equity avg `-0.0143` n `91`; fx avg `-0.0063` n `6`; index avg `0.002` n `25`; metal avg `0.0012` n `20`; unknown avg `0.04` n `765`
- 1h: commodity avg `0.0234` n `12`; crypto_alt avg `-0.152` n `229`; crypto_major avg `-0.1466` n `8`; equity avg `0.0833` n `91`; fx avg `-0.0011` n `6`; index avg `-0.0039` n `25`; metal avg `0.0146` n `20`; unknown avg `-0.0535` n `765`
- 4h: commodity avg `0.009` n `12`; crypto_alt avg `-0.2214` n `229`; crypto_major avg `-0.1188` n `8`; equity avg `0.2782` n `91`; fx avg `0.0071` n `6`; index avg `0.0258` n `25`; metal avg `0.036` n `20`; unknown avg `-0.4677` n `765`
- 24h: commodity avg `-1.0991` n `12`; crypto_alt avg `0.7376` n `229`; crypto_major avg `0.2583` n `8`; equity avg `1.4762` n `91`; fx avg `0.0615` n `6`; index avg `0.3379` n `25`; metal avg `0.613` n `20`; unknown avg `-0.2109` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
