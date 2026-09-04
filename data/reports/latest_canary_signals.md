# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T02:52:24.523125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `12`; crypto_alt avg `0.1683` n `232`; crypto_major avg `0.0683` n `8`; equity avg `0.0406` n `133`; fx avg `0.0027` n `6`; index avg `0.0152` n `26`; metal avg `0.023` n `20`; unknown avg `0.6238` n `793`
- 1h: commodity avg `-0.0484` n `12`; crypto_alt avg `0.1984` n `232`; crypto_major avg `-0.0256` n `8`; equity avg `0.1397` n `133`; fx avg `-0.032` n `6`; index avg `0.0282` n `26`; metal avg `0.0096` n `20`; unknown avg `3.8866` n `791`
- 4h: commodity avg `0.0062` n `12`; crypto_alt avg `0.0904` n `232`; crypto_major avg `-0.0487` n `8`; equity avg `0.3763` n `133`; fx avg `0.007` n `6`; index avg `0.0285` n `26`; metal avg `-0.0719` n `20`; unknown avg `2.3097` n `784`
- 24h: commodity avg `-0.1396` n `12`; crypto_alt avg `2.6956` n `232`; crypto_major avg `3.7509` n `8`; equity avg `1.4951` n `133`; fx avg `-0.1346` n `6`; index avg `0.2112` n `26`; metal avg `0.5895` n `20`; unknown avg `1.1013` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
