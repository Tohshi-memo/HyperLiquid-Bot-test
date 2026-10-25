# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T19:07:29.301456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `13`; crypto_alt avg `-0.2137` n `237`; crypto_major avg `-0.1293` n `8`; equity avg `-0.0352` n `152`; fx avg `-0.0063` n `6`; index avg `0.0052` n `26`; metal avg `-0.0028` n `20`; unknown avg `4.4242` n `1238`
- 1h: commodity avg `-0.0477` n `13`; crypto_alt avg `-0.217` n `237`; crypto_major avg `-0.1584` n `8`; equity avg `0.0145` n `152`; fx avg `-0.0006` n `6`; index avg `0.0083` n `26`; metal avg `-0.0116` n `20`; unknown avg `5.2924` n `1240`
- 4h: commodity avg `-0.0586` n `13`; crypto_alt avg `0.3843` n `237`; crypto_major avg `0.0502` n `8`; equity avg `0.3002` n `152`; fx avg `-0.0166` n `6`; index avg `0.0396` n `26`; metal avg `0.0438` n `20`; unknown avg `4.2537` n `1194`
- 24h: commodity avg `-0.2069` n `13`; crypto_alt avg `0.2095` n `237`; crypto_major avg `0.6458` n `8`; equity avg `0.6401` n `152`; fx avg `0.0236` n `6`; index avg `0.1273` n `26`; metal avg `0.1444` n `20`; unknown avg `10.8197` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2255`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
