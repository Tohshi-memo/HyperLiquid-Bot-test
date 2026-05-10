# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T01:22:16.004228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `12`; crypto_alt avg `-0.0218` n `228`; crypto_major avg `0.0014` n `8`; equity avg `0.0529` n `65`; fx avg `0.0` n `5`; index avg `0.0047` n `23`; metal avg `0.0035` n `18`; unknown avg `-0.097` n `376`
- 1h: commodity avg `0.035` n `12`; crypto_alt avg `-0.6202` n `228`; crypto_major avg `-0.4371` n `8`; equity avg `-0.0326` n `65`; fx avg `0.0002` n `5`; index avg `0.0373` n `23`; metal avg `-0.0046` n `18`; unknown avg `-0.2195` n `376`
- 4h: commodity avg `-0.0345` n `12`; crypto_alt avg `-0.94` n `228`; crypto_major avg `-0.5035` n `8`; equity avg `0.1038` n `65`; fx avg `0.0002` n `5`; index avg `0.1412` n `23`; metal avg `0.0782` n `18`; unknown avg `-0.4438` n `376`
- 24h: commodity avg `0.5464` n `12`; crypto_alt avg `-1.6887` n `228`; crypto_major avg `-0.6093` n `8`; equity avg `0.6449` n `65`; fx avg `-0.0083` n `5`; index avg `0.4083` n `23`; metal avg `0.2272` n `18`; unknown avg `-0.5122` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
