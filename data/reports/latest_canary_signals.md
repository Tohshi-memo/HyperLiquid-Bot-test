# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T18:52:25.373647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0199` n `12`; crypto_alt avg `-0.0361` n `229`; crypto_major avg `-0.1397` n `8`; equity avg `0.038` n `91`; fx avg `-0.0053` n `6`; index avg `-0.0037` n `25`; metal avg `0.007` n `20`; unknown avg `0.0098` n `765`
- 1h: commodity avg `0.0908` n `12`; crypto_alt avg `0.1789` n `229`; crypto_major avg `0.0739` n `8`; equity avg `-0.0966` n `91`; fx avg `-0.027` n `6`; index avg `-0.01` n `25`; metal avg `-0.1571` n `20`; unknown avg `0.0274` n `765`
- 4h: commodity avg `-0.3622` n `12`; crypto_alt avg `0.3533` n `229`; crypto_major avg `0.3249` n `8`; equity avg `0.5322` n `91`; fx avg `-0.0139` n `6`; index avg `0.1428` n `25`; metal avg `-0.0311` n `20`; unknown avg `0.0749` n `765`
- 24h: commodity avg `-0.9844` n `12`; crypto_alt avg `1.2882` n `229`; crypto_major avg `0.7898` n `8`; equity avg `2.4216` n `91`; fx avg `0.0383` n `6`; index avg `0.391` n `25`; metal avg `0.6586` n `20`; unknown avg `1.1055` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
