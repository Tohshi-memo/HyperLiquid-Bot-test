# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T01:52:27.056735+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `0.0725` n `231`; crypto_major avg `0.1112` n `8`; equity avg `0.0205` n `127`; fx avg `-0.0006` n `6`; index avg `0.0008` n `26`; metal avg `0.0111` n `20`; unknown avg `0.052` n `793`
- 1h: commodity avg `-0.0051` n `12`; crypto_alt avg `0.0175` n `231`; crypto_major avg `0.2158` n `8`; equity avg `0.0245` n `127`; fx avg `0.0065` n `6`; index avg `0.0149` n `26`; metal avg `-0.0159` n `20`; unknown avg `-0.1123` n `793`
- 4h: commodity avg `-0.0402` n `12`; crypto_alt avg `0.9611` n `231`; crypto_major avg `0.721` n `8`; equity avg `0.0525` n `127`; fx avg `-0.0434` n `6`; index avg `0.0083` n `26`; metal avg `0.0203` n `20`; unknown avg `0.2111` n `793`
- 24h: commodity avg `-0.0548` n `12`; crypto_alt avg `-3.2547` n `231`; crypto_major avg `-3.3044` n `8`; equity avg `-2.1621` n `127`; fx avg `-0.0828` n `6`; index avg `-0.2191` n `26`; metal avg `-0.1676` n `20`; unknown avg `-0.5799` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
