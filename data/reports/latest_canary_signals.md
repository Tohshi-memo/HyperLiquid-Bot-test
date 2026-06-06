# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T23:07:24.773284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0908` n `12`; crypto_alt avg `0.193` n `228`; crypto_major avg `0.1213` n `8`; equity avg `0.0973` n `74`; fx avg `-0.0028` n `6`; index avg `0.0196` n `23`; metal avg `-0.0004` n `18`; unknown avg `-0.0291` n `515`
- 1h: commodity avg `-0.0134` n `12`; crypto_alt avg `0.3575` n `228`; crypto_major avg `0.3281` n `8`; equity avg `0.0949` n `74`; fx avg `-0.0141` n `6`; index avg `-0.004` n `23`; metal avg `-0.0095` n `18`; unknown avg `-0.0518` n `515`
- 4h: commodity avg `0.1447` n `12`; crypto_alt avg `0.1564` n `228`; crypto_major avg `0.0032` n `8`; equity avg `0.19` n `74`; fx avg `-0.0671` n `6`; index avg `0.0448` n `23`; metal avg `-0.0057` n `18`; unknown avg `-0.2954` n `515`
- 24h: commodity avg `0.2214` n `12`; crypto_alt avg `-2.0464` n `228`; crypto_major avg `-2.1405` n `8`; equity avg `-0.7956` n `74`; fx avg `0.0158` n `6`; index avg `0.0663` n `23`; metal avg `-0.5251` n `18`; unknown avg `0.6851` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
