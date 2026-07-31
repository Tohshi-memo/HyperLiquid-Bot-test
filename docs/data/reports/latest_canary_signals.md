# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T05:37:34.158253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0723` n `12`; crypto_alt avg `-0.0423` n `230`; crypto_major avg `-0.1182` n `8`; equity avg `-0.121` n `102`; fx avg `0.018` n `6`; index avg `-0.025` n `25`; metal avg `-0.0319` n `20`; unknown avg `0.1692` n `779`
- 1h: commodity avg `-0.1276` n `12`; crypto_alt avg `0.1081` n `230`; crypto_major avg `0.1494` n `8`; equity avg `0.3118` n `102`; fx avg `-0.0469` n `6`; index avg `0.091` n `25`; metal avg `-0.0281` n `20`; unknown avg `3.8904` n `779`
- 4h: commodity avg `-0.1583` n `12`; crypto_alt avg `-0.6341` n `230`; crypto_major avg `-0.6554` n `8`; equity avg `0.2802` n `102`; fx avg `0.0066` n `6`; index avg `0.0796` n `25`; metal avg `0.0153` n `20`; unknown avg `0.1238` n `779`
- 24h: commodity avg `-0.6464` n `12`; crypto_alt avg `0.0732` n `230`; crypto_major avg `0.8911` n `8`; equity avg `9.1802` n `102`; fx avg `-0.1042` n `6`; index avg `1.3226` n `25`; metal avg `0.6807` n `20`; unknown avg `0.0701` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
