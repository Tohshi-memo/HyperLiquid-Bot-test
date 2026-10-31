# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T14:07:27.752099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `13`; crypto_alt avg `-0.1` n `238`; crypto_major avg `-0.2086` n `8`; equity avg `0.0192` n `156`; fx avg `-0.005` n `6`; index avg `0.003` n `27`; metal avg `0.0001` n `20`; unknown avg `129.6794` n `1256`
- 1h: commodity avg `-0.0255` n `13`; crypto_alt avg `0.0854` n `238`; crypto_major avg `-0.2384` n `8`; equity avg `0.0142` n `156`; fx avg `0.0025` n `6`; index avg `-0.0049` n `27`; metal avg `0.0013` n `20`; unknown avg `0.0274` n `1254`
- 4h: commodity avg `-0.0352` n `13`; crypto_alt avg `0.3684` n `238`; crypto_major avg `0.1325` n `8`; equity avg `-0.0596` n `156`; fx avg `-0.0017` n `6`; index avg `-0.0193` n `27`; metal avg `0.0073` n `20`; unknown avg `16.4798` n `1218`
- 24h: commodity avg `-0.3361` n `13`; crypto_alt avg `1.0448` n `238`; crypto_major avg `-0.0204` n `8`; equity avg `-1.2372` n `156`; fx avg `0.0528` n `6`; index avg `-0.136` n `27`; metal avg `-0.0181` n `20`; unknown avg `3.4253` n `1045`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
