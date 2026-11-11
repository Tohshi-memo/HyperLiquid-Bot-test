# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T05:37:25.326695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `13`; crypto_alt avg `-0.189` n `239`; crypto_major avg `-0.069` n `8`; equity avg `0.0019` n `161`; fx avg `-0.0069` n `6`; index avg `0.0036` n `27`; metal avg `0.0546` n `20`; unknown avg `-0.205` n `1259`
- 1h: commodity avg `-0.0609` n `13`; crypto_alt avg `-0.4365` n `239`; crypto_major avg `-0.0314` n `8`; equity avg `0.0909` n `161`; fx avg `-0.0452` n `6`; index avg `0.0171` n `27`; metal avg `0.1827` n `20`; unknown avg `29.0076` n `1253`
- 4h: commodity avg `0.0399` n `13`; crypto_alt avg `-0.3708` n `239`; crypto_major avg `-0.2694` n `8`; equity avg `0.7286` n `161`; fx avg `-0.0687` n `6`; index avg `0.1114` n `27`; metal avg `0.2066` n `20`; unknown avg `8.886` n `1243`
- 24h: commodity avg `0.0917` n `13`; crypto_alt avg `-0.7493` n `239`; crypto_major avg `-2.4812` n `8`; equity avg `1.2442` n `161`; fx avg `-0.1872` n `6`; index avg `0.181` n `27`; metal avg `-0.1483` n `20`; unknown avg `24.1284` n `1172`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3213`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2945`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
