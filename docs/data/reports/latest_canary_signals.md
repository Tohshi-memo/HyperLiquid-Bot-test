# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T15:37:21.357707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0222` n `12`; crypto_alt avg `0.487` n `228`; crypto_major avg `0.369` n `8`; equity avg `-0.0088` n `74`; fx avg `-0.0087` n `6`; index avg `0.0295` n `23`; metal avg `0.015` n `18`; unknown avg `-0.1579` n `515`
- 1h: commodity avg `-0.0326` n `12`; crypto_alt avg `-0.6609` n `228`; crypto_major avg `-0.6806` n `8`; equity avg `-0.2263` n `74`; fx avg `-0.0087` n `6`; index avg `-0.0299` n `23`; metal avg `-0.0216` n `18`; unknown avg `-2.7928` n `515`
- 4h: commodity avg `0.103` n `12`; crypto_alt avg `0.211` n `228`; crypto_major avg `-0.1306` n `8`; equity avg `0.3446` n `74`; fx avg `-0.008` n `6`; index avg `0.5291` n `23`; metal avg `-0.1545` n `18`; unknown avg `-0.4448` n `411`
- 24h: commodity avg `0.0046` n `12`; crypto_alt avg `-0.6225` n `228`; crypto_major avg `-0.5098` n `8`; equity avg `-3.0926` n `74`; fx avg `-0.1078` n `6`; index avg `-2.0004` n `23`; metal avg `-1.341` n `18`; unknown avg `-0.2649` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
