# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T13:07:36.664869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `13`; crypto_alt avg `-0.1247` n `239`; crypto_major avg `-0.2352` n `8`; equity avg `-0.1663` n `161`; fx avg `-0.0404` n `6`; index avg `-0.0144` n `27`; metal avg `-0.0495` n `20`; unknown avg `19.2147` n `1257`
- 1h: commodity avg `0.0149` n `13`; crypto_alt avg `0.0724` n `239`; crypto_major avg `0.0765` n `8`; equity avg `-0.1052` n `161`; fx avg `-0.008` n `6`; index avg `-0.0077` n `27`; metal avg `-0.0031` n `20`; unknown avg `0.3923` n `1255`
- 4h: commodity avg `0.3901` n `13`; crypto_alt avg `0.5593` n `239`; crypto_major avg `0.2639` n `8`; equity avg `0.3369` n `161`; fx avg `0.0137` n `6`; index avg `0.0027` n `27`; metal avg `-0.0202` n `20`; unknown avg `41.0457` n `1233`
- 24h: commodity avg `0.9968` n `13`; crypto_alt avg `-0.4873` n `239`; crypto_major avg `-1.2883` n `8`; equity avg `3.3873` n `161`; fx avg `-0.2198` n `6`; index avg `0.2986` n `27`; metal avg `0.2122` n `20`; unknown avg `1.2598` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2984`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.186`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
