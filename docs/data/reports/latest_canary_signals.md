# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T19:07:33.241110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `0.0877` n `230`; crypto_major avg `0.163` n `8`; equity avg `0.3977` n `102`; fx avg `-0.0007` n `6`; index avg `0.0548` n `25`; metal avg `0.0722` n `20`; unknown avg `-0.086` n `779`
- 1h: commodity avg `-0.1073` n `12`; crypto_alt avg `-0.1373` n `230`; crypto_major avg `-0.0319` n `8`; equity avg `0.3062` n `102`; fx avg `0.0123` n `6`; index avg `0.0631` n `25`; metal avg `0.0661` n `20`; unknown avg `-0.0435` n `779`
- 4h: commodity avg `-0.1891` n `12`; crypto_alt avg `-0.1185` n `230`; crypto_major avg `0.4925` n `8`; equity avg `0.7626` n `102`; fx avg `-0.0335` n `6`; index avg `0.1706` n `25`; metal avg `0.3285` n `20`; unknown avg `-0.0514` n `779`
- 24h: commodity avg `-0.1002` n `12`; crypto_alt avg `0.0193` n `230`; crypto_major avg `0.9511` n `8`; equity avg `3.12` n `102`; fx avg `-0.3923` n `6`; index avg `0.2279` n `25`; metal avg `0.2732` n `20`; unknown avg `-0.0794` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
