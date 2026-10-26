# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T18:52:34.993494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0361` n `13`; crypto_alt avg `-0.334` n `237`; crypto_major avg `-0.3842` n `8`; equity avg `-0.0667` n `154`; fx avg `0.0029` n `6`; index avg `-0.019` n `27`; metal avg `-0.0162` n `20`; unknown avg `0.1323` n `1238`
- 1h: commodity avg `-0.1058` n `13`; crypto_alt avg `-0.5807` n `237`; crypto_major avg `-0.4218` n `8`; equity avg `-0.0911` n `154`; fx avg `-0.0113` n `6`; index avg `-0.009` n `27`; metal avg `-0.0369` n `20`; unknown avg `0.0374` n `1236`
- 4h: commodity avg `0.018` n `13`; crypto_alt avg `-0.7563` n `237`; crypto_major avg `-0.2351` n `8`; equity avg `0.4127` n `154`; fx avg `-0.0186` n `6`; index avg `-0.0162` n `27`; metal avg `-0.0846` n `20`; unknown avg `-0.1567` n `1224`
- 24h: commodity avg `-0.2277` n `13`; crypto_alt avg `-1.019` n `237`; crypto_major avg `-0.3623` n `8`; equity avg `0.6411` n `153`; fx avg `0.0488` n `6`; index avg `-0.0912` n `27`; metal avg `0.0288` n `20`; unknown avg `778.5365` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1866`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
