# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T00:07:31.336437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `13`; crypto_alt avg `0.0957` n `239`; crypto_major avg `0.0627` n `8`; equity avg `-0.0107` n `160`; fx avg `-0.0296` n `6`; index avg `0.0112` n `27`; metal avg `0.0071` n `20`; unknown avg `0.3517` n `1254`
- 1h: commodity avg `-0.0269` n `13`; crypto_alt avg `0.6542` n `239`; crypto_major avg `0.4666` n `8`; equity avg `0.536` n `160`; fx avg `-0.0404` n `6`; index avg `0.0762` n `27`; metal avg `0.0534` n `20`; unknown avg `0.4855` n `1250`
- 4h: commodity avg `-0.0461` n `13`; crypto_alt avg `0.8833` n `239`; crypto_major avg `0.5306` n `8`; equity avg `1.3664` n `160`; fx avg `-0.0343` n `6`; index avg `0.1391` n `27`; metal avg `0.1019` n `20`; unknown avg `1.8186` n `1228`
- 24h: commodity avg `0.0827` n `13`; crypto_alt avg `-0.6617` n `239`; crypto_major avg `-2.7478` n `8`; equity avg `-1.1364` n `160`; fx avg `-0.1855` n `6`; index avg `-0.0978` n `27`; metal avg `-0.552` n `20`; unknown avg `21.1487` n `1173`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2582`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
