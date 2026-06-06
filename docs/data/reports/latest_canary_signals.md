# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T14:37:24.503734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6338` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0167` n `12`; crypto_alt avg `-0.1324` n `228`; crypto_major avg `0.0338` n `8`; equity avg `-0.0124` n `74`; fx avg `-0.0014` n `6`; index avg `-0.0122` n `23`; metal avg `-0.0404` n `18`; unknown avg `1.2657` n `515`
- 1h: commodity avg `0.0978` n `12`; crypto_alt avg `0.3494` n `228`; crypto_major avg `0.4082` n `8`; equity avg `0.1238` n `74`; fx avg `-0.0034` n `6`; index avg `0.1114` n `23`; metal avg `-0.2206` n `18`; unknown avg `1.2113` n `513`
- 4h: commodity avg `0.2318` n `12`; crypto_alt avg `2.0081` n `228`; crypto_major avg `1.5574` n `8`; equity avg `1.0294` n `74`; fx avg `0.0093` n `6`; index avg `0.5893` n `23`; metal avg `-0.0764` n `18`; unknown avg `0.3426` n `411`
- 24h: commodity avg `-0.3319` n `12`; crypto_alt avg `-2.4538` n `228`; crypto_major avg `-2.3273` n `8`; equity avg `-4.2949` n `74`; fx avg `-0.1353` n `6`; index avg `-2.3215` n `23`; metal avg `-2.0894` n `18`; unknown avg `0.342` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
