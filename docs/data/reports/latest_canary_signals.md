# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T16:22:27.733022+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `0.1354` n `232`; crypto_major avg `0.0465` n `8`; equity avg `0.0087` n `134`; fx avg `0.0042` n `6`; index avg `0.0032` n `26`; metal avg `0.0003` n `20`; unknown avg `0.0328` n `794`
- 1h: commodity avg `0.0043` n `12`; crypto_alt avg `0.1744` n `232`; crypto_major avg `0.1572` n `8`; equity avg `0.0261` n `134`; fx avg `-0.0232` n `6`; index avg `-0.0034` n `26`; metal avg `0.0056` n `20`; unknown avg `-0.2443` n `792`
- 4h: commodity avg `0.0318` n `12`; crypto_alt avg `0.2332` n `232`; crypto_major avg `0.7728` n `8`; equity avg `0.0545` n `134`; fx avg `-0.0092` n `6`; index avg `0.0084` n `26`; metal avg `0.0089` n `20`; unknown avg `-0.3093` n `730`
- 24h: commodity avg `0.1471` n `12`; crypto_alt avg `2.3152` n `232`; crypto_major avg `1.8465` n `8`; equity avg `0.3126` n `134`; fx avg `-0.0225` n `6`; index avg `-0.0052` n `26`; metal avg `0.0082` n `20`; unknown avg `0.0716` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
