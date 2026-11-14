# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T03:22:26.225598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `13`; crypto_alt avg `0.0499` n `239`; crypto_major avg `-0.1996` n `8`; equity avg `-0.0074` n `162`; fx avg `-0.0089` n `6`; index avg `0.0017` n `27`; metal avg `-0.0002` n `20`; unknown avg `0.8973` n `1260`
- 1h: commodity avg `0.0071` n `13`; crypto_alt avg `0.311` n `239`; crypto_major avg `-0.1709` n `8`; equity avg `0.0332` n `162`; fx avg `-0.0081` n `6`; index avg `-0.0074` n `27`; metal avg `-0.0141` n `20`; unknown avg `-0.3634` n `1260`
- 4h: commodity avg `0.0713` n `13`; crypto_alt avg `-0.6188` n `239`; crypto_major avg `-0.9982` n `8`; equity avg `-0.1412` n `162`; fx avg `-0.0378` n `6`; index avg `-0.0278` n `27`; metal avg `-0.0272` n `20`; unknown avg `3.6161` n `1252`
- 24h: commodity avg `-0.0904` n `13`; crypto_alt avg `-0.3446` n `239`; crypto_major avg `-1.8887` n `8`; equity avg `-3.1552` n `162`; fx avg `-0.0948` n `6`; index avg `-0.282` n `27`; metal avg `-0.6465` n `20`; unknown avg `61.3673` n `1036`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
