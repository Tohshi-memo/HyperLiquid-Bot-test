# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T01:52:32.436225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0391` n `13`; crypto_alt avg `0.1146` n `237`; crypto_major avg `0.1487` n `8`; equity avg `-0.2717` n `151`; fx avg `0.0081` n `6`; index avg `-0.0613` n `26`; metal avg `-0.0703` n `20`; unknown avg `0.3354` n `1233`
- 1h: commodity avg `0.1753` n `13`; crypto_alt avg `0.5562` n `237`; crypto_major avg `0.2464` n `8`; equity avg `0.1244` n `151`; fx avg `0.0206` n `6`; index avg `-0.0329` n `26`; metal avg `-0.184` n `20`; unknown avg `0.2322` n `1231`
- 4h: commodity avg `0.1638` n `13`; crypto_alt avg `0.6343` n `237`; crypto_major avg `0.42` n `8`; equity avg `0.7417` n `151`; fx avg `-0.0411` n `6`; index avg `0.0434` n `26`; metal avg `-0.1934` n `20`; unknown avg `0.4034` n `1185`
- 24h: commodity avg `0.4731` n `13`; crypto_alt avg `-3.1364` n `237`; crypto_major avg `-1.9834` n `8`; equity avg `-3.7389` n `151`; fx avg `-0.1754` n `6`; index avg `-0.4699` n `26`; metal avg `-0.8825` n `20`; unknown avg `52.7486` n `905`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
