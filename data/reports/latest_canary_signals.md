# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T22:04:43.912449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0528` n `12`; crypto_alt avg `-0.9262` n `228`; crypto_major avg `-0.9119` n `8`; equity avg `0.0511` n `74`; fx avg `0.005` n `6`; index avg `0.0115` n `23`; metal avg `-0.0255` n `18`; unknown avg `0.688` n `425`
- 1h: commodity avg `-0.5864` n `12`; crypto_alt avg `-0.287` n `228`; crypto_major avg `-0.4379` n `8`; equity avg `0.524` n `74`; fx avg `0.0258` n `6`; index avg `0.3192` n `23`; metal avg `0.0668` n `18`; unknown avg `0.9513` n `425`
- 4h: commodity avg `-0.251` n `12`; crypto_alt avg `-0.0438` n `228`; crypto_major avg `0.0202` n `8`; equity avg `-0.2673` n `74`; fx avg `0.0069` n `6`; index avg `-0.8411` n `23`; metal avg `-0.4138` n `18`; unknown avg `0.164` n `424`
- 24h: commodity avg `-1.8253` n `12`; crypto_alt avg `-5.2436` n `228`; crypto_major avg `-4.8514` n `8`; equity avg `-5.8308` n `74`; fx avg `-0.0402` n `6`; index avg `-4.2069` n `23`; metal avg `-4.4235` n `18`; unknown avg `-0.386` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
