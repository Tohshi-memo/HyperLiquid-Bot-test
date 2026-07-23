# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T04:37:29.234392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.052` n `12`; crypto_alt avg `0.0647` n `230`; crypto_major avg `-0.0093` n `8`; equity avg `0.082` n `98`; fx avg `0.0112` n `6`; index avg `0.038` n `25`; metal avg `-0.0106` n `20`; unknown avg `-0.0015` n `773`
- 1h: commodity avg `-0.0705` n `12`; crypto_alt avg `0.2508` n `230`; crypto_major avg `0.0358` n `8`; equity avg `0.1828` n `98`; fx avg `-0.0007` n `6`; index avg `0.0862` n `25`; metal avg `0.0088` n `20`; unknown avg `-0.0657` n `773`
- 4h: commodity avg `0.02` n `12`; crypto_alt avg `-0.4534` n `230`; crypto_major avg `-0.5532` n `8`; equity avg `-0.2847` n `98`; fx avg `-0.0337` n `6`; index avg `-0.0075` n `25`; metal avg `0.1121` n `20`; unknown avg `0.3287` n `773`
- 24h: commodity avg `0.687` n `12`; crypto_alt avg `-0.5717` n `230`; crypto_major avg `-0.7665` n `8`; equity avg `-0.451` n `98`; fx avg `-0.1427` n `6`; index avg `-0.009` n `25`; metal avg `-0.0096` n `20`; unknown avg `1.8074` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.082`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
