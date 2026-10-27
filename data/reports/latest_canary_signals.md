# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T05:37:27.932025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0252` n `13`; crypto_alt avg `-0.094` n `237`; crypto_major avg `-0.0607` n `8`; equity avg `-0.2254` n `154`; fx avg `-0.0016` n `6`; index avg `-0.048` n `27`; metal avg `-0.0013` n `20`; unknown avg `0.2319` n `1236`
- 1h: commodity avg `0.0164` n `13`; crypto_alt avg `-0.0396` n `237`; crypto_major avg `-0.0213` n `8`; equity avg `-0.3509` n `154`; fx avg `-0.0183` n `6`; index avg `0.0227` n `27`; metal avg `-0.1148` n `20`; unknown avg `-0.1676` n `1232`
- 4h: commodity avg `0.038` n `13`; crypto_alt avg `-0.6798` n `237`; crypto_major avg `-0.6647` n `8`; equity avg `-1.317` n `154`; fx avg `-0.0193` n `6`; index avg `-0.0759` n `27`; metal avg `-0.1893` n `20`; unknown avg `292.3454` n `1214`
- 24h: commodity avg `0.0361` n `13`; crypto_alt avg `-0.513` n `237`; crypto_major avg `-0.0659` n `8`; equity avg `0.3593` n `153`; fx avg `-0.0356` n `6`; index avg `0.0186` n `27`; metal avg `-0.2462` n `20`; unknown avg `1113.0236` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1915`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
