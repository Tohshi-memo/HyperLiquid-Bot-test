# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T05:22:24.503802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1661` n `12`; crypto_alt avg `0.2199` n `228`; crypto_major avg `0.195` n `8`; equity avg `-0.1061` n `74`; fx avg `-0.101` n `6`; index avg `0.02` n `23`; metal avg `0.02` n `18`; unknown avg `-0.2582` n `517`
- 1h: commodity avg `0.0324` n `12`; crypto_alt avg `-0.2019` n `228`; crypto_major avg `-0.2397` n `8`; equity avg `-0.4238` n `74`; fx avg `-0.0732` n `6`; index avg `-0.1038` n `23`; metal avg `-0.2266` n `18`; unknown avg `-0.245` n `517`
- 4h: commodity avg `0.0398` n `12`; crypto_alt avg `-0.5814` n `228`; crypto_major avg `-0.5561` n `8`; equity avg `-0.1586` n `74`; fx avg `-0.0952` n `6`; index avg `0.0399` n `23`; metal avg `-0.0407` n `18`; unknown avg `-0.3934` n `517`
- 24h: commodity avg `0.5023` n `12`; crypto_alt avg `0.254` n `228`; crypto_major avg `1.7731` n `8`; equity avg `0.6495` n `74`; fx avg `-0.1857` n `6`; index avg `0.0263` n `23`; metal avg `-0.4847` n `18`; unknown avg `-5.6518` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
