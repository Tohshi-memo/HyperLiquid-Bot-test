# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T04:07:26.124119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `13`; crypto_alt avg `0.0013` n `237`; crypto_major avg `0.0134` n `8`; equity avg `0.0154` n `152`; fx avg `0.0019` n `6`; index avg `0.0085` n `26`; metal avg `0.0017` n `20`; unknown avg `-0.1495` n `1223`
- 1h: commodity avg `-0.0162` n `13`; crypto_alt avg `0.164` n `237`; crypto_major avg `-0.0018` n `8`; equity avg `0.1135` n `152`; fx avg `-0.0012` n `6`; index avg `0.0223` n `26`; metal avg `0.0073` n `20`; unknown avg `1.4634` n `1221`
- 4h: commodity avg `-0.0091` n `13`; crypto_alt avg `-0.3633` n `237`; crypto_major avg `0.2813` n `8`; equity avg `0.1198` n `152`; fx avg `0.0055` n `6`; index avg `0.0326` n `26`; metal avg `0.0008` n `20`; unknown avg `1.6167` n `1207`
- 24h: commodity avg `0.0002` n `13`; crypto_alt avg `-1.2142` n `237`; crypto_major avg `-0.0844` n `8`; equity avg `0.0094` n `152`; fx avg `-0.0313` n `6`; index avg `0.017` n `26`; metal avg `-0.0842` n `20`; unknown avg `6.0401` n `1062`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
