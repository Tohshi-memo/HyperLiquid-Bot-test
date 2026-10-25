# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T09:52:27.317202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `13`; crypto_alt avg `0.3189` n `237`; crypto_major avg `0.1811` n `8`; equity avg `0.0867` n `152`; fx avg `0.0027` n `6`; index avg `-0.0151` n `26`; metal avg `0.0148` n `20`; unknown avg `-0.0124` n `1209`
- 1h: commodity avg `-0.0204` n `13`; crypto_alt avg `0.1821` n `237`; crypto_major avg `-0.0836` n `8`; equity avg `-0.0104` n `152`; fx avg `-0.0147` n `6`; index avg `-0.0058` n `26`; metal avg `-0.0004` n `20`; unknown avg `11.8804` n `1203`
- 4h: commodity avg `-0.0105` n `13`; crypto_alt avg `-0.7911` n `237`; crypto_major avg `-0.6449` n `8`; equity avg `-0.2172` n `152`; fx avg `-0.0007` n `6`; index avg `-0.012` n `26`; metal avg `-0.0028` n `20`; unknown avg `12.3157` n `1167`
- 24h: commodity avg `-0.0198` n `13`; crypto_alt avg `-1.5637` n `237`; crypto_major avg `-0.061` n `8`; equity avg `0.0279` n `152`; fx avg `-0.0283` n `6`; index avg `0.0215` n `26`; metal avg `-0.0552` n `20`; unknown avg `12.2477` n `1050`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.196`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
