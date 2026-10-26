# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T16:22:32.613545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0392` n `13`; crypto_alt avg `-0.2186` n `237`; crypto_major avg `-0.1668` n `8`; equity avg `0.0379` n `154`; fx avg `-0.0052` n `6`; index avg `-0.0007` n `27`; metal avg `-0.0106` n `20`; unknown avg `0.0218` n `1238`
- 1h: commodity avg `0.2928` n `13`; crypto_alt avg `-0.663` n `237`; crypto_major avg `-0.5443` n `8`; equity avg `-0.3144` n `154`; fx avg `0.0014` n `6`; index avg `-0.0615` n `27`; metal avg `-0.072` n `20`; unknown avg `2.515` n `1232`
- 4h: commodity avg `0.3882` n `13`; crypto_alt avg `0.3514` n `237`; crypto_major avg `0.1479` n `8`; equity avg `0.8528` n `153`; fx avg `0.0087` n `6`; index avg `0.1285` n `27`; metal avg `-0.016` n `20`; unknown avg `599.6097` n `1154`
- 24h: commodity avg `0.1251` n `13`; crypto_alt avg `0.2673` n `237`; crypto_major avg `0.148` n `8`; equity avg `0.8436` n `153`; fx avg `0.0706` n `6`; index avg `-0.0486` n `27`; metal avg `0.1376` n `20`; unknown avg `789.9775` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2289`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1922`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
