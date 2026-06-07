# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T17:37:27.402779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `-0.0406` n `228`; crypto_major avg `0.0582` n `8`; equity avg `0.0612` n `74`; fx avg `0.0019` n `6`; index avg `-0.0205` n `23`; metal avg `-0.0174` n `18`; unknown avg `0.0377` n `516`
- 1h: commodity avg `-0.0119` n `12`; crypto_alt avg `0.152` n `228`; crypto_major avg `0.4591` n `8`; equity avg `0.0966` n `74`; fx avg `0.0068` n `6`; index avg `-0.0453` n `23`; metal avg `0.0712` n `18`; unknown avg `-2.3822` n `516`
- 4h: commodity avg `0.2286` n `12`; crypto_alt avg `1.1282` n `228`; crypto_major avg `1.5777` n `8`; equity avg `0.7344` n `74`; fx avg `-0.0124` n `6`; index avg `0.1891` n `23`; metal avg `0.1893` n `18`; unknown avg `-2.0907` n `516`
- 24h: commodity avg `0.1547` n `12`; crypto_alt avg `3.4329` n `228`; crypto_major avg `3.8561` n `8`; equity avg `2.176` n `74`; fx avg `-0.0353` n `6`; index avg `0.4382` n `23`; metal avg `0.6486` n `18`; unknown avg `-4.4118` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
