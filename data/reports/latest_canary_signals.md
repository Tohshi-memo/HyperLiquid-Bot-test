# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T14:22:41.772849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.43` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0028` n `13`; crypto_alt avg `0.1685` n `239`; crypto_major avg `0.2924` n `8`; equity avg `0.0788` n `168`; fx avg `0.0121` n `6`; index avg `0.0036` n `27`; metal avg `0.0175` n `20`; unknown avg `3.8029` n `1263`
- 1h: commodity avg `0.0146` n `13`; crypto_alt avg `-0.152` n `239`; crypto_major avg `0.041` n `8`; equity avg `-0.1188` n `168`; fx avg `0.0206` n `6`; index avg `-0.0099` n `27`; metal avg `-0.0108` n `20`; unknown avg `1.0013` n `1255`
- 4h: commodity avg `0.0043` n `13`; crypto_alt avg `-0.5663` n `239`; crypto_major avg `-0.1811` n `8`; equity avg `-0.31` n `168`; fx avg `-0.002` n `6`; index avg `-0.0287` n `27`; metal avg `-0.0103` n `20`; unknown avg `5.2486` n `1245`
- 24h: commodity avg `-0.2713` n `13`; crypto_alt avg `-3.7531` n `239`; crypto_major avg `-3.1346` n `8`; equity avg `-0.0982` n `168`; fx avg `-0.0694` n `6`; index avg `0.0445` n `27`; metal avg `0.1485` n `20`; unknown avg `192.5758` n `1090`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
