# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T03:07:25.621408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0357` n `13`; crypto_alt avg `-0.179` n `237`; crypto_major avg `-0.0664` n `8`; equity avg `-0.1625` n `151`; fx avg `0.0028` n `6`; index avg `-0.0263` n `26`; metal avg `-0.0485` n `20`; unknown avg `0.4247` n `1229`
- 1h: commodity avg `-0.0915` n `13`; crypto_alt avg `0.583` n `237`; crypto_major avg `0.5815` n `8`; equity avg `0.2871` n `151`; fx avg `0.0298` n `6`; index avg `0.0537` n `26`; metal avg `0.1151` n `20`; unknown avg `1.8735` n `1229`
- 4h: commodity avg `0.1174` n `13`; crypto_alt avg `1.2627` n `237`; crypto_major avg `0.8287` n `8`; equity avg `0.6371` n `151`; fx avg `-0.0105` n `6`; index avg `-0.0153` n `26`; metal avg `-0.0671` n `20`; unknown avg `0.6343` n `1223`
- 24h: commodity avg `0.4386` n `13`; crypto_alt avg `-2.032` n `237`; crypto_major avg `-1.0045` n `8`; equity avg `-3.2821` n `151`; fx avg `-0.1406` n `6`; index avg `-0.4247` n `26`; metal avg `-0.6679` n `20`; unknown avg `53.2674` n `903`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1732`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
