# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T21:07:40.008271+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `0.066` n `228`; crypto_major avg `0.0963` n `8`; equity avg `0.0145` n `85`; fx avg `-0.0053` n `6`; index avg `-0.0064` n `23`; metal avg `0.0045` n `20`; unknown avg `-0.0082` n `717`
- 1h: commodity avg `-0.0349` n `12`; crypto_alt avg `-0.1383` n `228`; crypto_major avg `-0.1903` n `8`; equity avg `0.0145` n `85`; fx avg `-0.0019` n `6`; index avg `-0.0105` n `23`; metal avg `0.0037` n `20`; unknown avg `-0.0755` n `709`
- 4h: commodity avg `-0.0717` n `12`; crypto_alt avg `-0.6556` n `228`; crypto_major avg `-0.2823` n `8`; equity avg `0.0749` n `85`; fx avg `0.0077` n `6`; index avg `-0.0355` n `23`; metal avg `0.0274` n `20`; unknown avg `-0.1159` n `709`
- 24h: commodity avg `-0.8848` n `12`; crypto_alt avg `0.627` n `228`; crypto_major avg `0.7634` n `8`; equity avg `-0.3945` n `85`; fx avg `0.1676` n `6`; index avg `0.0884` n `23`; metal avg `0.3813` n `18`; unknown avg `0.699` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
