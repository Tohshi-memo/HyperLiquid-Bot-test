# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T08:22:38.301177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `13`; crypto_alt avg `0.0979` n `239`; crypto_major avg `-0.0` n `8`; equity avg `0.0826` n `161`; fx avg `-0.0249` n `6`; index avg `-0.0` n `27`; metal avg `0.0094` n `20`; unknown avg `0.1118` n `1261`
- 1h: commodity avg `0.0394` n `13`; crypto_alt avg `0.2249` n `239`; crypto_major avg `0.2384` n `8`; equity avg `0.3975` n `161`; fx avg `-0.0343` n `6`; index avg `0.015` n `27`; metal avg `-0.0418` n `20`; unknown avg `0.2559` n `1237`
- 4h: commodity avg `-0.0179` n `13`; crypto_alt avg `-0.2766` n `239`; crypto_major avg `0.4663` n `8`; equity avg `0.7882` n `161`; fx avg `-0.0572` n `6`; index avg `0.0341` n `27`; metal avg `0.1775` n `20`; unknown avg `0.1912` n `1201`
- 24h: commodity avg `0.4738` n `13`; crypto_alt avg `-0.9353` n `239`; crypto_major avg `-1.9648` n `8`; equity avg `1.8838` n `161`; fx avg `-0.2142` n `6`; index avg `0.2025` n `27`; metal avg `-0.02` n `20`; unknown avg `1.0223` n `1158`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
