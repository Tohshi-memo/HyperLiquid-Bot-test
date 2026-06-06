# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T01:37:24.091715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0315` n `12`; crypto_alt avg `0.4086` n `228`; crypto_major avg `0.3762` n `8`; equity avg `-0.1722` n `74`; fx avg `-0.0135` n `6`; index avg `-0.1515` n `23`; metal avg `-0.0373` n `18`; unknown avg `0.1428` n `425`
- 1h: commodity avg `-0.0943` n `12`; crypto_alt avg `-0.2244` n `228`; crypto_major avg `-0.1645` n `8`; equity avg `-0.5363` n `74`; fx avg `-0.0231` n `6`; index avg `-0.228` n `23`; metal avg `-0.0322` n `18`; unknown avg `-0.1483` n `425`
- 4h: commodity avg `0.6704` n `12`; crypto_alt avg `-0.9796` n `228`; crypto_major avg `-0.7619` n `8`; equity avg `-0.8818` n `74`; fx avg `-0.0343` n `6`; index avg `-0.1605` n `23`; metal avg `-0.1859` n `18`; unknown avg `1.1405` n `425`
- 24h: commodity avg `-1.06` n `12`; crypto_alt avg `-6.1137` n `228`; crypto_major avg `-5.3298` n `8`; equity avg `-5.7358` n `74`; fx avg `-0.2183` n `6`; index avg `-3.6198` n `23`; metal avg `-3.851` n `18`; unknown avg `-0.5697` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
