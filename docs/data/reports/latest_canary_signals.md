# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T03:22:28.694437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `0.1723` n `228`; crypto_major avg `0.1012` n `8`; equity avg `0.0155` n `78`; fx avg `-0.0007` n `6`; index avg `-0.0102` n `23`; metal avg `0.0075` n `18`; unknown avg `0.1499` n `687`
- 1h: commodity avg `0.0083` n `12`; crypto_alt avg `0.0425` n `228`; crypto_major avg `0.0828` n `8`; equity avg `0.092` n `78`; fx avg `0.0073` n `6`; index avg `0.0185` n `23`; metal avg `-0.0352` n `18`; unknown avg `0.0909` n `687`
- 4h: commodity avg `0.1781` n `12`; crypto_alt avg `-0.0822` n `228`; crypto_major avg `0.057` n `8`; equity avg `0.1203` n `78`; fx avg `0.0398` n `6`; index avg `0.0728` n `23`; metal avg `-0.0579` n `18`; unknown avg `-0.3865` n `671`
- 24h: commodity avg `0.4526` n `12`; crypto_alt avg `-3.7566` n `228`; crypto_major avg `-4.518` n `8`; equity avg `0.9509` n `78`; fx avg `-0.0758` n `6`; index avg `0.2965` n `23`; metal avg `-4.164` n `18`; unknown avg `-0.6236` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
