# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T20:52:26.669050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.3278` n `228`; crypto_major avg `-0.3325` n `8`; equity avg `-0.0855` n `78`; fx avg `-0.0106` n `6`; index avg `-0.0083` n `23`; metal avg `-0.0175` n `18`; unknown avg `-0.0566` n `702`
- 1h: commodity avg `-0.0088` n `12`; crypto_alt avg `-0.6857` n `228`; crypto_major avg `-0.6502` n `8`; equity avg `-0.1354` n `78`; fx avg `-0.0386` n `6`; index avg `-0.0194` n `23`; metal avg `-0.0271` n `18`; unknown avg `0.3493` n `702`
- 4h: commodity avg `0.1037` n `12`; crypto_alt avg `-0.7436` n `228`; crypto_major avg `-0.5162` n `8`; equity avg `-0.1738` n `78`; fx avg `-0.089` n `6`; index avg `-0.0186` n `23`; metal avg `-0.1129` n `18`; unknown avg `0.7005` n `694`
- 24h: commodity avg `0.3056` n `12`; crypto_alt avg `0.9915` n `228`; crypto_major avg `-0.2058` n `8`; equity avg `0.1195` n `78`; fx avg `-0.1312` n `6`; index avg `0.0127` n `23`; metal avg `-0.1221` n `18`; unknown avg `0.7988` n `645`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
