# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T00:38:40.354300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `12`; crypto_alt avg `0.1263` n `232`; crypto_major avg `0.0884` n `8`; equity avg `0.0039` n `134`; fx avg `0.0088` n `6`; index avg `-0.003` n `26`; metal avg `0.0062` n `20`; unknown avg `0.4822` n `788`
- 1h: commodity avg `-0.0062` n `12`; crypto_alt avg `0.4043` n `232`; crypto_major avg `0.2388` n `8`; equity avg `0.0242` n `134`; fx avg `-0.0012` n `6`; index avg `-0.0031` n `26`; metal avg `-0.0022` n `20`; unknown avg `-0.3963` n `786`
- 4h: commodity avg `0.022` n `12`; crypto_alt avg `0.7049` n `232`; crypto_major avg `0.0001` n `8`; equity avg `0.1052` n `134`; fx avg `-0.0134` n `6`; index avg `-0.0048` n `26`; metal avg `-0.0021` n `20`; unknown avg `-0.1676` n `782`
- 24h: commodity avg `0.1712` n `12`; crypto_alt avg `3.1342` n `232`; crypto_major avg `2.4052` n `8`; equity avg `0.3312` n `134`; fx avg `-0.0575` n `6`; index avg `0.0708` n `26`; metal avg `0.0617` n `20`; unknown avg `0.1035` n `694`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
