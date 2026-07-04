# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T04:07:25.353660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `0.1445` n `229`; crypto_major avg `0.1616` n `8`; equity avg `0.0518` n `88`; fx avg `-0.0016` n `6`; index avg `-0.0` n `25`; metal avg `0.0076` n `20`; unknown avg `0.1866` n `765`
- 1h: commodity avg `-0.0013` n `12`; crypto_alt avg `0.3477` n `229`; crypto_major avg `0.6165` n `8`; equity avg `0.0538` n `88`; fx avg `0.0184` n `6`; index avg `0.0142` n `25`; metal avg `0.0075` n `20`; unknown avg `3.8656` n `765`
- 4h: commodity avg `-0.0186` n `12`; crypto_alt avg `-0.2877` n `229`; crypto_major avg `0.0735` n `8`; equity avg `0.2231` n `88`; fx avg `0.0009` n `6`; index avg `-0.0091` n `25`; metal avg `-0.0314` n `20`; unknown avg `0.01` n `763`
- 24h: commodity avg `-0.0503` n `12`; crypto_alt avg `2.6209` n `229`; crypto_major avg `3.2924` n `8`; equity avg `0.7328` n `88`; fx avg `-0.1701` n `6`; index avg `0.1254` n `25`; metal avg `-0.0904` n `20`; unknown avg `4.3441` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
