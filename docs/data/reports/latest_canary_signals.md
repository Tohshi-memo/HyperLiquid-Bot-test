# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T19:52:29.255829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `-0.0392` n `229`; crypto_major avg `-0.0131` n `8`; equity avg `-0.003` n `88`; fx avg `-0.0071` n `6`; index avg `0.0137` n `25`; metal avg `-0.0168` n `20`; unknown avg `-0.0444` n `765`
- 1h: commodity avg `-0.0014` n `12`; crypto_alt avg `-0.1769` n `229`; crypto_major avg `-0.2528` n `8`; equity avg `0.0696` n `88`; fx avg `-0.0454` n `6`; index avg `0.0244` n `25`; metal avg `0.0303` n `20`; unknown avg `-0.4288` n `765`
- 4h: commodity avg `-0.0396` n `12`; crypto_alt avg `0.0097` n `229`; crypto_major avg `-0.0957` n `8`; equity avg `0.0052` n `88`; fx avg `-0.0528` n `6`; index avg `-0.006` n `25`; metal avg `0.0191` n `20`; unknown avg `-0.7598` n `765`
- 24h: commodity avg `-0.011` n `12`; crypto_alt avg `0.9548` n `229`; crypto_major avg `1.0765` n `8`; equity avg `0.2326` n `88`; fx avg `-0.0579` n `6`; index avg `-0.0485` n `25`; metal avg `0.0675` n `20`; unknown avg `-0.1893` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
