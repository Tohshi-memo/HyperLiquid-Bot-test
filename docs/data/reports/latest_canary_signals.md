# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T05:52:28.290943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0312` n `13`; crypto_alt avg `-0.0379` n `237`; crypto_major avg `0.0506` n `8`; equity avg `0.0659` n `151`; fx avg `0.0025` n `6`; index avg `0.0146` n `26`; metal avg `0.0021` n `20`; unknown avg `0.0796` n `1233`
- 1h: commodity avg `0.0596` n `13`; crypto_alt avg `0.4019` n `237`; crypto_major avg `0.3565` n `8`; equity avg `0.7185` n `151`; fx avg `0.0058` n `6`; index avg `0.054` n `26`; metal avg `0.2103` n `20`; unknown avg `0.0885` n `1227`
- 4h: commodity avg `0.0359` n `13`; crypto_alt avg `0.8138` n `237`; crypto_major avg `0.4733` n `8`; equity avg `0.9275` n `151`; fx avg `0.0291` n `6`; index avg `0.106` n `26`; metal avg `0.2449` n `20`; unknown avg `0.0765` n `1219`
- 24h: commodity avg `0.3121` n `13`; crypto_alt avg `-0.7325` n `237`; crypto_major avg `-0.4484` n `8`; equity avg `-1.6079` n `151`; fx avg `-0.0962` n `6`; index avg `-0.1087` n `26`; metal avg `-0.3175` n `20`; unknown avg `52.7624` n `899`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1886`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
