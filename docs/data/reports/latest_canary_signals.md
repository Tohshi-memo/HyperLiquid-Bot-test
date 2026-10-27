# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T16:22:45.695748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `13`; crypto_alt avg `0.1415` n `238`; crypto_major avg `0.0782` n `8`; equity avg `0.0661` n `154`; fx avg `-0.0052` n `6`; index avg `0.0506` n `27`; metal avg `-0.0226` n `20`; unknown avg `0.168` n `1236`
- 1h: commodity avg `0.0519` n `13`; crypto_alt avg `0.1437` n `238`; crypto_major avg `0.0682` n `8`; equity avg `0.5224` n `154`; fx avg `-0.0109` n `6`; index avg `0.1207` n `27`; metal avg `-0.0313` n `20`; unknown avg `5.6631` n `1226`
- 4h: commodity avg `-0.1774` n `13`; crypto_alt avg `0.9121` n `238`; crypto_major avg `0.7777` n `8`; equity avg `1.483` n `154`; fx avg `-0.0325` n `6`; index avg `0.2246` n `27`; metal avg `0.3251` n `20`; unknown avg `0.717` n `1150`
- 24h: commodity avg `-0.7489` n `13`; crypto_alt avg `0.4623` n `237`; crypto_major avg `0.8871` n `8`; equity avg `1.6239` n `154`; fx avg `-0.0797` n `6`; index avg `0.4666` n `27`; metal avg `0.0799` n `20`; unknown avg `30.8725` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2301`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2035`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2014`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
