# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T14:07:31.649651+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `13`; crypto_alt avg `-0.2105` n `237`; crypto_major avg `-0.1274` n `8`; equity avg `-0.0551` n `152`; fx avg `-0.0012` n `6`; index avg `0.0028` n `26`; metal avg `0.0107` n `20`; unknown avg `0.1533` n `1229`
- 1h: commodity avg `-0.016` n `13`; crypto_alt avg `-0.1638` n `237`; crypto_major avg `-0.1086` n `8`; equity avg `0.0552` n `152`; fx avg `0.0107` n `6`; index avg `0.0248` n `26`; metal avg `0.0339` n `20`; unknown avg `380.8521` n `1231`
- 4h: commodity avg `-0.0521` n `13`; crypto_alt avg `0.105` n `237`; crypto_major avg `0.1665` n `8`; equity avg `0.2591` n `152`; fx avg `0.0148` n `6`; index avg `0.0449` n `26`; metal avg `0.0741` n `20`; unknown avg `1.4428` n `1221`
- 24h: commodity avg `-0.1474` n `13`; crypto_alt avg `-1.2409` n `237`; crypto_major avg `-0.1742` n `8`; equity avg `0.1489` n `152`; fx avg `0.0232` n `6`; index avg `0.0725` n `26`; metal avg `0.0035` n `20`; unknown avg `18.304` n `1080`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2226`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
