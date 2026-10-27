# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T18:22:30.341457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `13`; crypto_alt avg `0.0843` n `238`; crypto_major avg `0.0015` n `8`; equity avg `-0.0379` n `154`; fx avg `-0.005` n `6`; index avg `-0.0086` n `27`; metal avg `-0.0296` n `20`; unknown avg `0.8726` n `1238`
- 1h: commodity avg `-0.0187` n `13`; crypto_alt avg `0.0849` n `238`; crypto_major avg `-0.1073` n `8`; equity avg `-0.1697` n `154`; fx avg `-0.0137` n `6`; index avg `-0.0089` n `27`; metal avg `-0.0687` n `20`; unknown avg `0.3975` n `1234`
- 4h: commodity avg `-0.1457` n `13`; crypto_alt avg `1.0912` n `238`; crypto_major avg `0.9773` n `8`; equity avg `1.0756` n `154`; fx avg `-0.0464` n `6`; index avg `0.1989` n `27`; metal avg `0.092` n `20`; unknown avg `14.8223` n `1196`
- 24h: commodity avg `-0.4438` n `13`; crypto_alt avg `0.6555` n `237`; crypto_major avg `0.7718` n `8`; equity avg `1.214` n `154`; fx avg `-0.0715` n `6`; index avg `0.3525` n `27`; metal avg `0.0602` n `20`; unknown avg `32.9844` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.197`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
