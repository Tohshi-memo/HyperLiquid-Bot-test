# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T23:52:23.941924+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4354` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0026` n `13`; crypto_alt avg `0.1589` n `239`; crypto_major avg `0.1471` n `8`; equity avg `0.035` n `162`; fx avg `-0.0127` n `6`; index avg `0.1062` n `27`; metal avg `0.0019` n `20`; unknown avg `0.278` n `1262`
- 1h: commodity avg `0.0073` n `13`; crypto_alt avg `0.0319` n `239`; crypto_major avg `-0.2225` n `8`; equity avg `-0.1581` n `162`; fx avg `-0.0142` n `6`; index avg `0.1034` n `27`; metal avg `-0.0026` n `20`; unknown avg `28.5186` n `1256`
- 4h: commodity avg `0.0621` n `13`; crypto_alt avg `-1.1162` n `239`; crypto_major avg `-1.3576` n `8`; equity avg `-0.7484` n `162`; fx avg `-0.0253` n `6`; index avg `0.0778` n `27`; metal avg `0.0083` n `20`; unknown avg `3.4766` n `1162`
- 24h: commodity avg `-0.3212` n `13`; crypto_alt avg `-1.4183` n `239`; crypto_major avg `-3.0897` n `8`; equity avg `-3.976` n `162`; fx avg `-0.0784` n `6`; index avg `-0.1961` n `27`; metal avg `-0.365` n `20`; unknown avg `60.4158` n `1035`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
