# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T22:07:43.793388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `13`; crypto_alt avg `0.0278` n `239`; crypto_major avg `0.0433` n `8`; equity avg `-0.1688` n `161`; fx avg `0.0488` n `6`; index avg `-0.0157` n `27`; metal avg `0.0222` n `20`; unknown avg `3.8937` n `1250`
- 1h: commodity avg `0.022` n `13`; crypto_alt avg `-0.225` n `239`; crypto_major avg `-0.2141` n `8`; equity avg `-0.0718` n `161`; fx avg `-0.0024` n `6`; index avg `-0.0122` n `27`; metal avg `0.0165` n `20`; unknown avg `2.337` n `1246`
- 4h: commodity avg `-0.1578` n `13`; crypto_alt avg `-0.7066` n `239`; crypto_major avg `-0.4341` n `8`; equity avg `-0.8982` n `161`; fx avg `0.0151` n `6`; index avg `-0.0617` n `27`; metal avg `-0.0998` n `20`; unknown avg `4.8612` n `1204`
- 24h: commodity avg `0.2361` n `13`; crypto_alt avg `-0.0865` n `239`; crypto_major avg `0.5409` n `8`; equity avg `4.2637` n `161`; fx avg `-0.1435` n `6`; index avg `0.4335` n `27`; metal avg `-0.0584` n `20`; unknown avg `5.9284` n `1141`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
