# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T14:52:29.993271+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3978` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0113` n `13`; crypto_alt avg `0.0981` n `237`; crypto_major avg `-0.0591` n `8`; equity avg `-0.0072` n `151`; fx avg `0.0069` n `6`; index avg `-0.0115` n `26`; metal avg `0.006` n `20`; unknown avg `-0.0938` n `1193`
- 1h: commodity avg `-0.003` n `13`; crypto_alt avg `-0.7522` n `237`; crypto_major avg `-0.6471` n `8`; equity avg `-0.1751` n `151`; fx avg `0.0036` n `6`; index avg `-0.0352` n `26`; metal avg `-0.0204` n `20`; unknown avg `-0.2696` n `1191`
- 4h: commodity avg `0.0507` n `13`; crypto_alt avg `-1.0868` n `237`; crypto_major avg `-1.5053` n `8`; equity avg `-0.5244` n `151`; fx avg `0.0112` n `6`; index avg `-0.1075` n `26`; metal avg `-0.0443` n `20`; unknown avg `-0.0666` n `1183`
- 24h: commodity avg `0.0296` n `13`; crypto_alt avg `-3.5147` n `236`; crypto_major avg `-1.6378` n `8`; equity avg `-1.017` n `151`; fx avg `-0.0332` n `6`; index avg `-0.1352` n `26`; metal avg `-0.0712` n `20`; unknown avg `0.7091` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2095`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1392`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1264`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0797`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
