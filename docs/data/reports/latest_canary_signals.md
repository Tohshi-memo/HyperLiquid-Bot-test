# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T17:37:26.985852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6232` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0156` n `12`; crypto_alt avg `-0.3438` n `231`; crypto_major avg `-0.4545` n `8`; equity avg `0.0525` n `127`; fx avg `-0.0089` n `6`; index avg `0.017` n `26`; metal avg `-0.0156` n `20`; unknown avg `-0.0908` n `793`
- 1h: commodity avg `0.018` n `12`; crypto_alt avg `0.0262` n `231`; crypto_major avg `-0.3491` n `8`; equity avg `-0.0403` n `127`; fx avg `-0.0153` n `6`; index avg `-0.0216` n `26`; metal avg `0.0019` n `20`; unknown avg `0.3537` n `793`
- 4h: commodity avg `0.069` n `12`; crypto_alt avg `-1.6548` n `231`; crypto_major avg `-1.7834` n `8`; equity avg `-1.3085` n `127`; fx avg `-0.0289` n `6`; index avg `-0.1602` n `26`; metal avg `-0.7397` n `20`; unknown avg `0.0622` n `793`
- 24h: commodity avg `-0.1167` n `12`; crypto_alt avg `-3.8021` n `231`; crypto_major avg `-3.5418` n `8`; equity avg `-2.1489` n `127`; fx avg `-0.0961` n `6`; index avg `-0.1672` n `26`; metal avg `-0.2015` n `20`; unknown avg `-0.3793` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
