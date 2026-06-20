# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T13:07:28.273590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0105` n `12`; crypto_alt avg `-0.0153` n `228`; crypto_major avg `0.0363` n `8`; equity avg `0.0652` n `78`; fx avg `0.0` n `6`; index avg `0.0051` n `23`; metal avg `0.0047` n `18`; unknown avg `-0.1305` n `701`
- 1h: commodity avg `-0.0239` n `12`; crypto_alt avg `-0.354` n `228`; crypto_major avg `-0.3005` n `8`; equity avg `0.0236` n `78`; fx avg `-0.0027` n `6`; index avg `0.0108` n `23`; metal avg `0.0053` n `18`; unknown avg `0.3143` n `701`
- 4h: commodity avg `-0.0943` n `12`; crypto_alt avg `-0.3182` n `228`; crypto_major avg `0.0022` n `8`; equity avg `-0.025` n `78`; fx avg `0.3219` n `6`; index avg `0.023` n `23`; metal avg `0.0222` n `18`; unknown avg `-0.2608` n `573`
- 24h: commodity avg `0.4048` n `12`; crypto_alt avg `-3.3425` n `228`; crypto_major avg `-3.4726` n `8`; equity avg `1.2024` n `78`; fx avg `-0.0677` n `6`; index avg `0.3027` n `23`; metal avg `-4.0878` n `18`; unknown avg `-0.1915` n `492`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
