# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T20:22:26.040025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `12`; crypto_alt avg `0.2863` n `231`; crypto_major avg `0.1597` n `8`; equity avg `0.0502` n `127`; fx avg `-0.0016` n `6`; index avg `0.0003` n `26`; metal avg `-0.0295` n `20`; unknown avg `-0.0115` n `793`
- 1h: commodity avg `0.0492` n `12`; crypto_alt avg `0.1565` n `231`; crypto_major avg `-0.0375` n `8`; equity avg `0.0354` n `127`; fx avg `-0.006` n `6`; index avg `-0.028` n `26`; metal avg `-0.0218` n `20`; unknown avg `-0.0884` n `793`
- 4h: commodity avg `0.0867` n `12`; crypto_alt avg `0.3805` n `231`; crypto_major avg `-0.2955` n `8`; equity avg `-0.0276` n `127`; fx avg `-0.0211` n `6`; index avg `-0.0184` n `26`; metal avg `-0.1496` n `20`; unknown avg `0.1899` n `793`
- 24h: commodity avg `-0.1308` n `12`; crypto_alt avg `-3.3004` n `231`; crypto_major avg `-3.8761` n `8`; equity avg `-2.3524` n `127`; fx avg `-0.1236` n `6`; index avg `-0.203` n `26`; metal avg `-0.4227` n `20`; unknown avg `-0.6879` n `760`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
