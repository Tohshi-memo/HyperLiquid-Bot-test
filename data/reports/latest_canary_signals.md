# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T05:52:36.450796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0703` n `13`; crypto_alt avg `0.1088` n `239`; crypto_major avg `-0.0148` n `8`; equity avg `-0.0411` n `166`; fx avg `-0.0137` n `6`; index avg `0.0006` n `27`; metal avg `-0.0523` n `20`; unknown avg `0.4777` n `1266`
- 1h: commodity avg `0.0544` n `13`; crypto_alt avg `0.9905` n `239`; crypto_major avg `0.6302` n `8`; equity avg `0.2477` n `166`; fx avg `0.0265` n `6`; index avg `0.0398` n `27`; metal avg `-0.0251` n `20`; unknown avg `0.4597` n `1260`
- 4h: commodity avg `-0.0232` n `13`; crypto_alt avg `0.7459` n `239`; crypto_major avg `0.0302` n `8`; equity avg `-0.3286` n `166`; fx avg `-0.0341` n `6`; index avg `0.0275` n `27`; metal avg `-0.4712` n `20`; unknown avg `322.7485` n `1238`
- 24h: commodity avg `-1.2732` n `13`; crypto_alt avg `1.1016` n `239`; crypto_major avg `0.2273` n `8`; equity avg `4.3606` n `166`; fx avg `-0.2474` n `6`; index avg `0.6427` n `27`; metal avg `-0.2057` n `20`; unknown avg `333.5416` n `1032`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
