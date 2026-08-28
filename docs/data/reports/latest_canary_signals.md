# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T16:52:29.204118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0528` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0434` n `12`; crypto_alt avg `0.2948` n `231`; crypto_major avg `0.1493` n `8`; equity avg `0.1417` n `127`; fx avg `0.0076` n `6`; index avg `0.0262` n `26`; metal avg `0.0551` n `20`; unknown avg `0.2529` n `793`
- 1h: commodity avg `0.0905` n `12`; crypto_alt avg `-0.7669` n `231`; crypto_major avg `-0.5199` n `8`; equity avg `-0.2918` n `127`; fx avg `-0.0065` n `6`; index avg `-0.0606` n `26`; metal avg `-0.3994` n `20`; unknown avg `-0.0192` n `793`
- 4h: commodity avg `0.2463` n `12`; crypto_alt avg `-1.5826` n `231`; crypto_major avg `-1.1789` n `8`; equity avg `-1.3636` n `127`; fx avg `0.0046` n `6`; index avg `-0.1261` n `26`; metal avg `-0.6033` n `20`; unknown avg `-0.3873` n `792`
- 24h: commodity avg `-0.0639` n `12`; crypto_alt avg `-3.5791` n `231`; crypto_major avg `-3.2842` n `8`; equity avg `-1.921` n `127`; fx avg `-0.0815` n `6`; index avg `-0.1227` n `26`; metal avg `-0.1367` n `20`; unknown avg `-0.3005` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
