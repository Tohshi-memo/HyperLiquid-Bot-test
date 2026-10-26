# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T20:22:41.601612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0487` n `13`; crypto_alt avg `0.0144` n `237`; crypto_major avg `-0.116` n `8`; equity avg `0.124` n `154`; fx avg `-0.0037` n `6`; index avg `0.0047` n `27`; metal avg `0.0128` n `20`; unknown avg `8.5449` n `1178`
- 1h: commodity avg `-0.1592` n `13`; crypto_alt avg `-0.418` n `237`; crypto_major avg `-0.4659` n `8`; equity avg `-0.3557` n `154`; fx avg `-0.0036` n `6`; index avg `-0.0444` n `27`; metal avg `-0.0074` n `20`; unknown avg `9.8595` n `1150`
- 4h: commodity avg `-0.4324` n `13`; crypto_alt avg `-0.58` n `237`; crypto_major avg `-0.3542` n `8`; equity avg `-0.2298` n `154`; fx avg `-0.0296` n `6`; index avg `-0.038` n `27`; metal avg `-0.0832` n `20`; unknown avg `8.8921` n `1150`
- 24h: commodity avg `-0.3287` n `13`; crypto_alt avg `-0.765` n `237`; crypto_major avg `-0.4243` n `8`; equity avg `0.3498` n `153`; fx avg `0.0119` n `6`; index avg `-0.1226` n `27`; metal avg `0.0063` n `20`; unknown avg `755.2666` n `970`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
