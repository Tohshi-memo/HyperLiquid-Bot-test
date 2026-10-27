# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T16:38:00.682898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0531` n `13`; crypto_alt avg `0.023` n `238`; crypto_major avg `0.1585` n `8`; equity avg `0.0147` n `154`; fx avg `0.0025` n `6`; index avg `-0.0446` n `27`; metal avg `0.0293` n `20`; unknown avg `0.0911` n `1238`
- 1h: commodity avg `-0.0326` n `13`; crypto_alt avg `0.2283` n `238`; crypto_major avg `0.3092` n `8`; equity avg `0.4464` n `154`; fx avg `-0.0072` n `6`; index avg `0.0623` n `27`; metal avg `0.0108` n `20`; unknown avg `1.6079` n `1226`
- 4h: commodity avg `-0.2766` n `13`; crypto_alt avg `0.8259` n `238`; crypto_major avg `0.8432` n `8`; equity avg `1.5391` n `154`; fx avg `-0.035` n `6`; index avg `0.2052` n `27`; metal avg `0.3097` n `20`; unknown avg `0.9822` n `1150`
- 24h: commodity avg `-0.8127` n `13`; crypto_alt avg `1.022` n `237`; crypto_major avg `1.4687` n `8`; equity avg `1.7688` n `154`; fx avg `-0.0779` n `6`; index avg `0.4335` n `27`; metal avg `0.1248` n `20`; unknown avg `29.1029` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2299`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2041`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2021`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
