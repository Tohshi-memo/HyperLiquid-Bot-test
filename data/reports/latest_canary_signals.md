# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T12:07:28.805721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0306` n `13`; crypto_alt avg `-0.0619` n `237`; crypto_major avg `-0.1197` n `8`; equity avg `0.0507` n `152`; fx avg `0.01` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0053` n `20`; unknown avg `0.2044` n `1223`
- 1h: commodity avg `-0.0605` n `13`; crypto_alt avg `0.634` n `237`; crypto_major avg `0.3993` n `8`; equity avg `0.1774` n `152`; fx avg `0.0022` n `6`; index avg `0.0233` n `26`; metal avg `0.0215` n `20`; unknown avg `0.2316` n `1225`
- 4h: commodity avg `-0.061` n `13`; crypto_alt avg `-0.2029` n `237`; crypto_major avg `-0.1142` n `8`; equity avg `0.07` n `152`; fx avg `0.0245` n `6`; index avg `0.0179` n `26`; metal avg `0.0194` n `20`; unknown avg `15.5764` n `1191`
- 24h: commodity avg `-0.139` n `13`; crypto_alt avg `-1.1035` n `237`; crypto_major avg `0.2298` n `8`; equity avg `0.1567` n `152`; fx avg `0.0033` n `6`; index avg `0.0498` n `26`; metal avg `-0.0176` n `20`; unknown avg `17.612` n `1048`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2167`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
