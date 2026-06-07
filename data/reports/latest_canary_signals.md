# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T04:37:24.253509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0222` n `12`; crypto_alt avg `0.3271` n `228`; crypto_major avg `0.3755` n `8`; equity avg `0.0621` n `74`; fx avg `-0.0007` n `6`; index avg `-0.0344` n `23`; metal avg `-0.0051` n `18`; unknown avg `0.2435` n `516`
- 1h: commodity avg `-0.0853` n `12`; crypto_alt avg `0.1162` n `228`; crypto_major avg `0.1973` n `8`; equity avg `0.1048` n `74`; fx avg `0.0039` n `6`; index avg `-0.0863` n `23`; metal avg `-0.037` n `18`; unknown avg `0.2041` n `516`
- 4h: commodity avg `-0.0987` n `12`; crypto_alt avg `1.0889` n `228`; crypto_major avg `1.3533` n `8`; equity avg `0.5368` n `74`; fx avg `0.0073` n `6`; index avg `0.3408` n `23`; metal avg `0.3856` n `18`; unknown avg `1.8917` n `516`
- 24h: commodity avg `0.2967` n `12`; crypto_alt avg `5.1759` n `228`; crypto_major avg `3.661` n `8`; equity avg `2.2474` n `74`; fx avg `0.0376` n `6`; index avg `1.1783` n `23`; metal avg `0.7214` n `18`; unknown avg `0.8992` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
