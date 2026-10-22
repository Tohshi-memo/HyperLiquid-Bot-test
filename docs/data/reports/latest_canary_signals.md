# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T23:07:28.038454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `0.0011` n `237`; crypto_major avg `0.0778` n `8`; equity avg `0.0332` n `151`; fx avg `0.0026` n `6`; index avg `0.0216` n `26`; metal avg `0.0048` n `20`; unknown avg `0.0623` n `1231`
- 1h: commodity avg `-0.0103` n `13`; crypto_alt avg `-0.3989` n `237`; crypto_major avg `-0.1876` n `8`; equity avg `-0.064` n `151`; fx avg `0.0037` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0141` n `20`; unknown avg `-0.1862` n `1191`
- 4h: commodity avg `-0.026` n `13`; crypto_alt avg `-0.1579` n `237`; crypto_major avg `0.0822` n `8`; equity avg `0.0806` n `151`; fx avg `-0.0265` n `6`; index avg `0.0279` n `26`; metal avg `0.0205` n `20`; unknown avg `-0.0354` n `1127`
- 24h: commodity avg `0.4668` n `13`; crypto_alt avg `-4.9055` n `237`; crypto_major avg `-3.4753` n `8`; equity avg `-4.9531` n `151`; fx avg `-0.1631` n `6`; index avg `-0.5315` n `26`; metal avg `-0.9645` n `20`; unknown avg `54.1235` n `905`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1711`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
