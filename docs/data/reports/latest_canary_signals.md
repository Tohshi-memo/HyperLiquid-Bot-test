# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T11:22:25.624931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0326` n `12`; crypto_alt avg `0.1214` n `228`; crypto_major avg `0.1097` n `8`; equity avg `0.145` n `74`; fx avg `-0.003` n `6`; index avg `-0.0163` n `23`; metal avg `0.0108` n `18`; unknown avg `0.0186` n `516`
- 1h: commodity avg `0.0601` n `12`; crypto_alt avg `-0.3042` n `228`; crypto_major avg `-0.2535` n `8`; equity avg `0.1843` n `74`; fx avg `0.0039` n `6`; index avg `0.111` n `23`; metal avg `-0.0123` n `18`; unknown avg `0.0236` n `516`
- 4h: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.0846` n `228`; crypto_major avg `0.218` n `8`; equity avg `-0.0743` n `74`; fx avg `-0.0209` n `6`; index avg `-0.2244` n `23`; metal avg `-0.0101` n `18`; unknown avg `-4.7351` n `516`
- 24h: commodity avg `0.1108` n `12`; crypto_alt avg `3.1173` n `228`; crypto_major avg `3.0064` n `8`; equity avg `2.0252` n `74`; fx avg `0.0245` n `6`; index avg `0.7295` n `23`; metal avg `0.6225` n `18`; unknown avg `0.2509` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
