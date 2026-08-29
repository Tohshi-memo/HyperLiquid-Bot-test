# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T00:07:28.968770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `0.1601` n `231`; crypto_major avg `0.1788` n `8`; equity avg `0.0431` n `127`; fx avg `0.0026` n `6`; index avg `0.0074` n `26`; metal avg `0.026` n `20`; unknown avg `0.9831` n `793`
- 1h: commodity avg `0.033` n `12`; crypto_alt avg `0.3954` n `231`; crypto_major avg `0.2078` n `8`; equity avg `0.0474` n `127`; fx avg `-0.0093` n `6`; index avg `0.0084` n `26`; metal avg `0.0279` n `20`; unknown avg `0.6358` n `793`
- 4h: commodity avg `-0.0186` n `12`; crypto_alt avg `0.9186` n `231`; crypto_major avg `0.7759` n `8`; equity avg `0.1087` n `127`; fx avg `-0.0266` n `6`; index avg `0.0119` n `26`; metal avg `0.0613` n `20`; unknown avg `1.8365` n `793`
- 24h: commodity avg `-0.1284` n `12`; crypto_alt avg `-2.5554` n `231`; crypto_major avg `-2.9821` n `8`; equity avg `-1.8423` n `127`; fx avg `-0.1434` n `6`; index avg `-0.1763` n `26`; metal avg `-0.2904` n `20`; unknown avg `-0.6068` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
