# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T20:22:32.366673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0319` n `13`; crypto_alt avg `0.1655` n `235`; crypto_major avg `0.1911` n `8`; equity avg `0.0279` n `150`; fx avg `0.0064` n `6`; index avg `-0.0045` n `26`; metal avg `0.0307` n `20`; unknown avg `0.1087` n `1077`
- 1h: commodity avg `0.0449` n `13`; crypto_alt avg `0.1312` n `235`; crypto_major avg `-0.0123` n `8`; equity avg `0.0905` n `150`; fx avg `0.0084` n `6`; index avg `0.0098` n `26`; metal avg `0.0082` n `20`; unknown avg `2.1818` n `1049`
- 4h: commodity avg `0.0208` n `13`; crypto_alt avg `0.1433` n `235`; crypto_major avg `-0.3122` n `8`; equity avg `0.0519` n `150`; fx avg `0.0102` n `6`; index avg `0.0086` n `26`; metal avg `-0.0997` n `20`; unknown avg `2.7299` n `1048`
- 24h: commodity avg `0.3532` n `13`; crypto_alt avg `-4.3488` n `235`; crypto_major avg `-3.3593` n `8`; equity avg `-1.363` n `150`; fx avg `-0.1537` n `6`; index avg `-0.212` n `26`; metal avg `-0.6984` n `20`; unknown avg `1.0535` n `970`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
