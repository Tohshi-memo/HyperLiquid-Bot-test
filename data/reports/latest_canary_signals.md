# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T05:22:30.093127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `12`; crypto_alt avg `0.031` n `228`; crypto_major avg `-0.0015` n `8`; equity avg `0.0175` n `78`; fx avg `-0.0027` n `6`; index avg `0.0006` n `23`; metal avg `-0.0019` n `18`; unknown avg `5.6408` n `686`
- 1h: commodity avg `-0.0295` n `12`; crypto_alt avg `-0.1323` n `228`; crypto_major avg `-0.4162` n `8`; equity avg `0.0252` n `78`; fx avg `0.0019` n `6`; index avg `0.0039` n `23`; metal avg `-0.0074` n `18`; unknown avg `6.0238` n `678`
- 4h: commodity avg `-0.0047` n `12`; crypto_alt avg `-0.0381` n `228`; crypto_major avg `-0.2492` n `8`; equity avg `0.1977` n `78`; fx avg `0.0491` n `6`; index avg `0.0215` n `23`; metal avg `0.026` n `18`; unknown avg `-0.2097` n `677`
- 24h: commodity avg `0.1755` n `12`; crypto_alt avg `0.8064` n `228`; crypto_major avg `0.3114` n `8`; equity avg `0.2479` n `78`; fx avg `0.057` n `6`; index avg `-0.0116` n `23`; metal avg `-0.047` n `18`; unknown avg `-0.1777` n `533`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
