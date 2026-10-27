# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T04:52:32.506584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `13`; crypto_alt avg `0.0313` n `237`; crypto_major avg `-0.0035` n `8`; equity avg `-0.0377` n `154`; fx avg `-0.0101` n `6`; index avg `0.1016` n `27`; metal avg `-0.0376` n `20`; unknown avg `0.0674` n `1236`
- 1h: commodity avg `-0.0106` n `13`; crypto_alt avg `0.0029` n `237`; crypto_major avg `-0.1514` n `8`; equity avg `-0.6674` n `154`; fx avg `-0.031` n `6`; index avg `0.0413` n `27`; metal avg `-0.0371` n `20`; unknown avg `-0.0095` n `1224`
- 4h: commodity avg `-0.0568` n `13`; crypto_alt avg `-0.8233` n `237`; crypto_major avg `-0.829` n `8`; equity avg `-1.1746` n `154`; fx avg `-0.0155` n `6`; index avg `-0.0044` n `27`; metal avg `-0.0823` n `20`; unknown avg `227.9631` n `1214`
- 24h: commodity avg `0.0686` n `13`; crypto_alt avg `-0.2227` n `237`; crypto_major avg `0.105` n `8`; equity avg `0.8603` n `153`; fx avg `-0.0248` n `6`; index avg `0.0961` n `27`; metal avg `-0.1691` n `20`; unknown avg `1112.8503` n `992`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2062`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
