# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T17:07:27.032581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `0.1923` n `228`; crypto_major avg `0.1749` n `8`; equity avg `-0.0211` n `74`; fx avg `-0.0213` n `6`; index avg `0.0187` n `23`; metal avg `0.0211` n `18`; unknown avg `-2.3845` n `516`
- 1h: commodity avg `0.0261` n `12`; crypto_alt avg `0.4545` n `228`; crypto_major avg `0.6094` n `8`; equity avg `0.3016` n `74`; fx avg `-0.0213` n `6`; index avg `0.1524` n `23`; metal avg `0.1235` n `18`; unknown avg `0.7804` n `516`
- 4h: commodity avg `0.1894` n `12`; crypto_alt avg `1.1917` n `228`; crypto_major avg `1.3562` n `8`; equity avg `0.7294` n `74`; fx avg `-0.0294` n `6`; index avg `0.2616` n `23`; metal avg `0.1764` n `18`; unknown avg `-2.0365` n `516`
- 24h: commodity avg `0.2551` n `12`; crypto_alt avg `3.1371` n `228`; crypto_major avg `3.4742` n `8`; equity avg `2.0151` n `74`; fx avg `-0.063` n `6`; index avg `0.4097` n `23`; metal avg `0.6681` n `18`; unknown avg `-4.9336` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
