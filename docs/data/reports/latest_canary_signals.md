# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T09:52:25.139876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `12`; crypto_alt avg `-0.5133` n `229`; crypto_major avg `-0.3306` n `8`; equity avg `-0.0377` n `88`; fx avg `0.0015` n `6`; index avg `-0.0033` n `25`; metal avg `-0.0063` n `20`; unknown avg `-0.0162` n `765`
- 1h: commodity avg `-0.0053` n `12`; crypto_alt avg `-0.6432` n `229`; crypto_major avg `-0.6529` n `8`; equity avg `-0.1274` n `88`; fx avg `0.0` n `6`; index avg `-0.0182` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.03` n `765`
- 4h: commodity avg `0.0198` n `12`; crypto_alt avg `-0.4521` n `229`; crypto_major avg `-0.3312` n `8`; equity avg `-0.0854` n `88`; fx avg `0.0112` n `6`; index avg `-0.0134` n `25`; metal avg `0.0167` n `20`; unknown avg `-0.152` n `731`
- 24h: commodity avg `0.0104` n `12`; crypto_alt avg `-0.8579` n `229`; crypto_major avg `-1.0586` n `8`; equity avg `0.0985` n `88`; fx avg `0.0111` n `6`; index avg `0.0321` n `25`; metal avg `0.0674` n `20`; unknown avg `-1.2097` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
