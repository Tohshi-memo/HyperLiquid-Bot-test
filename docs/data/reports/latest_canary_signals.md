# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T16:22:47.028940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.03` n `12`; crypto_alt avg `0.2749` n `228`; crypto_major avg `0.2382` n `8`; equity avg `-0.0204` n `85`; fx avg `-0.0102` n `6`; index avg `0.0314` n `23`; metal avg `0.0277` n `20`; unknown avg `-0.0192` n `717`
- 1h: commodity avg `0.0448` n `12`; crypto_alt avg `-0.2848` n `228`; crypto_major avg `-0.5005` n `8`; equity avg `-0.1589` n `85`; fx avg `0.0039` n `6`; index avg `0.0074` n `23`; metal avg `-0.1454` n `20`; unknown avg `0.0703` n `716`
- 4h: commodity avg `-0.2465` n `12`; crypto_alt avg `-0.7267` n `228`; crypto_major avg `-0.7314` n `8`; equity avg `-0.9009` n `85`; fx avg `-0.0677` n `6`; index avg `-0.0284` n `23`; metal avg `-0.3826` n `20`; unknown avg `0.1447` n `716`
- 24h: commodity avg `-0.7722` n `12`; crypto_alt avg `-0.3576` n `228`; crypto_major avg `-0.1687` n `8`; equity avg `-0.6732` n `85`; fx avg `-0.0352` n `6`; index avg `0.1326` n `23`; metal avg `0.1302` n `18`; unknown avg `0.7649` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
