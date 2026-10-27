# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T06:22:31.114740+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `13`; crypto_alt avg `-0.206` n `237`; crypto_major avg `-0.2253` n `8`; equity avg `-0.1797` n `154`; fx avg `-0.0037` n `6`; index avg `-0.0493` n `27`; metal avg `-0.0878` n `20`; unknown avg `0.1249` n `1238`
- 1h: commodity avg `0.0909` n `13`; crypto_alt avg `0.0101` n `237`; crypto_major avg `-0.1376` n `8`; equity avg `-0.3174` n `154`; fx avg `0.0063` n `6`; index avg `-0.0793` n `27`; metal avg `-0.1011` n `20`; unknown avg `-0.1444` n `1218`
- 4h: commodity avg `0.0865` n `13`; crypto_alt avg `-0.3052` n `237`; crypto_major avg `-0.5041` n `8`; equity avg `-1.2775` n `154`; fx avg `-0.0044` n `6`; index avg `-0.0817` n `27`; metal avg `-0.2571` n `20`; unknown avg `2.3356` n `1198`
- 24h: commodity avg `0.1165` n `13`; crypto_alt avg `-0.15` n `237`; crypto_major avg `-0.0424` n `8`; equity avg `0.5663` n `153`; fx avg `-0.0531` n `6`; index avg `0.0532` n `27`; metal avg `-0.2585` n `20`; unknown avg `1110.9508` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1917`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
