# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T05:22:24.681326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `13`; crypto_alt avg `0.0813` n `239`; crypto_major avg `0.1959` n `8`; equity avg `0.1135` n `161`; fx avg `0.0001` n `6`; index avg `0.0096` n `27`; metal avg `0.0334` n `20`; unknown avg `-0.0494` n `1261`
- 1h: commodity avg `-0.0535` n `13`; crypto_alt avg `0.1387` n `239`; crypto_major avg `0.4386` n `8`; equity avg `0.2822` n `161`; fx avg `-0.0252` n `6`; index avg `0.0332` n `27`; metal avg `0.1392` n `20`; unknown avg `38.2596` n `1253`
- 4h: commodity avg `0.024` n `13`; crypto_alt avg `0.2846` n `239`; crypto_major avg `0.3968` n `8`; equity avg `1.2183` n `161`; fx avg `-0.0734` n `6`; index avg `0.1726` n `27`; metal avg `0.3037` n `20`; unknown avg `9.0285` n `1245`
- 24h: commodity avg `0.2266` n `13`; crypto_alt avg `-0.4201` n `239`; crypto_major avg `-2.2783` n `8`; equity avg `1.4549` n `161`; fx avg `-0.2197` n `6`; index avg `0.2165` n `27`; metal avg `-0.2081` n `20`; unknown avg `24.4026` n `1174`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3309`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3049`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
