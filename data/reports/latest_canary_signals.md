# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T05:22:17.579335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0368` n `12`; crypto_alt avg `0.2666` n `228`; crypto_major avg `0.246` n `8`; equity avg `0.0398` n `67`; fx avg `-0.0052` n `6`; index avg `-0.0074` n `23`; metal avg `0.0822` n `18`; unknown avg `0.343` n `407`
- 1h: commodity avg `0.1335` n `12`; crypto_alt avg `0.6888` n `228`; crypto_major avg `0.5701` n `8`; equity avg `-0.0922` n `67`; fx avg `-0.0041` n `6`; index avg `-0.0098` n `23`; metal avg `-0.1065` n `18`; unknown avg `0.1021` n `407`
- 4h: commodity avg `0.1212` n `12`; crypto_alt avg `0.3642` n `228`; crypto_major avg `0.1569` n `8`; equity avg `-0.0617` n `67`; fx avg `-0.0298` n `6`; index avg `0.0324` n `23`; metal avg `-0.3714` n `18`; unknown avg `-0.3118` n `407`
- 24h: commodity avg `0.8084` n `12`; crypto_alt avg `-0.3349` n `228`; crypto_major avg `-1.0834` n `8`; equity avg `-0.6373` n `67`; fx avg `-0.0242` n `6`; index avg `-0.0031` n `23`; metal avg `-0.3174` n `18`; unknown avg `0.3141` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1783`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
