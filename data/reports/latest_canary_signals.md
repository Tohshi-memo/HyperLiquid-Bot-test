# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T15:07:29.459449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0702` n `12`; crypto_alt avg `0.5662` n `228`; crypto_major avg `0.4019` n `8`; equity avg `0.1131` n `74`; fx avg `0.0004` n `6`; index avg `0.1752` n `23`; metal avg `0.0111` n `18`; unknown avg `0.0724` n `547`
- 1h: commodity avg `-0.3044` n `12`; crypto_alt avg `-0.5296` n `228`; crypto_major avg `-0.5477` n `8`; equity avg `-1.4197` n `74`; fx avg `0.0008` n `6`; index avg `-0.9512` n `23`; metal avg `-1.1239` n `18`; unknown avg `0.0517` n `545`
- 4h: commodity avg `-0.5287` n `12`; crypto_alt avg `-0.4613` n `228`; crypto_major avg `-1.4303` n `8`; equity avg `-2.2833` n `74`; fx avg `0.0165` n `6`; index avg `-1.3692` n `23`; metal avg `-1.4283` n `18`; unknown avg `-0.6701` n `545`
- 24h: commodity avg `-0.9195` n `12`; crypto_alt avg `-2.5362` n `228`; crypto_major avg `-3.1014` n `8`; equity avg `-2.0536` n `74`; fx avg `0.114` n `6`; index avg `-1.1857` n `23`; metal avg `-0.9989` n `18`; unknown avg `-1.2505` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
