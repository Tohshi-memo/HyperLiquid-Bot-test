# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T18:07:33.556616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0204` n `13`; crypto_alt avg `-0.1652` n `239`; crypto_major avg `-0.0092` n `8`; equity avg `-0.2526` n `164`; fx avg `-0.0037` n `6`; index avg `-0.0285` n `27`; metal avg `0.0713` n `20`; unknown avg `0.1392` n `1259`
- 1h: commodity avg `0.0505` n `13`; crypto_alt avg `0.0761` n `239`; crypto_major avg `0.3663` n `8`; equity avg `0.1897` n `164`; fx avg `0.0065` n `6`; index avg `-0.0013` n `27`; metal avg `0.0521` n `20`; unknown avg `0.4556` n `1263`
- 4h: commodity avg `-0.4257` n `13`; crypto_alt avg `-1.0272` n `239`; crypto_major avg `-1.041` n `8`; equity avg `-1.2511` n `164`; fx avg `-0.0292` n `6`; index avg `-0.102` n `27`; metal avg `-0.2596` n `20`; unknown avg `1.1341` n `1257`
- 24h: commodity avg `-0.4949` n `13`; crypto_alt avg `0.3826` n `239`; crypto_major avg `-0.0972` n `8`; equity avg `0.4158` n `164`; fx avg `-0.1916` n `6`; index avg `0.0461` n `27`; metal avg `-1.156` n `20`; unknown avg `-0.0245` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
