# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T15:37:33.405002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `13`; crypto_alt avg `0.1868` n `237`; crypto_major avg `0.087` n `8`; equity avg `0.0509` n `154`; fx avg `0.0051` n `6`; index avg `-0.0144` n `27`; metal avg `-0.0213` n `20`; unknown avg `-0.1704` n `1238`
- 1h: commodity avg `0.3321` n `13`; crypto_alt avg `1.0142` n `237`; crypto_major avg `0.8743` n `8`; equity avg `1.5746` n `154`; fx avg `0.0173` n `6`; index avg `0.1362` n `27`; metal avg `0.0996` n `20`; unknown avg `2.1203` n `1212`
- 4h: commodity avg `0.092` n `13`; crypto_alt avg `1.3191` n `237`; crypto_major avg `0.8911` n `8`; equity avg `1.8523` n `153`; fx avg `0.0231` n `6`; index avg `0.2664` n `27`; metal avg `0.1019` n `20`; unknown avg `629.836` n `1154`
- 24h: commodity avg `-0.1648` n `13`; crypto_alt avg `0.8178` n `237`; crypto_major avg `0.5702` n `8`; equity avg `1.2541` n `153`; fx avg `0.0669` n `6`; index avg `0.0033` n `27`; metal avg `0.1926` n `20`; unknown avg `806.0883` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2341`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
