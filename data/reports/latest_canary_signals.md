# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T22:22:34.762701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0248` n `13`; crypto_alt avg `-0.1055` n `239`; crypto_major avg `-0.1743` n `8`; equity avg `-0.3134` n `160`; fx avg `0.0001` n `6`; index avg `-0.0239` n `27`; metal avg `0.0019` n `20`; unknown avg `1.2883` n `1262`
- 1h: commodity avg `0.0047` n `13`; crypto_alt avg `0.2759` n `239`; crypto_major avg `0.0411` n `8`; equity avg `-0.1029` n `160`; fx avg `0.0075` n `6`; index avg `-0.0223` n `27`; metal avg `-0.0013` n `20`; unknown avg `1.2457` n `1250`
- 4h: commodity avg `0.1366` n `13`; crypto_alt avg `0.5097` n `239`; crypto_major avg `1.0034` n `8`; equity avg `1.1458` n `160`; fx avg `0.0047` n `6`; index avg `0.1075` n `27`; metal avg `0.1007` n `20`; unknown avg `1.254` n `1226`
- 24h: commodity avg `0.0473` n `13`; crypto_alt avg `-1.0008` n `239`; crypto_major avg `-2.37` n `8`; equity avg `-1.5186` n `160`; fx avg `-0.0932` n `6`; index avg `-0.2142` n `27`; metal avg `-0.655` n `20`; unknown avg `21.0274` n `1173`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2567`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1971`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
