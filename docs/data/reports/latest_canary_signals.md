# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T20:52:21.217189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0522` n `12`; crypto_alt avg `-0.0053` n `228`; crypto_major avg `-0.0419` n `8`; equity avg `0.0256` n `69`; fx avg `-0.0026` n `6`; index avg `0.0093` n `23`; metal avg `-0.0026` n `18`; unknown avg `0.1375` n `421`
- 1h: commodity avg `-0.048` n `12`; crypto_alt avg `0.1474` n `228`; crypto_major avg `-0.1244` n `8`; equity avg `0.0844` n `69`; fx avg `-0.0029` n `6`; index avg `-0.0606` n `23`; metal avg `0.0138` n `18`; unknown avg `-0.3473` n `421`
- 4h: commodity avg `-0.0736` n `12`; crypto_alt avg `0.3073` n `228`; crypto_major avg `0.371` n `8`; equity avg `0.2777` n `69`; fx avg `-0.0019` n `6`; index avg `0.0075` n `23`; metal avg `0.0018` n `18`; unknown avg `-0.2213` n `421`
- 24h: commodity avg `-0.0828` n `12`; crypto_alt avg `1.5918` n `228`; crypto_major avg `2.4636` n `8`; equity avg `0.956` n `69`; fx avg `0.0157` n `6`; index avg `0.0428` n `23`; metal avg `0.0868` n `18`; unknown avg `0.3224` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
