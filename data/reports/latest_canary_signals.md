# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T21:52:16.625499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.0144` n `228`; crypto_major avg `0.0163` n `8`; equity avg `-0.0322` n `67`; fx avg `-0.0029` n `6`; index avg `0.0163` n `23`; metal avg `-0.021` n `18`; unknown avg `0.0545` n `405`
- 1h: commodity avg `0.361` n `12`; crypto_alt avg `0.0637` n `228`; crypto_major avg `0.0402` n `8`; equity avg `0.0069` n `67`; fx avg `0.0267` n `6`; index avg `0.1243` n `23`; metal avg `-0.0077` n `18`; unknown avg `0.0442` n `405`
- 4h: commodity avg `0.4527` n `12`; crypto_alt avg `-0.6412` n `228`; crypto_major avg `-0.5783` n `8`; equity avg `-0.0168` n `67`; fx avg `0.0283` n `6`; index avg `0.1373` n `23`; metal avg `0.0365` n `18`; unknown avg `-0.5114` n `405`
- 24h: commodity avg `-0.8488` n `12`; crypto_alt avg `3.2466` n `228`; crypto_major avg `1.0471` n `8`; equity avg `1.0147` n `67`; fx avg `-0.052` n `6`; index avg `0.7554` n `23`; metal avg `2.0484` n `18`; unknown avg `1.471` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
