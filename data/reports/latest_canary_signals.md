# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T04:52:27.328825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0166` n `13`; crypto_alt avg `-0.046` n `239`; crypto_major avg `0.0209` n `8`; equity avg `-0.0675` n `161`; fx avg `-0.007` n `6`; index avg `-0.0047` n `27`; metal avg `0.0286` n `20`; unknown avg `-0.1668` n `1261`
- 1h: commodity avg `-0.0295` n `13`; crypto_alt avg `-0.0482` n `239`; crypto_major avg `-0.0712` n `8`; equity avg `0.1525` n `161`; fx avg `0.0056` n `6`; index avg `0.0164` n `27`; metal avg `0.0032` n `20`; unknown avg `18.8926` n `1245`
- 4h: commodity avg `0.0145` n `13`; crypto_alt avg `0.426` n `239`; crypto_major avg `0.3238` n `8`; equity avg `1.5829` n `161`; fx avg `-0.0211` n `6`; index avg `0.1902` n `27`; metal avg `0.3141` n `20`; unknown avg `5.5577` n `1245`
- 24h: commodity avg `0.3029` n `13`; crypto_alt avg `-0.14` n `239`; crypto_major avg `-1.9954` n `8`; equity avg `1.5013` n `161`; fx avg `-0.2168` n `6`; index avg `0.2473` n `27`; metal avg `-0.2498` n `20`; unknown avg `44.4077` n `1174`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3419`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.317`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.175`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
