# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T20:37:35.442376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0335` n `12`; crypto_alt avg `0.0463` n `228`; crypto_major avg `0.0795` n `8`; equity avg `-0.0239` n `85`; fx avg `-0.008` n `6`; index avg `-0.0079` n `23`; metal avg `0.0012` n `20`; unknown avg `0.0433` n `717`
- 1h: commodity avg `-0.0501` n `12`; crypto_alt avg `0.073` n `228`; crypto_major avg `-0.0448` n `8`; equity avg `0.1724` n `85`; fx avg `0.0132` n `6`; index avg `0.0253` n `23`; metal avg `0.0165` n `20`; unknown avg `-0.0099` n `709`
- 4h: commodity avg `-0.1073` n `12`; crypto_alt avg `-0.5241` n `228`; crypto_major avg `-0.1068` n `8`; equity avg `0.1165` n `85`; fx avg `0.0048` n `6`; index avg `-0.0197` n `23`; metal avg `0.0312` n `20`; unknown avg `-0.3027` n `709`
- 24h: commodity avg `-1.0034` n `12`; crypto_alt avg `-0.5674` n `228`; crypto_major avg `-0.2741` n `8`; equity avg `-0.6181` n `85`; fx avg `0.1084` n `6`; index avg `0.0918` n `23`; metal avg `0.3191` n `18`; unknown avg `0.751` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
