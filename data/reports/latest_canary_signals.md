# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T14:07:26.587424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2007` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0405` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0297` n `13`; crypto_alt avg `-0.6629` n `237`; crypto_major avg `-0.4036` n `8`; equity avg `-0.1138` n `151`; fx avg `0.005` n `6`; index avg `-0.0222` n `26`; metal avg `-0.0108` n `20`; unknown avg `-0.2187` n `1191`
- 1h: commodity avg `0.0527` n `13`; crypto_alt avg `-1.4518` n `237`; crypto_major avg `-1.1093` n `8`; equity avg `-0.3823` n `151`; fx avg `0.0026` n `6`; index avg `-0.0688` n `26`; metal avg `-0.0375` n `20`; unknown avg `-0.5913` n `1189`
- 4h: commodity avg `-0.0111` n `13`; crypto_alt avg `-1.4026` n `237`; crypto_major avg `-1.2992` n `8`; equity avg `-0.4753` n `151`; fx avg `0.011` n `6`; index avg `-0.0985` n `26`; metal avg `-0.0348` n `20`; unknown avg `0.1132` n `1183`
- 24h: commodity avg `-0.0866` n `13`; crypto_alt avg `-3.0224` n `236`; crypto_major avg `-1.1214` n `8`; equity avg `-0.9434` n `151`; fx avg `-0.0349` n `6`; index avg `-0.1213` n `26`; metal avg `-0.0694` n `20`; unknown avg `0.5898` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2068`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1373`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1045`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0811`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
