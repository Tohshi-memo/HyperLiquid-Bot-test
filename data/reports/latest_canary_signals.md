# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T05:52:23.841923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `13`; crypto_alt avg `0.1496` n `237`; crypto_major avg `0.1104` n `8`; equity avg `0.0473` n `152`; fx avg `-0.001` n `6`; index avg `-0.0118` n `26`; metal avg `-0.0425` n `20`; unknown avg `2.0222` n `1240`
- 1h: commodity avg `0.0559` n `13`; crypto_alt avg `0.3745` n `237`; crypto_major avg `0.2618` n `8`; equity avg `0.2249` n `152`; fx avg `0.0016` n `6`; index avg `-0.0126` n `26`; metal avg `-0.042` n `20`; unknown avg `0.2271` n `1240`
- 4h: commodity avg `-0.0262` n `13`; crypto_alt avg `0.7342` n `237`; crypto_major avg `0.561` n `8`; equity avg `0.4062` n `152`; fx avg `-0.0158` n `6`; index avg `0.0211` n `26`; metal avg `0.1221` n `20`; unknown avg `0.7718` n `1224`
- 24h: commodity avg `-0.5478` n `13`; crypto_alt avg `-0.3151` n `237`; crypto_major avg `-0.3046` n `8`; equity avg `-0.1771` n `152`; fx avg `0.0514` n `6`; index avg `0.027` n `26`; metal avg `0.1676` n `20`; unknown avg `5.1401` n `985`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2555`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2055`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
