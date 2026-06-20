# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T01:37:28.578178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `12`; crypto_alt avg `-0.0088` n `228`; crypto_major avg `0.124` n `8`; equity avg `0.01` n `78`; fx avg `0.0009` n `6`; index avg `0.0003` n `23`; metal avg `-0.002` n `18`; unknown avg `-0.2729` n `679`
- 1h: commodity avg `-0.0194` n `12`; crypto_alt avg `-0.5208` n `228`; crypto_major avg `-0.1933` n `8`; equity avg `-0.0971` n `78`; fx avg `-0.005` n `6`; index avg `-0.0157` n `23`; metal avg `-0.0417` n `18`; unknown avg `-0.5492` n `679`
- 4h: commodity avg `-0.0858` n `12`; crypto_alt avg `0.3702` n `228`; crypto_major avg `0.3848` n `8`; equity avg `0.2004` n `78`; fx avg `0.0693` n `6`; index avg `0.0573` n `23`; metal avg `-0.0162` n `18`; unknown avg `-0.555` n `671`
- 24h: commodity avg `0.2609` n `12`; crypto_alt avg `-3.4299` n `228`; crypto_major avg `-4.3024` n `8`; equity avg `0.9048` n `78`; fx avg `-0.0839` n `6`; index avg `0.2681` n `23`; metal avg `-4.131` n `18`; unknown avg `-0.6121` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
