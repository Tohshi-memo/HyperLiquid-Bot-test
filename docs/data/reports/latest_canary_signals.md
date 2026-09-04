# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T04:52:30.479263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `-0.3261` n `232`; crypto_major avg `-0.2465` n `8`; equity avg `-0.0301` n `133`; fx avg `-0.005` n `6`; index avg `-0.0101` n `26`; metal avg `0.006` n `20`; unknown avg `0.2653` n `793`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `-0.1749` n `232`; crypto_major avg `-0.0012` n `8`; equity avg `0.1645` n `133`; fx avg `-0.005` n `6`; index avg `0.0337` n `26`; metal avg `0.0517` n `20`; unknown avg `10.9775` n `791`
- 4h: commodity avg `0.0377` n `12`; crypto_alt avg `-0.4469` n `232`; crypto_major avg `-0.0405` n `8`; equity avg `0.1686` n `133`; fx avg `0.0338` n `6`; index avg `0.049` n `26`; metal avg `-0.094` n `20`; unknown avg `0.8728` n `791`
- 24h: commodity avg `-0.0942` n `12`; crypto_alt avg `2.2597` n `232`; crypto_major avg `4.1153` n `8`; equity avg `1.4885` n `133`; fx avg `-0.097` n `6`; index avg `0.2322` n `26`; metal avg `0.4361` n `20`; unknown avg `0.9673` n `736`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
