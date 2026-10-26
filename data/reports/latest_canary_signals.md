# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T21:52:49.856171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `13`; crypto_alt avg `0.0183` n `237`; crypto_major avg `0.0295` n `8`; equity avg `0.038` n `154`; fx avg `-0.0022` n `6`; index avg `0.0084` n `27`; metal avg `-0.0062` n `20`; unknown avg `0.0365` n `1238`
- 1h: commodity avg `0.0017` n `13`; crypto_alt avg `0.2567` n `237`; crypto_major avg `0.2143` n `8`; equity avg `0.2061` n `154`; fx avg `-0.0056` n `6`; index avg `0.0223` n `27`; metal avg `0.0113` n `20`; unknown avg `131.7827` n `1228`
- 4h: commodity avg `-0.2064` n `13`; crypto_alt avg `-0.4031` n `237`; crypto_major avg `-0.4825` n `8`; equity avg `-0.1715` n `154`; fx avg `-0.0405` n `6`; index avg `-0.0063` n `27`; metal avg `-0.0414` n `20`; unknown avg `10.0218` n `1134`
- 24h: commodity avg `-0.2341` n `13`; crypto_alt avg `0.1433` n `237`; crypto_major avg `0.2053` n `8`; equity avg `0.8904` n `153`; fx avg `-0.0273` n `6`; index avg `-0.0587` n `27`; metal avg `-0.0216` n `20`; unknown avg `704.9698` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1836`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
