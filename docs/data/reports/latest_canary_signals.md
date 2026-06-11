# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T07:22:30.288826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `0.3606` n `228`; crypto_major avg `0.2577` n `8`; equity avg `0.2005` n `74`; fx avg `-0.003` n `6`; index avg `0.13` n `23`; metal avg `0.2537` n `18`; unknown avg `0.1105` n `548`
- 1h: commodity avg `-0.3491` n `12`; crypto_alt avg `-0.0431` n `228`; crypto_major avg `-0.171` n `8`; equity avg `0.2474` n `74`; fx avg `0.0344` n `6`; index avg `0.1173` n `23`; metal avg `0.3654` n `18`; unknown avg `-0.0869` n `546`
- 4h: commodity avg `-0.646` n `12`; crypto_alt avg `1.5227` n `228`; crypto_major avg `1.2059` n `8`; equity avg `1.0949` n `74`; fx avg `0.0778` n `6`; index avg `0.5596` n `23`; metal avg `1.0194` n `18`; unknown avg `0.4587` n `530`
- 24h: commodity avg `0.9759` n `12`; crypto_alt avg `0.7362` n `228`; crypto_major avg `0.8737` n `8`; equity avg `-0.1644` n `74`; fx avg `0.0309` n `6`; index avg `-0.4239` n `23`; metal avg `-0.4961` n `18`; unknown avg `3.7822` n `527`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
