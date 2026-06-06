# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T21:52:18.958532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `-0.0767` n `228`; crypto_major avg `-0.0086` n `8`; equity avg `-0.073` n `74`; fx avg `0.024` n `6`; index avg `-0.0942` n `23`; metal avg `0.0033` n `18`; unknown avg `0.2024` n `515`
- 1h: commodity avg `-0.0092` n `12`; crypto_alt avg `0.5082` n `228`; crypto_major avg `0.4106` n `8`; equity avg `0.023` n `74`; fx avg `-0.02` n `6`; index avg `0.0332` n `23`; metal avg `0.0205` n `18`; unknown avg `0.3414` n `515`
- 4h: commodity avg `0.0458` n `12`; crypto_alt avg `0.7049` n `228`; crypto_major avg `0.3433` n `8`; equity avg `0.3733` n `74`; fx avg `-0.1136` n `6`; index avg `0.1024` n `23`; metal avg `0.017` n `18`; unknown avg `0.0953` n `515`
- 24h: commodity avg `0.8108` n `12`; crypto_alt avg `-2.9532` n `228`; crypto_major avg `-2.6154` n `8`; equity avg `-1.0874` n `74`; fx avg `0.0299` n `6`; index avg `0.024` n `23`; metal avg `-0.6056` n `18`; unknown avg `0.3127` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
