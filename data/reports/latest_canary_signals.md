# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T04:52:29.020135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `13`; crypto_alt avg `0.0837` n `237`; crypto_major avg `-0.0622` n `8`; equity avg `-0.0554` n `151`; fx avg `0.0097` n `6`; index avg `-0.012` n `26`; metal avg `-0.0148` n `20`; unknown avg `0.0787` n `1233`
- 1h: commodity avg `0.0303` n `13`; crypto_alt avg `-0.2509` n `237`; crypto_major avg `-0.3456` n `8`; equity avg `-0.1541` n `151`; fx avg `0.0133` n `6`; index avg `-0.0229` n `26`; metal avg `-0.1049` n `20`; unknown avg `-0.1252` n `1223`
- 4h: commodity avg `0.152` n `13`; crypto_alt avg `0.9684` n `237`; crypto_major avg `0.3631` n `8`; equity avg `0.3319` n `151`; fx avg `0.044` n `6`; index avg `0.0188` n `26`; metal avg `-0.1495` n `20`; unknown avg `-0.2604` n `1221`
- 24h: commodity avg `0.388` n `13`; crypto_alt avg `-1.6077` n `237`; crypto_major avg `-1.1141` n `8`; equity avg `-2.7157` n `151`; fx avg `-0.1177` n `6`; index avg `-0.2558` n `26`; metal avg `-0.6216` n `20`; unknown avg `52.7333` n `901`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1732`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
