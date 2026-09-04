# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T12:22:32.339896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0884` n `12`; crypto_alt avg `-0.0069` n `232`; crypto_major avg `0.0083` n `8`; equity avg `0.0844` n `133`; fx avg `-0.0235` n `6`; index avg `0.0028` n `26`; metal avg `0.0143` n `20`; unknown avg `-0.0359` n `793`
- 1h: commodity avg `0.0131` n `12`; crypto_alt avg `-0.1379` n `232`; crypto_major avg `-0.1428` n `8`; equity avg `-0.0347` n `133`; fx avg `-0.0494` n `6`; index avg `-0.0304` n `26`; metal avg `0.0519` n `20`; unknown avg `-0.114` n `791`
- 4h: commodity avg `0.0173` n `12`; crypto_alt avg `0.6476` n `232`; crypto_major avg `0.5047` n `8`; equity avg `0.1285` n `133`; fx avg `-0.0735` n `6`; index avg `0.008` n `26`; metal avg `-0.0958` n `20`; unknown avg `-0.1495` n `785`
- 24h: commodity avg `-0.4243` n `12`; crypto_alt avg `2.5449` n `232`; crypto_major avg `3.9287` n `8`; equity avg `2.3585` n `133`; fx avg `0.0123` n `6`; index avg `0.4135` n `26`; metal avg `0.4716` n `20`; unknown avg `18.3384` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
