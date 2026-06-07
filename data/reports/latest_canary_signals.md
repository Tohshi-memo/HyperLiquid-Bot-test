# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T09:37:27.949265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.028` n `12`; crypto_alt avg `-0.596` n `228`; crypto_major avg `-0.6146` n `8`; equity avg `-0.1673` n `74`; fx avg `-0.0029` n `6`; index avg `-0.1004` n `23`; metal avg `-0.0194` n `18`; unknown avg `-0.2042` n `516`
- 1h: commodity avg `0.0639` n `12`; crypto_alt avg `0.2697` n `228`; crypto_major avg `0.1088` n `8`; equity avg `0.091` n `74`; fx avg `-0.0328` n `6`; index avg `-0.1511` n `23`; metal avg `0.0822` n `18`; unknown avg `-1.0459` n `516`
- 4h: commodity avg `-0.268` n `12`; crypto_alt avg `0.7718` n `228`; crypto_major avg `1.1991` n `8`; equity avg `0.3205` n `74`; fx avg `-0.0377` n `6`; index avg `-0.0343` n `23`; metal avg `0.2119` n `18`; unknown avg `-3.0989` n `506`
- 24h: commodity avg `0.1407` n `12`; crypto_alt avg `2.0154` n `228`; crypto_major avg `2.0027` n `8`; equity avg `2.0928` n `74`; fx avg `0.0318` n `6`; index avg `0.6558` n `23`; metal avg `0.6764` n `18`; unknown avg `1.2016` n `401`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
