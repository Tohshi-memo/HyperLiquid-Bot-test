# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T03:52:27.842497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0156` n `13`; crypto_alt avg `-0.1623` n `237`; crypto_major avg `-0.1387` n `8`; equity avg `-0.0835` n `154`; fx avg `-0.0038` n `6`; index avg `0.0131` n `27`; metal avg `-0.0146` n `20`; unknown avg `154.5838` n `1238`
- 1h: commodity avg `0.0235` n `13`; crypto_alt avg `-0.1715` n `237`; crypto_major avg `-0.1034` n `8`; equity avg `-0.0696` n `154`; fx avg `0.0032` n `6`; index avg `0.012` n `27`; metal avg `0.0261` n `20`; unknown avg `270.4964` n `1228`
- 4h: commodity avg `-0.0705` n `13`; crypto_alt avg `-0.8407` n `237`; crypto_major avg `-0.376` n `8`; equity avg `-0.1995` n `154`; fx avg `0.0128` n `6`; index avg `0.03` n `27`; metal avg `-0.0378` n `20`; unknown avg `92.7425` n `1220`
- 24h: commodity avg `0.0804` n `13`; crypto_alt avg `0.7186` n `237`; crypto_major avg `1.1763` n `8`; equity avg `1.8475` n `153`; fx avg `0.0107` n `6`; index avg `0.1098` n `27`; metal avg `-0.107` n `20`; unknown avg `1009.2051` n `996`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1854`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.182`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
