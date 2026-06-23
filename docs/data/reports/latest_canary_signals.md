# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T00:07:29.631980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `0.1102` n `228`; crypto_major avg `-0.03` n `8`; equity avg `-0.1113` n `86`; fx avg `0.0065` n `6`; index avg `-0.0069` n `23`; metal avg `-0.0328` n `20`; unknown avg `0.0293` n `716`
- 1h: commodity avg `-0.0255` n `12`; crypto_alt avg `0.2034` n `228`; crypto_major avg `0.051` n `8`; equity avg `-0.2007` n `86`; fx avg `0.0224` n `6`; index avg `-0.0693` n `23`; metal avg `-0.0829` n `20`; unknown avg `0.6927` n `716`
- 4h: commodity avg `-0.0442` n `12`; crypto_alt avg `-0.982` n `228`; crypto_major avg `-0.8104` n `8`; equity avg `-0.4212` n `86`; fx avg `0.0224` n `6`; index avg `-0.0907` n `23`; metal avg `-0.0963` n `20`; unknown avg `-0.0034` n `708`
- 24h: commodity avg `-0.8853` n `12`; crypto_alt avg `-0.366` n `228`; crypto_major avg `0.0472` n `8`; equity avg `-0.1746` n `85`; fx avg `0.1062` n `6`; index avg `0.145` n `23`; metal avg `0.2965` n `18`; unknown avg `0.5286` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
