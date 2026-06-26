# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T18:37:27.635158+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0337` n `12`; crypto_alt avg `-0.345` n `228`; crypto_major avg `-0.3833` n `8`; equity avg `-0.2538` n `86`; fx avg `-0.0044` n `6`; index avg `-0.0311` n `23`; metal avg `-0.0063` n `20`; unknown avg `0.0346` n `766`
- 1h: commodity avg `-0.1584` n `12`; crypto_alt avg `-0.2528` n `228`; crypto_major avg `-0.1033` n `8`; equity avg `-0.4579` n `86`; fx avg `0.0019` n `6`; index avg `-0.0966` n `23`; metal avg `-0.0593` n `20`; unknown avg `-0.1647` n `765`
- 4h: commodity avg `-0.1437` n `12`; crypto_alt avg `1.4024` n `228`; crypto_major avg `1.0981` n `8`; equity avg `0.0633` n `86`; fx avg `-0.0466` n `6`; index avg `0.0063` n `23`; metal avg `-0.0279` n `20`; unknown avg `-0.0524` n `765`
- 24h: commodity avg `-0.5891` n `12`; crypto_alt avg `2.4993` n `228`; crypto_major avg `2.3099` n `8`; equity avg `-0.7117` n `86`; fx avg `-0.0766` n `6`; index avg `-0.295` n `23`; metal avg `0.5019` n `20`; unknown avg `0.2561` n `701`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2128`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
