# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T11:51:03.057631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0432` n `12`; crypto_alt avg `-0.2156` n `231`; crypto_major avg `-0.2749` n `8`; equity avg `-0.112` n `122`; fx avg `-0.0022` n `6`; index avg `-0.0197` n `25`; metal avg `-0.1287` n `20`; unknown avg `0.0204` n `793`
- 1h: commodity avg `0.1196` n `12`; crypto_alt avg `0.7751` n `231`; crypto_major avg `0.8161` n `8`; equity avg `0.128` n `122`; fx avg `-0.0005` n `6`; index avg `0.0393` n `25`; metal avg `0.0174` n `20`; unknown avg `0.1569` n `793`
- 4h: commodity avg `0.173` n `12`; crypto_alt avg `0.8639` n `231`; crypto_major avg `0.7185` n `8`; equity avg `0.2016` n `122`; fx avg `-0.0019` n `6`; index avg `0.0496` n `25`; metal avg `0.0328` n `20`; unknown avg `0.548` n `793`
- 24h: commodity avg `-0.0269` n `12`; crypto_alt avg `1.2752` n `231`; crypto_major avg `0.3396` n `8`; equity avg `-1.402` n `122`; fx avg `-0.1175` n `6`; index avg `-0.1178` n `25`; metal avg `0.1377` n `20`; unknown avg `4.8686` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
