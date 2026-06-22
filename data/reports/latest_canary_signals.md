# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T19:37:36.667591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.0233` n `228`; crypto_major avg `0.0493` n `8`; equity avg `-0.0132` n `85`; fx avg `-0.0029` n `6`; index avg `0.0016` n `23`; metal avg `-0.0222` n `20`; unknown avg `-0.0115` n `717`
- 1h: commodity avg `0.1012` n `12`; crypto_alt avg `-0.6286` n `228`; crypto_major avg `-0.653` n `8`; equity avg `-0.6452` n `85`; fx avg `0.0053` n `6`; index avg `-0.0304` n `23`; metal avg `-0.0085` n `20`; unknown avg `-0.1343` n `717`
- 4h: commodity avg `0.0377` n `12`; crypto_alt avg `-1.2077` n `228`; crypto_major avg `-0.7961` n `8`; equity avg `-0.4621` n `85`; fx avg `-0.0125` n `6`; index avg `-0.0409` n `23`; metal avg `-0.0523` n `20`; unknown avg `-0.3037` n `716`
- 24h: commodity avg `-1.0302` n `12`; crypto_alt avg `-0.9705` n `228`; crypto_major avg `-0.4938` n `8`; equity avg `-0.8627` n `85`; fx avg `0.0472` n `6`; index avg `0.0619` n `23`; metal avg `0.2715` n `18`; unknown avg `0.4047` n `639`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
