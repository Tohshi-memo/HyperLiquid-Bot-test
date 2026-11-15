# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T08:07:23.698616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4436` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0253` n `13`; crypto_alt avg `0.0584` n `239`; crypto_major avg `0.287` n `8`; equity avg `0.0708` n `162`; fx avg `0.0036` n `6`; index avg `-0.0183` n `27`; metal avg `0.0049` n `20`; unknown avg `0.2223` n `1241`
- 1h: commodity avg `-0.0585` n `13`; crypto_alt avg `-0.4818` n `239`; crypto_major avg `-0.4606` n `8`; equity avg `-0.0563` n `162`; fx avg `-0.0026` n `6`; index avg `0.0017` n `27`; metal avg `0.0071` n `20`; unknown avg `0.6779` n `1245`
- 4h: commodity avg `-0.0196` n `13`; crypto_alt avg `-0.8972` n `239`; crypto_major avg `-1.473` n `8`; equity avg `-0.3316` n `162`; fx avg `-0.0012` n `6`; index avg `-0.0294` n `27`; metal avg `-0.0059` n `20`; unknown avg `0.7025` n `1217`
- 24h: commodity avg `-0.0167` n `13`; crypto_alt avg `-5.6701` n `239`; crypto_major avg `-5.3133` n `8`; equity avg `-1.0988` n `162`; fx avg `0.0439` n `6`; index avg `-0.1024` n `27`; metal avg `-0.4334` n `20`; unknown avg `47.1941` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
