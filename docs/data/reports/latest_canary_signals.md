# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T05:22:25.292926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.1739` n `229`; crypto_major avg `-0.1816` n `8`; equity avg `-0.0124` n `88`; fx avg `0.0` n `6`; index avg `-0.0264` n `25`; metal avg `-0.0106` n `20`; unknown avg `0.1088` n `765`
- 1h: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.0643` n `229`; crypto_major avg `-0.1197` n `8`; equity avg `0.0108` n `88`; fx avg `0.0037` n `6`; index avg `-0.0115` n `25`; metal avg `-0.0058` n `20`; unknown avg `1.7495` n `765`
- 4h: commodity avg `-0.0465` n `12`; crypto_alt avg `0.0416` n `229`; crypto_major avg `0.2735` n `8`; equity avg `0.1577` n `88`; fx avg `0.0104` n `6`; index avg `0.014` n `25`; metal avg `0.0259` n `20`; unknown avg `1.052` n `763`
- 24h: commodity avg `-0.1205` n `12`; crypto_alt avg `2.3918` n `229`; crypto_major avg `2.8616` n `8`; equity avg `0.5352` n `88`; fx avg `-0.1941` n `6`; index avg `0.0375` n `25`; metal avg `-0.0703` n `20`; unknown avg `4.1021` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
