# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T22:07:25.943144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0026` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0184` n `13`; crypto_alt avg `0.2674` n `236`; crypto_major avg `0.152` n `8`; equity avg `0.0581` n `151`; fx avg `-0.0007` n `6`; index avg `0.0141` n `26`; metal avg `0.0149` n `20`; unknown avg `0.4659` n `1191`
- 1h: commodity avg `0.0148` n `13`; crypto_alt avg `-1.4601` n `236`; crypto_major avg `-1.1267` n `8`; equity avg `-0.9871` n `151`; fx avg `-0.0023` n `6`; index avg `-0.1241` n `26`; metal avg `-0.0745` n `20`; unknown avg `0.7113` n `1191`
- 4h: commodity avg `-0.0158` n `13`; crypto_alt avg `-0.7573` n `236`; crypto_major avg `-0.6678` n `8`; equity avg `-0.9635` n `151`; fx avg `0.0021` n `6`; index avg `-0.1072` n `26`; metal avg `-0.0647` n `20`; unknown avg `1.2508` n `1131`
- 24h: commodity avg `0.0158` n `13`; crypto_alt avg `-2.5734` n `236`; crypto_major avg `-1.463` n `8`; equity avg `-0.9639` n `151`; fx avg `-0.0293` n `6`; index avg `-0.1339` n `26`; metal avg `-0.1199` n `20`; unknown avg `5.2502` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1672`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1366`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1064`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0725`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
