# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T17:52:19.790504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `12`; crypto_alt avg `-0.3448` n `228`; crypto_major avg `-0.272` n `8`; equity avg `-0.1413` n `74`; fx avg `-0.002` n `6`; index avg `-0.0236` n `23`; metal avg `-0.0266` n `18`; unknown avg `-0.1273` n `516`
- 1h: commodity avg `0.0011` n `12`; crypto_alt avg `-0.1524` n `228`; crypto_major avg `0.0929` n `8`; equity avg `-0.1124` n `74`; fx avg `0.0079` n `6`; index avg `-0.08` n `23`; metal avg `0.0202` n `18`; unknown avg `-2.538` n `516`
- 4h: commodity avg `0.2617` n `12`; crypto_alt avg `0.5713` n `228`; crypto_major avg `1.068` n `8`; equity avg `0.4128` n `74`; fx avg `-0.0048` n `6`; index avg `0.0511` n `23`; metal avg `0.1237` n `18`; unknown avg `-2.2735` n `516`
- 24h: commodity avg `0.1643` n `12`; crypto_alt avg `3.4012` n `228`; crypto_major avg `3.847` n `8`; equity avg `2.1067` n `74`; fx avg `-0.1524` n `6`; index avg `0.4298` n `23`; metal avg `0.6414` n `18`; unknown avg `-4.9599` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
