# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T15:48:02.616114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0335` n `12`; crypto_alt avg `0.0156` n `228`; crypto_major avg `-0.0637` n `8`; equity avg `-0.0185` n `74`; fx avg `-0.0019` n `6`; index avg `0.0013` n `23`; metal avg `-0.0186` n `18`; unknown avg `-0.0569` n `516`
- 1h: commodity avg `0.1311` n `12`; crypto_alt avg `0.0162` n `228`; crypto_major avg `0.1487` n `8`; equity avg `0.0545` n `74`; fx avg `-0.0011` n `6`; index avg `-0.1166` n `23`; metal avg `0.036` n `18`; unknown avg `0.0062` n `516`
- 4h: commodity avg `0.3226` n `12`; crypto_alt avg `-0.2034` n `228`; crypto_major avg `-0.1957` n `8`; equity avg `0.2439` n `74`; fx avg `0.0021` n `6`; index avg `0.0995` n `23`; metal avg `-0.128` n `18`; unknown avg `0.1564` n `516`
- 24h: commodity avg `0.2952` n `12`; crypto_alt avg `2.7852` n `228`; crypto_major avg `2.7083` n `8`; equity avg `1.892` n `74`; fx avg `0.003` n `6`; index avg `0.4078` n `23`; metal avg `0.6376` n `18`; unknown avg `-4.5736` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
