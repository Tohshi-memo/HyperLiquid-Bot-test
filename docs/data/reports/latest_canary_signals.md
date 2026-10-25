# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T03:07:28.346914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `13`; crypto_alt avg `-0.0553` n `237`; crypto_major avg `-0.0001` n `8`; equity avg `-0.0256` n `152`; fx avg `0.004` n `6`; index avg `0.0035` n `26`; metal avg `-0.0052` n `20`; unknown avg `0.0466` n `1227`
- 1h: commodity avg `0.0193` n `13`; crypto_alt avg `-0.3207` n `237`; crypto_major avg `-0.0625` n `8`; equity avg `-0.0681` n `152`; fx avg `0.0063` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0142` n `20`; unknown avg `5.452` n `1227`
- 4h: commodity avg `-0.0115` n `13`; crypto_alt avg `-0.0261` n `237`; crypto_major avg `0.7201` n `8`; equity avg `0.092` n `152`; fx avg `0.0086` n `6`; index avg `0.0077` n `26`; metal avg `0.005` n `20`; unknown avg `0.1311` n `1211`
- 24h: commodity avg `0.4608` n `13`; crypto_alt avg `-1.3974` n `237`; crypto_major avg `-0.1688` n `8`; equity avg `-0.1086` n `152`; fx avg `-0.0287` n `6`; index avg `-0.0058` n `26`; metal avg `-0.0947` n `20`; unknown avg `6.1453` n `1066`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
