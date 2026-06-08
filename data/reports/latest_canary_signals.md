# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T02:22:20.261591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1179` n `12`; crypto_alt avg `0.0476` n `228`; crypto_major avg `0.1248` n `8`; equity avg `0.0165` n `74`; fx avg `0.0154` n `6`; index avg `0.2435` n `23`; metal avg `-0.2356` n `18`; unknown avg `0.0415` n `517`
- 1h: commodity avg `-0.0153` n `12`; crypto_alt avg `0.2377` n `228`; crypto_major avg `0.3798` n `8`; equity avg `0.1725` n `74`; fx avg `0.0041` n `6`; index avg `0.1357` n `23`; metal avg `0.0107` n `18`; unknown avg `-0.3052` n `517`
- 4h: commodity avg `0.1553` n `12`; crypto_alt avg `-0.6025` n `228`; crypto_major avg `0.3967` n `8`; equity avg `0.5638` n `74`; fx avg `-0.0291` n `6`; index avg `0.2375` n `23`; metal avg `-0.1762` n `18`; unknown avg `-0.2591` n `516`
- 24h: commodity avg `0.4007` n `12`; crypto_alt avg `1.3288` n `228`; crypto_major avg `3.9368` n `8`; equity avg `1.5106` n `74`; fx avg `-0.079` n `6`; index avg `0.4435` n `23`; metal avg `-0.1646` n `18`; unknown avg `-5.2453` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
