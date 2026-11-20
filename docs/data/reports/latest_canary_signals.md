# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T01:52:31.148787+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `13`; crypto_alt avg `-0.4461` n `239`; crypto_major avg `-0.518` n `8`; equity avg `-0.2811` n `165`; fx avg `-0.0026` n `6`; index avg `-0.024` n `27`; metal avg `-0.1624` n `20`; unknown avg `0.4934` n `1262`
- 1h: commodity avg `-0.0017` n `13`; crypto_alt avg `-0.6158` n `239`; crypto_major avg `-0.3959` n `8`; equity avg `-0.21` n `165`; fx avg `-0.0512` n `6`; index avg `0.0227` n `27`; metal avg `-0.419` n `20`; unknown avg `-0.0139` n `1260`
- 4h: commodity avg `-0.0542` n `13`; crypto_alt avg `-0.524` n `239`; crypto_major avg `-0.171` n `8`; equity avg `-1.1145` n `165`; fx avg `-0.0275` n `6`; index avg `-0.1147` n `27`; metal avg `-0.6434` n `20`; unknown avg `13.2023` n `1240`
- 24h: commodity avg `-0.1813` n `13`; crypto_alt avg `-1.7027` n `239`; crypto_major avg `-1.0124` n `8`; equity avg `-5.1618` n `165`; fx avg `-0.0244` n `6`; index avg `-0.381` n `27`; metal avg `-1.6905` n `20`; unknown avg `15.766` n `1172`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
