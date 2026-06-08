# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T03:37:22.899947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0876` n `12`; crypto_alt avg `-0.2694` n `228`; crypto_major avg `-0.3577` n `8`; equity avg `0.0234` n `74`; fx avg `-0.0092` n `6`; index avg `-0.0381` n `23`; metal avg `-0.029` n `18`; unknown avg `-0.1776` n `517`
- 1h: commodity avg `-0.0811` n `12`; crypto_alt avg `0.0244` n `228`; crypto_major avg `0.0959` n `8`; equity avg `0.0871` n `74`; fx avg `-0.0584` n `6`; index avg `0.0018` n `23`; metal avg `-0.0493` n `18`; unknown avg `-0.2223` n `517`
- 4h: commodity avg `0.2034` n `12`; crypto_alt avg `-0.2663` n `228`; crypto_major avg `0.2854` n `8`; equity avg `1.0004` n `74`; fx avg `-0.0537` n `6`; index avg `0.4106` n `23`; metal avg `-0.4873` n `18`; unknown avg `-0.503` n `517`
- 24h: commodity avg `0.2477` n `12`; crypto_alt avg `1.207` n `228`; crypto_major avg `3.5297` n `8`; equity avg `1.7639` n `74`; fx avg `-0.1042` n `6`; index avg `0.2923` n `23`; metal avg `-0.3602` n `18`; unknown avg `-5.4554` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
