# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T03:37:29.455706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `13`; crypto_alt avg `-0.1922` n `239`; crypto_major avg `-0.1552` n `8`; equity avg `-0.0457` n `161`; fx avg `0.0094` n `6`; index avg `-0.0001` n `27`; metal avg `-0.0218` n `20`; unknown avg `-0.1147` n `1261`
- 1h: commodity avg `-0.0112` n `13`; crypto_alt avg `0.1991` n `239`; crypto_major avg `0.2999` n `8`; equity avg `0.4057` n `161`; fx avg `-0.0121` n `6`; index avg `0.054` n `27`; metal avg `0.0127` n `20`; unknown avg `2.3142` n `1255`
- 4h: commodity avg `0.0495` n `13`; crypto_alt avg `0.5748` n `239`; crypto_major avg `0.2448` n `8`; equity avg `1.7305` n `161`; fx avg `-0.083` n `6`; index avg `0.2164` n `27`; metal avg `0.2691` n `20`; unknown avg `6.3` n `1249`
- 24h: commodity avg `0.3378` n `13`; crypto_alt avg `0.162` n `239`; crypto_major avg `-1.736` n `8`; equity avg `1.4064` n `161`; fx avg `-0.2262` n `6`; index avg `0.2121` n `27`; metal avg `-0.2522` n `20`; unknown avg `24.7459` n `1172`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3184`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2902`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
