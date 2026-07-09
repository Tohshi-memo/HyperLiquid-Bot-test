# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T20:27:24.217232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `0.0568` n `229`; crypto_major avg `0.0456` n `8`; equity avg `-0.0521` n `91`; fx avg `0.0041` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0082` n `20`; unknown avg `-0.0061` n `765`
- 1h: commodity avg `0.0537` n `12`; crypto_alt avg `-0.0034` n `229`; crypto_major avg `0.1463` n `8`; equity avg `-0.255` n `91`; fx avg `-0.0067` n `6`; index avg `0.0019` n `25`; metal avg `-0.02` n `20`; unknown avg `-0.1064` n `765`
- 4h: commodity avg `-0.0744` n `12`; crypto_alt avg `0.4806` n `229`; crypto_major avg `0.4769` n `8`; equity avg `-0.2637` n `91`; fx avg `-0.0312` n `6`; index avg `0.0408` n `25`; metal avg `-0.3591` n `20`; unknown avg `-0.0319` n `765`
- 24h: commodity avg `-1.1889` n `12`; crypto_alt avg `1.2146` n `229`; crypto_major avg `0.6293` n `8`; equity avg `1.7128` n `91`; fx avg `0.0224` n `6`; index avg `0.3883` n `25`; metal avg `0.6292` n `20`; unknown avg `-0.0152` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
