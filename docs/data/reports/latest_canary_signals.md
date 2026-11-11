# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T00:37:28.206720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `13`; crypto_alt avg `0.2116` n `239`; crypto_major avg `0.1492` n `8`; equity avg `0.0918` n `161`; fx avg `-0.0175` n `6`; index avg `0.0202` n `27`; metal avg `-0.0189` n `20`; unknown avg `0.314` n `1261`
- 1h: commodity avg `0.001` n `13`; crypto_alt avg `0.5097` n `239`; crypto_major avg `0.1879` n `8`; equity avg `0.127` n `161`; fx avg `-0.0734` n `6`; index avg `0.0402` n `27`; metal avg `0.0126` n `20`; unknown avg `0.6402` n `1249`
- 4h: commodity avg `-0.0595` n `13`; crypto_alt avg `1.1684` n `239`; crypto_major avg `0.4842` n `8`; equity avg `0.9955` n `161`; fx avg `-0.0623` n `6`; index avg `0.1174` n `27`; metal avg `0.0388` n `20`; unknown avg `1.9117` n `1227`
- 24h: commodity avg `0.0539` n `13`; crypto_alt avg `-0.1126` n `239`; crypto_major avg `-2.267` n `8`; equity avg `-0.9378` n `161`; fx avg `-0.2038` n `6`; index avg `-0.0565` n `27`; metal avg `-0.5017` n `20`; unknown avg `21.3403` n `1172`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2578`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
