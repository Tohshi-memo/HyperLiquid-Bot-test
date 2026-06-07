# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T20:22:22.594319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2771` n `12`; crypto_alt avg `0.4911` n `228`; crypto_major avg `0.5558` n `8`; equity avg `0.1184` n `74`; fx avg `-0.0014` n `6`; index avg `0.1025` n `23`; metal avg `0.0522` n `18`; unknown avg `0.3885` n `516`
- 1h: commodity avg `-0.5165` n `12`; crypto_alt avg `0.5771` n `228`; crypto_major avg `0.6264` n `8`; equity avg `-0.0094` n `74`; fx avg `-0.0032` n `6`; index avg `0.01` n `23`; metal avg `-0.0841` n `18`; unknown avg `0.2013` n `516`
- 4h: commodity avg `0.1067` n `12`; crypto_alt avg `-1.0162` n `228`; crypto_major avg `-0.2966` n `8`; equity avg `-0.6678` n `74`; fx avg `0.0136` n `6`; index avg `-0.1718` n `23`; metal avg `-0.2127` n `18`; unknown avg `-2.3231` n `516`
- 24h: commodity avg `0.3665` n `12`; crypto_alt avg `2.2322` n `228`; crypto_major avg `3.5144` n `8`; equity avg `1.157` n `74`; fx avg `-0.0586` n `6`; index avg `0.3121` n `23`; metal avg `0.3477` n `18`; unknown avg `-4.4342` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
