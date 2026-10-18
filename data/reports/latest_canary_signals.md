# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T13:37:26.104914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.044` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0248` n `13`; crypto_alt avg `-0.7722` n `237`; crypto_major avg `-0.7876` n `8`; equity avg `-0.1866` n `151`; fx avg `0.01` n `6`; index avg `-0.0287` n `26`; metal avg `-0.0228` n `20`; unknown avg `0.2826` n `1191`
- 1h: commodity avg `0.0112` n `13`; crypto_alt avg `-0.757` n `237`; crypto_major avg `-0.9627` n `8`; equity avg `-0.3468` n `151`; fx avg `0.0006` n `6`; index avg `-0.0516` n `26`; metal avg `-0.0198` n `20`; unknown avg `-0.018` n `1189`
- 4h: commodity avg `0.0336` n `13`; crypto_alt avg `-0.7264` n `237`; crypto_major avg `-1.1058` n `8`; equity avg `-0.4071` n `151`; fx avg `0.01` n `6`; index avg `-0.0618` n `26`; metal avg `-0.0156` n `20`; unknown avg `3.9888` n `1183`
- 24h: commodity avg `0.0731` n `13`; crypto_alt avg `-2.2856` n `236`; crypto_major avg `-0.8185` n `8`; equity avg `-0.8027` n `151`; fx avg `-0.0364` n `6`; index avg `-0.1055` n `26`; metal avg `-0.055` n `20`; unknown avg `1.3933` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2078`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1383`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1286`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1091`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0815`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
