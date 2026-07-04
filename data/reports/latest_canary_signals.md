# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T11:52:25.267974+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `12`; crypto_alt avg `-0.0197` n `229`; crypto_major avg `-0.0532` n `8`; equity avg `-0.0238` n `88`; fx avg `-0.0094` n `6`; index avg `-0.0001` n `25`; metal avg `-0.0061` n `20`; unknown avg `-0.0182` n `765`
- 1h: commodity avg `0.0194` n `12`; crypto_alt avg `0.3542` n `229`; crypto_major avg `0.0041` n `8`; equity avg `-0.0684` n `88`; fx avg `0.0192` n `6`; index avg `-0.0052` n `25`; metal avg `0.0059` n `20`; unknown avg `-0.0066` n `765`
- 4h: commodity avg `0.1211` n `12`; crypto_alt avg `0.2761` n `229`; crypto_major avg `-0.2335` n `8`; equity avg `-0.0198` n `88`; fx avg `-0.0074` n `6`; index avg `0.027` n `25`; metal avg `0.0223` n `20`; unknown avg `0.2005` n `765`
- 24h: commodity avg `0.1534` n `12`; crypto_alt avg `0.8813` n `229`; crypto_major avg `1.0812` n `8`; equity avg `0.1252` n `88`; fx avg `-0.0806` n `6`; index avg `-0.0291` n `25`; metal avg `-0.0695` n `20`; unknown avg `2.8928` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
