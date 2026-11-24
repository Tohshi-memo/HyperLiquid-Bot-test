# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T00:22:28.030885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `13`; crypto_alt avg `0.3351` n `239`; crypto_major avg `0.1925` n `8`; equity avg `0.1284` n `166`; fx avg `0.0121` n `6`; index avg `0.1119` n `27`; metal avg `0.1076` n `20`; unknown avg `0.0987` n `1264`
- 1h: commodity avg `0.0378` n `13`; crypto_alt avg `0.4965` n `239`; crypto_major avg `-0.0073` n `8`; equity avg `-0.1209` n `166`; fx avg `-0.0153` n `6`; index avg `0.0766` n `27`; metal avg `0.0952` n `20`; unknown avg `633.6839` n `1258`
- 4h: commodity avg `0.1551` n `13`; crypto_alt avg `-0.3291` n `239`; crypto_major avg `-0.6323` n `8`; equity avg `0.2165` n `166`; fx avg `-0.0104` n `6`; index avg `0.1197` n `27`; metal avg `0.069` n `20`; unknown avg `163.7922` n `1218`
- 24h: commodity avg `-1.0247` n `13`; crypto_alt avg `1.2468` n `239`; crypto_major avg `0.8804` n `8`; equity avg `5.5911` n `166`; fx avg `-0.1645` n `6`; index avg `0.5827` n `27`; metal avg `0.4284` n `20`; unknown avg `288.3247` n `1047`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
