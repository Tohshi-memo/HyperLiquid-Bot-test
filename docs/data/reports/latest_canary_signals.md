# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T18:14:45.548027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `0.1474` n `232`; crypto_major avg `0.0744` n `8`; equity avg `0.0221` n `134`; fx avg `-0.0052` n `6`; index avg `0.0063` n `26`; metal avg `0.0105` n `20`; unknown avg `142.0372` n `791`
- 1h: commodity avg `-0.0239` n `12`; crypto_alt avg `0.1797` n `232`; crypto_major avg `0.1723` n `8`; equity avg `0.0763` n `134`; fx avg `0.0026` n `6`; index avg `0.0065` n `26`; metal avg `0.027` n `20`; unknown avg `-0.2524` n `783`
- 4h: commodity avg `0.0014` n `12`; crypto_alt avg `-0.1481` n `232`; crypto_major avg `-0.3397` n `8`; equity avg `0.0477` n `134`; fx avg `-0.0295` n `6`; index avg `0.0085` n `26`; metal avg `0.0034` n `20`; unknown avg `144.8061` n `776`
- 24h: commodity avg `0.0722` n `12`; crypto_alt avg `1.2864` n `232`; crypto_major avg `-0.4223` n `8`; equity avg `0.2611` n `134`; fx avg `-0.0215` n `6`; index avg `0.0209` n `26`; metal avg `-0.0345` n `20`; unknown avg `2.4345` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
