# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T19:07:25.226357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0168` n `12`; crypto_alt avg `0.0647` n `232`; crypto_major avg `-0.0138` n `8`; equity avg `-0.0156` n `134`; fx avg `-0.002` n `6`; index avg `0.0233` n `26`; metal avg `-0.0037` n `20`; unknown avg `-0.0591` n `792`
- 1h: commodity avg `0.0086` n `12`; crypto_alt avg `0.1054` n `232`; crypto_major avg `-0.2495` n `8`; equity avg `-0.0156` n `134`; fx avg `-0.0012` n `6`; index avg `0.0293` n `26`; metal avg `-0.0036` n `20`; unknown avg `-0.0141` n `792`
- 4h: commodity avg `0.0565` n `12`; crypto_alt avg `0.4133` n `232`; crypto_major avg `1.051` n `8`; equity avg `0.0752` n `134`; fx avg `-0.0342` n `6`; index avg `0.0471` n `26`; metal avg `0.0358` n `20`; unknown avg `-0.4538` n `786`
- 24h: commodity avg `0.0359` n `12`; crypto_alt avg `2.7052` n `232`; crypto_major avg `2.6593` n `8`; equity avg `0.4957` n `134`; fx avg `-0.0405` n `6`; index avg `0.0775` n `26`; metal avg `0.1374` n `20`; unknown avg `0.1479` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
