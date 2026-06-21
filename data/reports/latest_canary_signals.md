# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T00:22:28.330177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0334` n `12`; crypto_alt avg `0.1973` n `228`; crypto_major avg `0.0292` n `8`; equity avg `0.0398` n `78`; fx avg `0.1191` n `6`; index avg `-0.002` n `23`; metal avg `0.0022` n `18`; unknown avg `-0.0233` n `701`
- 1h: commodity avg `0.0201` n `12`; crypto_alt avg `0.0587` n `228`; crypto_major avg `-0.1679` n `8`; equity avg `-0.032` n `78`; fx avg `-0.0024` n `6`; index avg `-0.0254` n `23`; metal avg `-0.011` n `18`; unknown avg `0.1749` n `701`
- 4h: commodity avg `0.064` n `12`; crypto_alt avg `0.8345` n `228`; crypto_major avg `0.6275` n `8`; equity avg `0.1483` n `78`; fx avg `0.0004` n `6`; index avg `0.0123` n `23`; metal avg `0.0132` n `18`; unknown avg `-0.1605` n `701`
- 24h: commodity avg `0.3518` n `12`; crypto_alt avg `1.0994` n `228`; crypto_major avg `1.5063` n `8`; equity avg `0.4018` n `78`; fx avg `0.0466` n `6`; index avg `0.0157` n `23`; metal avg `-0.0561` n `18`; unknown avg `-0.3136` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
