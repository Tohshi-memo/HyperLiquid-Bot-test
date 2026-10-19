# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T09:07:29.713411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1068` n `13`; crypto_alt avg `-0.0486` n `237`; crypto_major avg `-0.0395` n `8`; equity avg `-0.0924` n `151`; fx avg `0.0056` n `6`; index avg `-0.0047` n `26`; metal avg `0.0278` n `20`; unknown avg `-0.02` n `1193`
- 1h: commodity avg `0.2391` n `13`; crypto_alt avg `-0.0233` n `237`; crypto_major avg `0.1523` n `8`; equity avg `-0.1656` n `151`; fx avg `0.0287` n `6`; index avg `-0.0175` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.1047` n `1193`
- 4h: commodity avg `0.1524` n `13`; crypto_alt avg `0.2485` n `237`; crypto_major avg `0.1474` n `8`; equity avg `-0.1326` n `151`; fx avg `-0.0198` n `6`; index avg `-0.0351` n `26`; metal avg `-0.0914` n `20`; unknown avg `0.4642` n `1126`
- 24h: commodity avg `-0.2756` n `13`; crypto_alt avg `0.1529` n `237`; crypto_major avg `0.8462` n `8`; equity avg `2.2552` n `151`; fx avg `-0.0289` n `6`; index avg `0.4357` n `26`; metal avg `0.223` n `20`; unknown avg `1.0702` n `939`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1987`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1444`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1274`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0624`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
