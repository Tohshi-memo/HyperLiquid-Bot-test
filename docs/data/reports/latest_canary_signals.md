# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T11:37:28.403793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.016` n `13`; crypto_alt avg `0.1409` n `237`; crypto_major avg `0.1178` n `8`; equity avg `0.2193` n `152`; fx avg `-0.0002` n `6`; index avg `0.0402` n `26`; metal avg `0.0184` n `20`; unknown avg `1.4506` n `1240`
- 1h: commodity avg `0.1056` n `13`; crypto_alt avg `-0.0435` n `237`; crypto_major avg `-0.0504` n `8`; equity avg `-0.0301` n `152`; fx avg `-0.0033` n `6`; index avg `0.0077` n `26`; metal avg `-0.0136` n `20`; unknown avg `1.4765` n `1240`
- 4h: commodity avg `0.1305` n `13`; crypto_alt avg `0.9267` n `237`; crypto_major avg `0.7115` n `8`; equity avg `0.2621` n `152`; fx avg `0.0195` n `6`; index avg `0.0671` n `26`; metal avg `0.0324` n `20`; unknown avg `0.8869` n `1144`
- 24h: commodity avg `-0.3694` n `13`; crypto_alt avg `0.6782` n `237`; crypto_major avg `0.3998` n `8`; equity avg `-0.192` n `152`; fx avg `0.0483` n `6`; index avg `0.0275` n `26`; metal avg `0.1551` n `20`; unknown avg `-0.4171` n `977`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2592`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2294`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.228`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
