# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T05:07:33.137452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `-0.1549` n `229`; crypto_major avg `-0.3288` n `8`; equity avg `-0.0706` n `88`; fx avg `0.0` n `6`; index avg `0.0081` n `25`; metal avg `-0.0012` n `20`; unknown avg `0.1862` n `765`
- 1h: commodity avg `-0.0306` n `12`; crypto_alt avg `-0.135` n `229`; crypto_major avg `0.0004` n `8`; equity avg `-0.0114` n `88`; fx avg `0.0073` n `6`; index avg `0.0141` n `25`; metal avg `0.0088` n `20`; unknown avg `1.3052` n `765`
- 4h: commodity avg `-0.0861` n `12`; crypto_alt avg `0.3901` n `229`; crypto_major avg `0.5012` n `8`; equity avg `0.1953` n `88`; fx avg `-0.0125` n `6`; index avg `0.0412` n `25`; metal avg `0.0176` n `20`; unknown avg `3.967` n `763`
- 24h: commodity avg `-0.1009` n `12`; crypto_alt avg `2.4752` n `229`; crypto_major avg `3.1604` n `8`; equity avg `0.5175` n `88`; fx avg `-0.1717` n `6`; index avg `0.0553` n `25`; metal avg `-0.1343` n `20`; unknown avg `4.37` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
