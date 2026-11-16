# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T02:37:25.406662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `13`; crypto_alt avg `0.2849` n `239`; crypto_major avg `0.1304` n `8`; equity avg `0.0909` n `162`; fx avg `0.0006` n `6`; index avg `-0.0025` n `27`; metal avg `-0.027` n `20`; unknown avg `0.0003` n `1265`
- 1h: commodity avg `0.0066` n `13`; crypto_alt avg `1.295` n `239`; crypto_major avg `0.9098` n `8`; equity avg `0.6441` n `162`; fx avg `-0.0088` n `6`; index avg `0.0507` n `27`; metal avg `0.0702` n `20`; unknown avg `0.1816` n `1259`
- 4h: commodity avg `-0.2688` n `13`; crypto_alt avg `0.2043` n `239`; crypto_major avg `-0.0643` n `8`; equity avg `0.0743` n `162`; fx avg `-0.0157` n `6`; index avg `0.0124` n `27`; metal avg `-0.009` n `20`; unknown avg `-0.0152` n `1211`
- 24h: commodity avg `-0.4016` n `13`; crypto_alt avg `0.9735` n `239`; crypto_major avg `1.24` n `8`; equity avg `0.8997` n `162`; fx avg `-0.003` n `6`; index avg `0.0946` n `27`; metal avg `0.2525` n `20`; unknown avg `1.1306` n `1127`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
