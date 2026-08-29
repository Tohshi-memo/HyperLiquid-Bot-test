# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T03:07:31.786009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.48` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0017` n `12`; crypto_alt avg `-0.0279` n `231`; crypto_major avg `-0.0266` n `8`; equity avg `-0.0038` n `127`; fx avg `0.0018` n `6`; index avg `0.0039` n `26`; metal avg `-0.0003` n `20`; unknown avg `-0.036` n `793`
- 1h: commodity avg `0.0114` n `12`; crypto_alt avg `-0.0439` n `231`; crypto_major avg `-0.0996` n `8`; equity avg `0.0291` n `127`; fx avg `0.0012` n `6`; index avg `0.0221` n `26`; metal avg `-0.0087` n `20`; unknown avg `-0.1969` n `793`
- 4h: commodity avg `0.0518` n `12`; crypto_alt avg `0.1678` n `231`; crypto_major avg `-0.0595` n `8`; equity avg `0.1069` n `127`; fx avg `-0.0025` n `6`; index avg `0.0389` n `26`; metal avg `0.004` n `20`; unknown avg `-0.4067` n `793`
- 24h: commodity avg `-0.0879` n `12`; crypto_alt avg `-1.4298` n `231`; crypto_major avg `-2.2633` n `8`; equity avg `-1.9939` n `127`; fx avg `-0.0954` n `6`; index avg `-0.2051` n `26`; metal avg `-0.2492` n `20`; unknown avg `-0.4122` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
