# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T04:22:24.532897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.45` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.1089` n `231`; crypto_major avg `0.07` n `8`; equity avg `0.0242` n `127`; fx avg `0.0` n `6`; index avg `-0.0039` n `26`; metal avg `0.0011` n `20`; unknown avg `-0.0072` n `793`
- 1h: commodity avg `0.003` n `12`; crypto_alt avg `-0.2239` n `231`; crypto_major avg `-0.0908` n `8`; equity avg `0.0439` n `127`; fx avg `0.0002` n `6`; index avg `0.002` n `26`; metal avg `0.0138` n `20`; unknown avg `0.0021` n `793`
- 4h: commodity avg `0.0372` n `12`; crypto_alt avg `-0.4112` n `231`; crypto_major avg `-0.2355` n `8`; equity avg `0.106` n `127`; fx avg `0.0018` n `6`; index avg `0.026` n `26`; metal avg `-0.0172` n `20`; unknown avg `-0.2896` n `793`
- 24h: commodity avg `-0.1134` n `12`; crypto_alt avg `-1.8578` n `231`; crypto_major avg `-2.4633` n `8`; equity avg `-1.8682` n `127`; fx avg `-0.0879` n `6`; index avg `-0.1951` n `26`; metal avg `-0.2543` n `20`; unknown avg `-0.4244` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
