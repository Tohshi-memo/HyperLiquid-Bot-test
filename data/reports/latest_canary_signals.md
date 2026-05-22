# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T06:18:15.341735+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.51` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0262` n `12`; crypto_alt avg `0.0836` n `228`; crypto_major avg `0.075` n `8`; equity avg `0.0555` n `67`; fx avg `-0.0081` n `6`; index avg `0.0083` n `23`; metal avg `-0.0401` n `18`; unknown avg `-0.2505` n `386`
- 1h: commodity avg `0.1799` n `12`; crypto_alt avg `-0.3256` n `228`; crypto_major avg `-0.2133` n `8`; equity avg `-0.1264` n `67`; fx avg `0.003` n `6`; index avg `-0.0009` n `23`; metal avg `-0.2114` n `18`; unknown avg `-0.2777` n `376`
- 4h: commodity avg `0.1869` n `12`; crypto_alt avg `0.1696` n `228`; crypto_major avg `-0.2817` n `8`; equity avg `0.2656` n `67`; fx avg `0.072` n `6`; index avg `0.1168` n `23`; metal avg `0.011` n `18`; unknown avg `-0.3322` n `376`
- 24h: commodity avg `-0.4986` n `12`; crypto_alt avg `1.8256` n `228`; crypto_major avg `0.2303` n `8`; equity avg `1.3699` n `66`; fx avg `0.0842` n `6`; index avg `0.6668` n `23`; metal avg `0.3981` n `18`; unknown avg `2.2403` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0443`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0429`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0414`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0414`, n `668`, weak_sample_signal
