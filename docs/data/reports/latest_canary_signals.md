# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T09:22:20.320207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0126` n `12`; crypto_alt avg `0.1171` n `228`; crypto_major avg `0.1019` n `8`; equity avg `-0.0223` n `69`; fx avg `-0.0036` n `6`; index avg `-0.0317` n `23`; metal avg `-0.0034` n `18`; unknown avg `-0.0749` n `421`
- 1h: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.0993` n `228`; crypto_major avg `-0.1362` n `8`; equity avg `-0.0354` n `69`; fx avg `-0.005` n `6`; index avg `-0.1193` n `23`; metal avg `-0.0144` n `18`; unknown avg `1.3175` n `421`
- 4h: commodity avg `0.1313` n `12`; crypto_alt avg `-0.59` n `228`; crypto_major avg `-0.7286` n `8`; equity avg `0.3291` n `69`; fx avg `0.0161` n `6`; index avg `-0.1033` n `23`; metal avg `-0.0196` n `18`; unknown avg `1.4767` n `401`
- 24h: commodity avg `0.2675` n `12`; crypto_alt avg `0.2677` n `228`; crypto_major avg `1.5622` n `8`; equity avg `1.1466` n `69`; fx avg `0.0359` n `6`; index avg `-0.1095` n `23`; metal avg `-0.0383` n `18`; unknown avg `2.347` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
