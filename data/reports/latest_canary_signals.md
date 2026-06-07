# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T05:52:25.354731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `12`; crypto_alt avg `-0.0473` n `228`; crypto_major avg `-0.0018` n `8`; equity avg `-0.0117` n `74`; fx avg `-0.0071` n `6`; index avg `0.0101` n `23`; metal avg `0.0146` n `18`; unknown avg `0.2707` n `516`
- 1h: commodity avg `-0.056` n `12`; crypto_alt avg `0.4392` n `228`; crypto_major avg `0.4077` n `8`; equity avg `0.1911` n `74`; fx avg `-0.0028` n `6`; index avg `-0.0251` n `23`; metal avg `0.1098` n `18`; unknown avg `-0.5118` n `516`
- 4h: commodity avg `-0.1531` n `12`; crypto_alt avg `0.133` n `228`; crypto_major avg `1.0122` n `8`; equity avg `0.4335` n `74`; fx avg `-0.0004` n `6`; index avg `0.2844` n `23`; metal avg `0.301` n `18`; unknown avg `-0.3823` n `516`
- 24h: commodity avg `0.2381` n `12`; crypto_alt avg `3.2293` n `228`; crypto_major avg `2.0523` n `8`; equity avg `1.8376` n `74`; fx avg `0.0499` n `6`; index avg `1.0761` n `23`; metal avg `0.6894` n `18`; unknown avg `1.7629` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
