# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T00:52:25.716497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `-0.3261` n `232`; crypto_major avg `-0.3633` n `8`; equity avg `0.0788` n `133`; fx avg `-0.0149` n `6`; index avg `0.0097` n `26`; metal avg `0.011` n `20`; unknown avg `0.1689` n `793`
- 1h: commodity avg `-0.0621` n `12`; crypto_alt avg `-0.0995` n `232`; crypto_major avg `-0.2081` n `8`; equity avg `0.3237` n `133`; fx avg `0.017` n `6`; index avg `0.0227` n `26`; metal avg `0.0076` n `20`; unknown avg `13.4901` n `784`
- 4h: commodity avg `-0.0434` n `12`; crypto_alt avg `-0.344` n `232`; crypto_major avg `-0.3435` n `8`; equity avg `0.3388` n `133`; fx avg `0.01` n `6`; index avg `0.0225` n `26`; metal avg `0.008` n `20`; unknown avg `1.4688` n `778`
- 24h: commodity avg `-0.1797` n `12`; crypto_alt avg `3.9501` n `232`; crypto_major avg `5.2098` n `8`; equity avg `1.6417` n `133`; fx avg `-0.209` n `6`; index avg `0.2398` n `26`; metal avg `0.7791` n `20`; unknown avg `23.5288` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
