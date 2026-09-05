# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T18:22:54.485864+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.1279` n `232`; crypto_major avg `-0.0553` n `8`; equity avg `0.0099` n `134`; fx avg `0.0041` n `6`; index avg `0.0009` n `26`; metal avg `0.0027` n `20`; unknown avg `-0.0004` n `794`
- 1h: commodity avg `0.0288` n `12`; crypto_alt avg `0.1542` n `232`; crypto_major avg `0.5811` n `8`; equity avg `0.0202` n `134`; fx avg `-0.005` n `6`; index avg `-0.0007` n `26`; metal avg `0.0184` n `20`; unknown avg `-0.032` n `792`
- 4h: commodity avg `0.0384` n `12`; crypto_alt avg `0.6382` n `232`; crypto_major avg `1.4244` n `8`; equity avg `0.1359` n `134`; fx avg `-0.0228` n `6`; index avg `0.0434` n `26`; metal avg `0.041` n `20`; unknown avg `-0.5597` n `786`
- 24h: commodity avg `0.0274` n `12`; crypto_alt avg `2.8749` n `232`; crypto_major avg `3.1003` n `8`; equity avg `0.4551` n `134`; fx avg `-0.0176` n `6`; index avg `0.0652` n `26`; metal avg `0.1482` n `20`; unknown avg `0.0702` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
