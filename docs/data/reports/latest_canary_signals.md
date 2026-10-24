# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T02:37:25.040038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `13`; crypto_alt avg `0.0879` n `237`; crypto_major avg `0.0913` n `8`; equity avg `0.0104` n `152`; fx avg `0.0019` n `6`; index avg `0.0018` n `26`; metal avg `-0.0017` n `20`; unknown avg `0.0827` n `1230`
- 1h: commodity avg `-0.059` n `13`; crypto_alt avg `0.4862` n `237`; crypto_major avg `0.4285` n `8`; equity avg `0.2295` n `152`; fx avg `0.0051` n `6`; index avg `0.0276` n `26`; metal avg `0.0183` n `20`; unknown avg `0.4478` n `1226`
- 4h: commodity avg `-0.0117` n `13`; crypto_alt avg `0.2393` n `237`; crypto_major avg `0.0169` n `8`; equity avg `0.1488` n `152`; fx avg `-0.0488` n `6`; index avg `0.0064` n `26`; metal avg `-0.0136` n `20`; unknown avg `4.0118` n `1214`
- 24h: commodity avg `0.3571` n `13`; crypto_alt avg `-1.7412` n `237`; crypto_major avg `-1.0968` n `8`; equity avg `0.5583` n `152`; fx avg `-0.0881` n `6`; index avg `0.052` n `26`; metal avg `-0.1779` n `20`; unknown avg `205.9495` n `1014`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
