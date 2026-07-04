# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T10:52:25.362000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `0.1323` n `229`; crypto_major avg `0.0761` n `8`; equity avg `-0.0004` n `88`; fx avg `-0.0223` n `6`; index avg `0.0014` n `25`; metal avg `-0.0024` n `20`; unknown avg `-0.0001` n `765`
- 1h: commodity avg `0.0359` n `12`; crypto_alt avg `0.2325` n `229`; crypto_major avg `-0.0171` n `8`; equity avg `0.0241` n `88`; fx avg `-0.0325` n `6`; index avg `0.0065` n `25`; metal avg `-0.0018` n `20`; unknown avg `-0.0266` n `765`
- 4h: commodity avg `0.1042` n `12`; crypto_alt avg `-0.1876` n `229`; crypto_major avg `-0.1183` n `8`; equity avg `0.0169` n `88`; fx avg `-0.0263` n `6`; index avg `-0.001` n `25`; metal avg `0.011` n `20`; unknown avg `0.485` n `765`
- 24h: commodity avg `0.0925` n `12`; crypto_alt avg `0.6336` n `229`; crypto_major avg `1.1652` n `8`; equity avg `0.1428` n `88`; fx avg `-0.0944` n `6`; index avg `-0.0246` n `25`; metal avg `-0.0842` n `20`; unknown avg `3.2058` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
