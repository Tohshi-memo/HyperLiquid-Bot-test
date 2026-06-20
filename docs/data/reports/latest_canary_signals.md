# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T13:22:32.774312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3355` n `12`; crypto_alt avg `-0.3308` n `228`; crypto_major avg `-0.3729` n `8`; equity avg `-0.2477` n `78`; fx avg `-0.0175` n `6`; index avg `-0.0132` n `23`; metal avg `-0.0319` n `18`; unknown avg `0.0156` n `701`
- 1h: commodity avg `0.4029` n `12`; crypto_alt avg `-0.6146` n `228`; crypto_major avg `-0.5849` n `8`; equity avg `-0.2322` n `78`; fx avg `-0.0202` n `6`; index avg `-0.0073` n `23`; metal avg `-0.0174` n `18`; unknown avg `-0.1733` n `701`
- 4h: commodity avg `0.3289` n `12`; crypto_alt avg `-0.6248` n `228`; crypto_major avg `-0.3023` n `8`; equity avg `-0.2843` n `78`; fx avg `0.2955` n `6`; index avg `-0.0074` n `23`; metal avg `-0.0147` n `18`; unknown avg `-0.3307` n `573`
- 24h: commodity avg `0.8362` n `12`; crypto_alt avg `-3.5736` n `228`; crypto_major avg `-3.794` n `8`; equity avg `0.9451` n `78`; fx avg `-0.0851` n `6`; index avg `0.2902` n `23`; metal avg `-4.1182` n `18`; unknown avg `-0.3094` n `492`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
