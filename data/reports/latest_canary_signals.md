# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T04:37:17.894749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0374` n `12`; crypto_alt avg `0.0465` n `228`; crypto_major avg `0.0266` n `8`; equity avg `0.001` n `69`; fx avg `0.0004` n `6`; index avg `-0.0025` n `23`; metal avg `-0.0024` n `18`; unknown avg `0.0839` n `421`
- 1h: commodity avg `0.1554` n `12`; crypto_alt avg `0.2068` n `228`; crypto_major avg `0.1398` n `8`; equity avg `-0.0222` n `69`; fx avg `0.0057` n `6`; index avg `-0.0384` n `23`; metal avg `0.0117` n `18`; unknown avg `-0.3011` n `421`
- 4h: commodity avg `0.202` n `12`; crypto_alt avg `0.6996` n `228`; crypto_major avg `0.7042` n `8`; equity avg `0.1611` n `69`; fx avg `0.0223` n `6`; index avg `-0.0068` n `23`; metal avg `-0.0365` n `18`; unknown avg `0.0636` n `419`
- 24h: commodity avg `0.1597` n `12`; crypto_alt avg `1.7849` n `228`; crypto_major avg `3.3835` n `8`; equity avg `1.0958` n `69`; fx avg `0.0511` n `6`; index avg `0.0758` n `23`; metal avg `0.0247` n `18`; unknown avg `0.8816` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
