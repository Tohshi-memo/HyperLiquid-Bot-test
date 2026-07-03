# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T16:37:25.848715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0253` n `12`; crypto_alt avg `0.0203` n `229`; crypto_major avg `-0.1531` n `8`; equity avg `-0.015` n `88`; fx avg `-0.0006` n `6`; index avg `0.0319` n `25`; metal avg `0.0069` n `20`; unknown avg `-0.0087` n `765`
- 1h: commodity avg `0.0096` n `12`; crypto_alt avg `-0.1075` n `229`; crypto_major avg `-0.1243` n `8`; equity avg `0.0332` n `88`; fx avg `-0.004` n `6`; index avg `0.028` n `25`; metal avg `-0.0357` n `20`; unknown avg `0.4957` n `765`
- 4h: commodity avg `0.106` n `12`; crypto_alt avg `0.3711` n `229`; crypto_major avg `0.5351` n `8`; equity avg `-0.0663` n `88`; fx avg `-0.0198` n `6`; index avg `0.0206` n `25`; metal avg `-0.0453` n `20`; unknown avg `1.447` n `765`
- 24h: commodity avg `0.2961` n `12`; crypto_alt avg `2.6956` n `229`; crypto_major avg `2.4147` n `8`; equity avg `2.2221` n `88`; fx avg `-0.0567` n `6`; index avg `0.6046` n `25`; metal avg `0.7323` n `20`; unknown avg `7.8568` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
