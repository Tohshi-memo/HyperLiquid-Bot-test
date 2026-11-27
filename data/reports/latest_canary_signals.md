# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T19:22:35.177714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0952` n `13`; crypto_alt avg `0.1102` n `239`; crypto_major avg `0.13` n `8`; equity avg `0.1014` n `168`; fx avg `-0.0055` n `6`; index avg `0.0062` n `27`; metal avg `0.0258` n `20`; unknown avg `61.7764` n `1263`
- 1h: commodity avg `0.0101` n `13`; crypto_alt avg `-0.0095` n `239`; crypto_major avg `0.1185` n `8`; equity avg `-0.2134` n `168`; fx avg `0.0019` n `6`; index avg `-0.0071` n `27`; metal avg `-0.0512` n `20`; unknown avg `165.1653` n `1240`
- 4h: commodity avg `-0.2231` n `13`; crypto_alt avg `0.8219` n `239`; crypto_major avg `0.6627` n `8`; equity avg `1.499` n `168`; fx avg `-0.0375` n `6`; index avg `0.1644` n `27`; metal avg `0.1006` n `20`; unknown avg `166.4654` n `1230`
- 24h: commodity avg `-0.5196` n `13`; crypto_alt avg `-0.0823` n `239`; crypto_major avg `0.2221` n `8`; equity avg `3.3091` n `168`; fx avg `-0.1473` n `6`; index avg `0.3192` n `27`; metal avg `0.8525` n `20`; unknown avg `309.3686` n `1045`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
