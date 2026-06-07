# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T17:22:26.042223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0162` n `12`; crypto_alt avg `0.0419` n `228`; crypto_major avg `0.1327` n `8`; equity avg `-0.0118` n `74`; fx avg `0.0293` n `6`; index avg `-0.0544` n `23`; metal avg `0.0431` n `18`; unknown avg `-0.0868` n `516`
- 1h: commodity avg `-0.0399` n `12`; crypto_alt avg `0.4041` n `228`; crypto_major avg `0.4993` n `8`; equity avg `0.0828` n `74`; fx avg `0.0097` n `6`; index avg `0.0505` n `23`; metal avg `0.1202` n `18`; unknown avg `-2.3238` n `516`
- 4h: commodity avg `0.1851` n `12`; crypto_alt avg `1.251` n `228`; crypto_major avg `1.4374` n `8`; equity avg `0.8163` n `74`; fx avg `-0.0014` n `6`; index avg `0.2183` n `23`; metal avg `0.2141` n `18`; unknown avg `-2.12` n `516`
- 24h: commodity avg `0.2527` n `12`; crypto_alt avg `3.4273` n `228`; crypto_major avg `3.7763` n `8`; equity avg `2.0363` n `74`; fx avg `-0.033` n `6`; index avg `0.4082` n `23`; metal avg `0.691` n `18`; unknown avg `-4.8351` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
