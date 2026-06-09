# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T13:52:26.967112+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1383` n `12`; crypto_alt avg `0.6377` n `228`; crypto_major avg `0.5165` n `8`; equity avg `0.6389` n `74`; fx avg `-0.0091` n `6`; index avg `0.2241` n `23`; metal avg `-0.0058` n `18`; unknown avg `0.0822` n `547`
- 1h: commodity avg `-0.823` n `12`; crypto_alt avg `0.2579` n `228`; crypto_major avg `-0.1535` n `8`; equity avg `0.2435` n `74`; fx avg `-0.038` n `6`; index avg `0.0426` n `23`; metal avg `-0.1236` n `18`; unknown avg `-0.0552` n `547`
- 4h: commodity avg `-0.4361` n `12`; crypto_alt avg `0.7813` n `228`; crypto_major avg `-0.2039` n `8`; equity avg `0.2397` n `74`; fx avg `0.0836` n `6`; index avg `0.0506` n `23`; metal avg `0.1961` n `18`; unknown avg `-0.0259` n `547`
- 24h: commodity avg `-0.8747` n `12`; crypto_alt avg `-1.0078` n `228`; crypto_major avg `-1.2995` n `8`; equity avg `1.4563` n `74`; fx avg `0.1128` n `6`; index avg `0.5715` n `23`; metal avg `0.6481` n `18`; unknown avg `-1.1983` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
