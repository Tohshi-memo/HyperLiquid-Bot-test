# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T05:37:34.224943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `12`; crypto_alt avg `0.0291` n `232`; crypto_major avg `0.078` n `8`; equity avg `0.0143` n `134`; fx avg `-0.0205` n `6`; index avg `0.0127` n `26`; metal avg `0.0519` n `20`; unknown avg `-0.1438` n `794`
- 1h: commodity avg `0.0371` n `12`; crypto_alt avg `0.5601` n `232`; crypto_major avg `0.5349` n `8`; equity avg `0.018` n `134`; fx avg `-0.0446` n `6`; index avg `0.0169` n `26`; metal avg `0.0961` n `20`; unknown avg `0.6704` n `792`
- 4h: commodity avg `0.142` n `12`; crypto_alt avg `0.3061` n `232`; crypto_major avg `0.1232` n `8`; equity avg `0.2956` n `134`; fx avg `0.0505` n `6`; index avg `0.0005` n `26`; metal avg `-0.0396` n `20`; unknown avg `1.9166` n `758`
- 24h: commodity avg `0.1002` n `12`; crypto_alt avg `0.1205` n `232`; crypto_major avg `-0.6741` n `8`; equity avg `0.4299` n `134`; fx avg `-0.0231` n `6`; index avg `0.0158` n `26`; metal avg `-0.1316` n `20`; unknown avg `72.9765` n `658`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
