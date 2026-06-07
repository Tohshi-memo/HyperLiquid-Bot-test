# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T10:07:22.809773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `-0.6007` n `228`; crypto_major avg `-0.5399` n `8`; equity avg `-0.3154` n `74`; fx avg `-0.0042` n `6`; index avg `-0.1607` n `23`; metal avg `-0.1271` n `18`; unknown avg `-3.2532` n `516`
- 1h: commodity avg `-0.0471` n `12`; crypto_alt avg `-1.1765` n `228`; crypto_major avg `-1.2876` n `8`; equity avg `-0.4656` n `74`; fx avg `-0.0158` n `6`; index avg `-0.3627` n `23`; metal avg `-0.1636` n `18`; unknown avg `-3.3151` n `516`
- 4h: commodity avg `-0.2836` n `12`; crypto_alt avg `0.5317` n `228`; crypto_major avg `0.7415` n `8`; equity avg `-0.0035` n `74`; fx avg `-0.03` n `6`; index avg `-0.312` n `23`; metal avg `0.099` n `18`; unknown avg `-2.9042` n `516`
- 24h: commodity avg `0.1015` n `12`; crypto_alt avg `3.4748` n `228`; crypto_major avg `3.0872` n `8`; equity avg `2.1211` n `74`; fx avg `0.0168` n `6`; index avg `0.6937` n `23`; metal avg `0.6457` n `18`; unknown avg `1.4046` n `401`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
