# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T16:07:28.293192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1517` n `13`; crypto_alt avg `-0.066` n `239`; crypto_major avg `-0.0355` n `8`; equity avg `0.0914` n `161`; fx avg `0.0029` n `6`; index avg `0.0042` n `27`; metal avg `0.0245` n `20`; unknown avg `0.3653` n `1247`
- 1h: commodity avg `0.0822` n `13`; crypto_alt avg `0.5605` n `239`; crypto_major avg `0.7225` n `8`; equity avg `0.9768` n `161`; fx avg `0.0472` n `6`; index avg `0.1043` n `27`; metal avg `-0.0278` n `20`; unknown avg `0.2782` n `1243`
- 4h: commodity avg `0.2333` n `13`; crypto_alt avg `0.7542` n `239`; crypto_major avg `0.8778` n `8`; equity avg `1.2511` n `161`; fx avg `0.012` n `6`; index avg `0.0983` n `27`; metal avg `-0.2433` n `20`; unknown avg `-0.0613` n `1225`
- 24h: commodity avg `1.1196` n `13`; crypto_alt avg `1.2424` n `239`; crypto_major avg `1.7714` n `8`; equity avg `4.9958` n `161`; fx avg `-0.1168` n `6`; index avg `0.4366` n `27`; metal avg `0.2169` n `20`; unknown avg `2.4954` n `1153`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.3164`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
