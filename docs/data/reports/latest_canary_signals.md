# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T18:14:45.498665+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `13`; crypto_alt avg `0.1138` n `238`; crypto_major avg `0.0442` n `8`; equity avg `-0.0597` n `154`; fx avg `-0.0064` n `6`; index avg `-0.0054` n `27`; metal avg `-0.0027` n `20`; unknown avg `-0.012` n `1232`
- 1h: commodity avg `-0.0464` n `13`; crypto_alt avg `0.0283` n `238`; crypto_major avg `-0.0593` n `8`; equity avg `-0.0911` n `154`; fx avg `-0.0085` n `6`; index avg `0.0006` n `27`; metal avg `-0.0395` n `20`; unknown avg `-0.1396` n `1230`
- 4h: commodity avg `-0.2401` n `13`; crypto_alt avg `0.969` n `238`; crypto_major avg `0.8483` n `8`; equity avg `0.9923` n `154`; fx avg `-0.0456` n `6`; index avg `0.1903` n `27`; metal avg `0.1346` n `20`; unknown avg `8.4719` n `1194`
- 24h: commodity avg `-0.4723` n `13`; crypto_alt avg `0.3521` n `237`; crypto_major avg `0.6784` n `8`; equity avg `1.0622` n `154`; fx avg `-0.071` n `6`; index avg `0.341` n `27`; metal avg `0.08` n `20`; unknown avg `33.9005` n `1042`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2225`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1976`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.197`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
