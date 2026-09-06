# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T03:37:27.665087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `0.1661` n `232`; crypto_major avg `0.3832` n `8`; equity avg `0.0206` n `134`; fx avg `0.012` n `6`; index avg `-0.0102` n `26`; metal avg `0.013` n `20`; unknown avg `-0.0806` n `794`
- 1h: commodity avg `-0.0138` n `12`; crypto_alt avg `0.1023` n `232`; crypto_major avg `0.5286` n `8`; equity avg `0.0576` n `134`; fx avg `0.0057` n `6`; index avg `0.0073` n `26`; metal avg `0.0083` n `20`; unknown avg `8.8973` n `792`
- 4h: commodity avg `-0.0044` n `12`; crypto_alt avg `0.896` n `232`; crypto_major avg `0.9741` n `8`; equity avg `0.1302` n `134`; fx avg `0.0062` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0092` n `20`; unknown avg `1.2677` n `784`
- 24h: commodity avg `0.1292` n `12`; crypto_alt avg `3.0996` n `232`; crypto_major avg `3.0894` n `8`; equity avg `0.5187` n `134`; fx avg `-0.0611` n `6`; index avg `0.0674` n `26`; metal avg `0.0279` n `20`; unknown avg `0.9915` n `692`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
