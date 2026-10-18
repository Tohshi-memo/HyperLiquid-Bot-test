# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T15:37:26.798786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3985` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0062` n `13`; crypto_alt avg `-0.1376` n `237`; crypto_major avg `-0.1959` n `8`; equity avg `-0.0629` n `151`; fx avg `0.0015` n `6`; index avg `-0.0313` n `26`; metal avg `-0.0042` n `20`; unknown avg `0.1266` n `1194`
- 1h: commodity avg `-0.0013` n `13`; crypto_alt avg `-0.0865` n `237`; crypto_major avg `-0.1382` n `8`; equity avg `-0.0915` n `151`; fx avg `0.0096` n `6`; index avg `-0.0463` n `26`; metal avg `0.0019` n `20`; unknown avg `-0.4761` n `1191`
- 4h: commodity avg `0.0081` n `13`; crypto_alt avg `-1.363` n `237`; crypto_major avg `-1.5332` n `8`; equity avg `-0.5792` n `151`; fx avg `0.001` n `6`; index avg `-0.1347` n `26`; metal avg `-0.0528` n `20`; unknown avg `-0.4717` n `1183`
- 24h: commodity avg `-0.0536` n `13`; crypto_alt avg `-3.0309` n `236`; crypto_major avg `-1.2588` n `8`; equity avg `-0.8879` n `151`; fx avg `-0.0162` n `6`; index avg `-0.1553` n `26`; metal avg `-0.0676` n `20`; unknown avg `-0.0154` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2107`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1403`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1298`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1096`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0804`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
