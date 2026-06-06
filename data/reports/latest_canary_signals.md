# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T16:22:21.648762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0275` n `12`; crypto_alt avg `-0.363` n `228`; crypto_major avg `-0.366` n `8`; equity avg `0.0437` n `74`; fx avg `0.0234` n `6`; index avg `0.0188` n `23`; metal avg `0.0145` n `18`; unknown avg `0.0346` n `515`
- 1h: commodity avg `0.0427` n `12`; crypto_alt avg `0.3508` n `228`; crypto_major avg `0.1741` n `8`; equity avg `0.09` n `74`; fx avg `0.0426` n `6`; index avg `0.0772` n `23`; metal avg `0.0792` n `18`; unknown avg `-3.4917` n `515`
- 4h: commodity avg `0.1242` n `12`; crypto_alt avg `0.0962` n `228`; crypto_major avg `-0.3735` n `8`; equity avg `0.1479` n `74`; fx avg `0.0439` n `6`; index avg `0.3574` n `23`; metal avg `-0.1324` n `18`; unknown avg `-0.391` n `415`
- 24h: commodity avg `0.2781` n `12`; crypto_alt avg `-1.8203` n `228`; crypto_major avg `-2.2038` n `8`; equity avg `-2.4902` n `74`; fx avg `-0.025` n `6`; index avg `-1.5673` n `23`; metal avg `-1.1445` n `18`; unknown avg `-0.4942` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
