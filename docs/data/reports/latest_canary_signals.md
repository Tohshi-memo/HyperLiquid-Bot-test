# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T09:52:18.736468+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0084` n `12`; crypto_alt avg `0.0893` n `228`; crypto_major avg `-0.0444` n `8`; equity avg `-0.0061` n `74`; fx avg `0.0019` n `6`; index avg `-0.0714` n `23`; metal avg `0.0005` n `18`; unknown avg `0.1018` n `516`
- 1h: commodity avg `0.0167` n `12`; crypto_alt avg `-0.2867` n `228`; crypto_major avg `-0.2767` n `8`; equity avg `0.0141` n `74`; fx avg `-0.0141` n `6`; index avg `-0.2367` n `23`; metal avg `-0.0029` n `18`; unknown avg `-0.3118` n `516`
- 4h: commodity avg `-0.2631` n `12`; crypto_alt avg `0.9101` n `228`; crypto_major avg `1.1572` n `8`; equity avg `0.3268` n `74`; fx avg `-0.0287` n `6`; index avg `-0.1154` n `23`; metal avg `0.1977` n `18`; unknown avg `-3.0546` n `506`
- 24h: commodity avg `0.095` n `12`; crypto_alt avg `3.1732` n `228`; crypto_major avg `2.9571` n `8`; equity avg `2.2694` n `74`; fx avg `0.0277` n `6`; index avg `0.8242` n `23`; metal avg `0.7041` n `18`; unknown avg `0.5589` n `401`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
