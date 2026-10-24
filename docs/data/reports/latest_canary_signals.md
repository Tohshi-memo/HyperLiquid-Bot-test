# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T20:37:28.908743+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0456` n `13`; crypto_alt avg `0.0031` n `237`; crypto_major avg `-0.0359` n `8`; equity avg `-0.0043` n `152`; fx avg `-0.004` n `6`; index avg `-0.0015` n `26`; metal avg `0.0065` n `20`; unknown avg `0.1094` n `1229`
- 1h: commodity avg `0.0147` n `13`; crypto_alt avg `0.3697` n `237`; crypto_major avg `0.1462` n `8`; equity avg `0.0392` n `152`; fx avg `0.012` n `6`; index avg `0.0042` n `26`; metal avg `0.0117` n `20`; unknown avg `-0.1596` n `1199`
- 4h: commodity avg `-0.0339` n `13`; crypto_alt avg `1.7142` n `237`; crypto_major avg `1.4947` n `8`; equity avg `0.6163` n `152`; fx avg `-0.0078` n `6`; index avg `0.079` n `26`; metal avg `0.0782` n `20`; unknown avg `1.8483` n `1157`
- 24h: commodity avg `0.0821` n `13`; crypto_alt avg `-1.9904` n `237`; crypto_major avg `-1.4493` n `8`; equity avg `-0.2442` n `152`; fx avg `-0.0133` n `6`; index avg `-0.0469` n `26`; metal avg `-0.132` n `20`; unknown avg `0.3648` n `1074`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1812`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
