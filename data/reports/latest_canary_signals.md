# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T05:07:30.866794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0398` n `13`; crypto_alt avg `-0.2813` n `239`; crypto_major avg `-0.1787` n `8`; equity avg `0.0428` n `161`; fx avg `-0.0315` n `6`; index avg `0.0086` n `27`; metal avg `0.0657` n `20`; unknown avg `66.8809` n `1257`
- 1h: commodity avg `-0.0544` n `13`; crypto_alt avg `-0.3355` n `239`; crypto_major avg `-0.2824` n `8`; equity avg `-0.0234` n `161`; fx avg `-0.0362` n `6`; index avg `0.0009` n `27`; metal avg `0.0517` n `20`; unknown avg `2.9915` n `1253`
- 4h: commodity avg `-0.0423` n `13`; crypto_alt avg `0.3174` n `239`; crypto_major avg `0.328` n `8`; equity avg `1.4929` n `161`; fx avg `-0.064` n `6`; index avg `0.2024` n `27`; metal avg `0.3578` n `20`; unknown avg `10.6052` n `1245`
- 24h: commodity avg `0.2664` n `13`; crypto_alt avg `-0.5857` n `239`; crypto_major avg `-2.4319` n `8`; equity avg `1.5549` n `161`; fx avg `-0.2535` n `6`; index avg `0.2555` n `27`; metal avg `-0.1715` n `20`; unknown avg `24.3054` n `1174`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3353`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.31`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
