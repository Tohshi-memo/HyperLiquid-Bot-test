# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T05:52:24.159301+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1056` n `12`; crypto_alt avg `0.4743` n `228`; crypto_major avg `0.4474` n `8`; equity avg `0.2156` n `74`; fx avg `-0.0007` n `6`; index avg `0.1109` n `23`; metal avg `0.088` n `18`; unknown avg `-0.3841` n `425`
- 1h: commodity avg `0.1145` n `12`; crypto_alt avg `1.9196` n `228`; crypto_major avg `1.5951` n `8`; equity avg `0.6624` n `74`; fx avg `-0.0065` n `6`; index avg `0.2499` n `23`; metal avg `0.1963` n `18`; unknown avg `4.1028` n `425`
- 4h: commodity avg `-0.2126` n `12`; crypto_alt avg `-2.0745` n `228`; crypto_major avg `-1.0275` n `8`; equity avg `-0.4497` n `74`; fx avg `-0.0143` n `6`; index avg `-0.3151` n `23`; metal avg `-0.4248` n `18`; unknown avg `-0.2435` n `425`
- 24h: commodity avg `-1.4186` n `12`; crypto_alt avg `-6.2086` n `228`; crypto_major avg `-4.1252` n `8`; equity avg `-6.5993` n `74`; fx avg `-0.1953` n `6`; index avg `-4.1505` n `23`; metal avg `-4.1774` n `18`; unknown avg `-0.7201` n `404`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
