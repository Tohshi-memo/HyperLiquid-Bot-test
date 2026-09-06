# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T11:22:27.179811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `0.0731` n `232`; crypto_major avg `0.025` n `8`; equity avg `0.0015` n `134`; fx avg `0.015` n `6`; index avg `0.0028` n `26`; metal avg `0.0014` n `20`; unknown avg `0.6261` n `794`
- 1h: commodity avg `-0.0128` n `12`; crypto_alt avg `0.3278` n `232`; crypto_major avg `0.0449` n `8`; equity avg `0.0503` n `134`; fx avg `0.0112` n `6`; index avg `-0.0046` n `26`; metal avg `-0.0074` n `20`; unknown avg `0.1566` n `792`
- 4h: commodity avg `0.0042` n `12`; crypto_alt avg `0.9331` n `232`; crypto_major avg `0.2856` n `8`; equity avg `0.1772` n `134`; fx avg `0.0401` n `6`; index avg `0.0196` n `26`; metal avg `-0.0044` n `20`; unknown avg `0.0251` n `786`
- 24h: commodity avg `0.1723` n `12`; crypto_alt avg `2.3701` n `232`; crypto_major avg `2.1064` n `8`; equity avg `0.5281` n `134`; fx avg `0.0037` n `6`; index avg `0.0836` n `26`; metal avg `0.0037` n `20`; unknown avg `492.5455` n `677`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
