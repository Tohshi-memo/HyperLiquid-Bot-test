# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T05:01:05.340363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `13`; crypto_alt avg `0.341` n `237`; crypto_major avg `0.1821` n `8`; equity avg `0.1895` n `152`; fx avg `-0.0055` n `6`; index avg `0.0306` n `26`; metal avg `0.0164` n `20`; unknown avg `0.1284` n `1238`
- 1h: commodity avg `0.0128` n `13`; crypto_alt avg `1.0499` n `237`; crypto_major avg `0.7379` n `8`; equity avg `0.4156` n `152`; fx avg `0.0028` n `6`; index avg `0.0617` n `26`; metal avg `0.0592` n `20`; unknown avg `1.9222` n `1236`
- 4h: commodity avg `-0.1324` n `13`; crypto_alt avg `0.1832` n `237`; crypto_major avg `0.1299` n `8`; equity avg `0.2614` n `152`; fx avg `-0.012` n `6`; index avg `0.1126` n `26`; metal avg `0.1897` n `20`; unknown avg `0.4471` n `1222`
- 24h: commodity avg `-0.62` n `13`; crypto_alt avg `-0.8107` n `237`; crypto_major avg `-0.9189` n `8`; equity avg `-0.3544` n `152`; fx avg `0.0441` n `6`; index avg `0.0622` n `26`; metal avg `0.1966` n `20`; unknown avg `-0.2779` n `983`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2532`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2014`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
