# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T19:22:23.136515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4829` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0045` n `13`; crypto_alt avg `-0.4319` n `239`; crypto_major avg `-0.4184` n `8`; equity avg `-0.0998` n `162`; fx avg `0.0026` n `6`; index avg `-0.0133` n `27`; metal avg `-0.0075` n `20`; unknown avg `4.8599` n `1260`
- 1h: commodity avg `-0.0067` n `13`; crypto_alt avg `-0.3013` n `239`; crypto_major avg `-0.3073` n `8`; equity avg `-0.0352` n `162`; fx avg `-0.0019` n `6`; index avg `0.0004` n `27`; metal avg `-0.0182` n `20`; unknown avg `10.0318` n `1260`
- 4h: commodity avg `-0.0424` n `13`; crypto_alt avg `-1.7648` n `239`; crypto_major avg `-1.534` n `8`; equity avg `-0.4977` n `162`; fx avg `0.0154` n `6`; index avg `-0.0511` n `27`; metal avg `-0.1156` n `20`; unknown avg `166.8334` n `1254`
- 24h: commodity avg `0.0075` n `13`; crypto_alt avg `-7.4679` n `239`; crypto_major avg `-7.0343` n `8`; equity avg `-2.1606` n `162`; fx avg `-0.0256` n `6`; index avg `-0.1874` n `27`; metal avg `-0.296` n `20`; unknown avg `3.0419` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
