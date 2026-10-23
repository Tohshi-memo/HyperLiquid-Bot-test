# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T08:07:26.519457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0087` n `13`; crypto_alt avg `-0.0713` n `237`; crypto_major avg `0.0871` n `8`; equity avg `0.2271` n `152`; fx avg `0.0032` n `6`; index avg `0.0216` n `26`; metal avg `-0.0168` n `20`; unknown avg `-0.053` n `1165`
- 1h: commodity avg `0.0342` n `13`; crypto_alt avg `-0.0604` n `237`; crypto_major avg `-0.0468` n `8`; equity avg `0.0119` n `152`; fx avg `-0.0266` n `6`; index avg `-0.006` n `26`; metal avg `-0.029` n `20`; unknown avg `0.54` n `1165`
- 4h: commodity avg `0.0815` n `13`; crypto_alt avg `0.1434` n `237`; crypto_major avg `0.2452` n `8`; equity avg `0.9509` n `152`; fx avg `-0.0174` n `6`; index avg `0.0389` n `26`; metal avg `0.0023` n `20`; unknown avg `-0.0455` n `1148`
- 24h: commodity avg `0.1306` n `13`; crypto_alt avg `-0.0788` n `237`; crypto_major avg `0.048` n `8`; equity avg `-0.7285` n `152`; fx avg `-0.0589` n `6`; index avg `-0.0491` n `26`; metal avg `-0.4477` n `20`; unknown avg `54.4664` n `858`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1867`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
