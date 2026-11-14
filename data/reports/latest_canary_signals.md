# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T19:27:36.003746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.207` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0047` n `13`; crypto_alt avg `-0.1779` n `239`; crypto_major avg `-0.1376` n `8`; equity avg `-0.0363` n `162`; fx avg `0.0046` n `6`; index avg `-0.0126` n `27`; metal avg `-0.0075` n `20`; unknown avg `2.9152` n `1258`
- 1h: commodity avg `-0.0065` n `13`; crypto_alt avg `-0.0466` n `239`; crypto_major avg `-0.0261` n `8`; equity avg `0.0284` n `162`; fx avg `0.0002` n `6`; index avg `0.0011` n `27`; metal avg `-0.0182` n `20`; unknown avg `8.6007` n `1258`
- 4h: commodity avg `-0.0422` n `13`; crypto_alt avg `-1.515` n `239`; crypto_major avg `-1.2575` n `8`; equity avg `-0.4349` n `162`; fx avg `0.0175` n `6`; index avg `-0.0505` n `27`; metal avg `-0.1156` n `20`; unknown avg `6.0409` n `1252`
- 24h: commodity avg `0.0077` n `13`; crypto_alt avg `-7.237` n `239`; crypto_major avg `-6.7761` n `8`; equity avg `-2.0998` n `162`; fx avg `-0.0235` n `6`; index avg `-0.1868` n `27`; metal avg `-0.296` n `20`; unknown avg `1.6741` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
