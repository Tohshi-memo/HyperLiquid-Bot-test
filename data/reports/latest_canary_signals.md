# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T03:52:28.035882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.51` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `-0.0995` n `231`; crypto_major avg `-0.0686` n `8`; equity avg `0.0045` n `127`; fx avg `-0.0007` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.0111` n `793`
- 1h: commodity avg `0.0026` n `12`; crypto_alt avg `-0.2062` n `231`; crypto_major avg `-0.0183` n `8`; equity avg `0.0061` n `127`; fx avg `0.0` n `6`; index avg `0.0001` n `26`; metal avg `0.0087` n `20`; unknown avg `0.479` n `793`
- 4h: commodity avg `0.0115` n `12`; crypto_alt avg `-0.2453` n `231`; crypto_major avg `-0.0801` n `8`; equity avg `0.1126` n `127`; fx avg `0.0077` n `6`; index avg `0.0342` n `26`; metal avg `0.0111` n `20`; unknown avg `-0.1231` n `793`
- 24h: commodity avg `-0.1032` n `12`; crypto_alt avg `-1.8638` n `231`; crypto_major avg `-2.5069` n `8`; equity avg `-1.9287` n `127`; fx avg `-0.0752` n `6`; index avg `-0.196` n `26`; metal avg `-0.2088` n `20`; unknown avg `-0.4651` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
