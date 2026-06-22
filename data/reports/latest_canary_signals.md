# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T19:51:35.644409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0218` n `12`; crypto_alt avg `-0.1665` n `228`; crypto_major avg `-0.1679` n `8`; equity avg `0.1433` n `85`; fx avg `0.015` n `6`; index avg `0.0135` n `23`; metal avg `-0.0191` n `20`; unknown avg `0.1674` n `717`
- 1h: commodity avg `0.0612` n `12`; crypto_alt avg `-0.3539` n `228`; crypto_major avg `-0.374` n `8`; equity avg `-0.1005` n `85`; fx avg `0.0274` n `6`; index avg `0.0139` n `23`; metal avg `-0.0504` n `20`; unknown avg `0.0002` n `717`
- 4h: commodity avg `0.0568` n `12`; crypto_alt avg `-0.935` n `228`; crypto_major avg `-0.477` n `8`; equity avg `-0.3055` n `85`; fx avg `0.0002` n `6`; index avg `-0.0358` n `23`; metal avg `0.0811` n `20`; unknown avg `-0.3449` n `717`
- 24h: commodity avg `-0.929` n `12`; crypto_alt avg `-1.157` n `228`; crypto_major avg `-0.7133` n `8`; equity avg `-0.7048` n `85`; fx avg `0.0822` n `6`; index avg `0.0686` n `23`; metal avg `0.2694` n `18`; unknown avg `0.488` n `639`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
