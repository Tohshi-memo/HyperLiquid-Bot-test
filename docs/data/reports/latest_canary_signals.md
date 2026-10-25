# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T01:07:28.539757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `13`; crypto_alt avg `-0.2581` n `237`; crypto_major avg `-0.1134` n `8`; equity avg `-0.015` n `152`; fx avg `0.0029` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0004` n `20`; unknown avg `-0.1631` n `1229`
- 1h: commodity avg `0.0073` n `13`; crypto_alt avg `-0.1297` n `237`; crypto_major avg `0.0524` n `8`; equity avg `0.0742` n `152`; fx avg `0.0068` n `6`; index avg `0.0116` n `26`; metal avg `0.0016` n `20`; unknown avg `1.6361` n `1231`
- 4h: commodity avg `-0.0373` n `13`; crypto_alt avg `0.6151` n `237`; crypto_major avg `0.7732` n `8`; equity avg `0.2485` n `152`; fx avg `-0.006` n `6`; index avg `0.0252` n `26`; metal avg `0.0267` n `20`; unknown avg `0.1556` n `1157`
- 24h: commodity avg `-0.0747` n `13`; crypto_alt avg `-0.6359` n `237`; crypto_major avg `-0.0065` n `8`; equity avg `0.1176` n `152`; fx avg `-0.0276` n `6`; index avg `0.0147` n `26`; metal avg `-0.0714` n `20`; unknown avg `0.4139` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1746`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
