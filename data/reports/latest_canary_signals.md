# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T14:52:21.971852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0679` n `12`; crypto_alt avg `-0.0263` n `228`; crypto_major avg `0.03` n `8`; equity avg `0.0156` n `74`; fx avg `0.005` n `6`; index avg `-0.025` n `23`; metal avg `-0.0226` n `18`; unknown avg `0.0097` n `515`
- 1h: commodity avg `0.1301` n `12`; crypto_alt avg `0.3749` n `228`; crypto_major avg `0.4287` n `8`; equity avg `0.1569` n `74`; fx avg `0.0034` n `6`; index avg `0.067` n `23`; metal avg `-0.2546` n `18`; unknown avg `3.1368` n `515`
- 4h: commodity avg `0.3095` n `12`; crypto_alt avg `1.6638` n `228`; crypto_major avg `1.409` n `8`; equity avg `1.0212` n `74`; fx avg `0.0143` n `6`; index avg `0.5686` n `23`; metal avg `-0.0905` n `18`; unknown avg `0.3858` n `411`
- 24h: commodity avg `-0.173` n `12`; crypto_alt avg `-1.9602` n `228`; crypto_major avg `-1.5297` n `8`; equity avg `-4.0502` n `74`; fx avg `-0.1299` n `6`; index avg `-2.2514` n `23`; metal avg `-2.0455` n `18`; unknown avg `-0.0867` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
