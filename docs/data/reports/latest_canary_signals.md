# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T04:07:25.584092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.49` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `-0.04` n `231`; crypto_major avg `-0.0338` n `8`; equity avg `0.0179` n `127`; fx avg `0.0007` n `6`; index avg `0.0098` n `26`; metal avg `0.0025` n `20`; unknown avg `-0.0051` n `793`
- 1h: commodity avg `0.0011` n `12`; crypto_alt avg `-0.2195` n `231`; crypto_major avg `-0.0253` n `8`; equity avg `0.0277` n `127`; fx avg `-0.001` n `6`; index avg `0.0061` n `26`; metal avg `0.0116` n `20`; unknown avg `0.1305` n `793`
- 4h: commodity avg `0.0199` n `12`; crypto_alt avg `-0.446` n `231`; crypto_major avg `-0.2918` n `8`; equity avg `0.0872` n `127`; fx avg `0.0057` n `6`; index avg `0.0367` n `26`; metal avg `-0.0123` n `20`; unknown avg `-0.2016` n `793`
- 24h: commodity avg `-0.1046` n `12`; crypto_alt avg `-1.7628` n `231`; crypto_major avg `-2.4013` n `8`; equity avg `-1.8283` n `127`; fx avg `-0.085` n `6`; index avg `-0.1682` n `26`; metal avg `-0.2046` n `20`; unknown avg `-0.4615` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
