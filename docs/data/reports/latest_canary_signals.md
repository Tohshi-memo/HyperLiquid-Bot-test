# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T08:07:24.251158+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `0.0252` n `232`; crypto_major avg `0.0402` n `8`; equity avg `0.0269` n `134`; fx avg `-0.0124` n `6`; index avg `-0.0063` n `26`; metal avg `0.0085` n `20`; unknown avg `-0.0362` n `792`
- 1h: commodity avg `-0.0093` n `12`; crypto_alt avg `-0.1311` n `232`; crypto_major avg `-0.1861` n `8`; equity avg `-0.041` n `134`; fx avg `0.0231` n `6`; index avg `-0.0101` n `26`; metal avg `-0.0175` n `20`; unknown avg `-0.0752` n `790`
- 4h: commodity avg `-0.013` n `12`; crypto_alt avg `-0.385` n `232`; crypto_major avg `-0.2048` n `8`; equity avg `0.0492` n `134`; fx avg `0.0392` n `6`; index avg `-0.004` n `26`; metal avg `-0.0147` n `20`; unknown avg `438.6445` n `760`
- 24h: commodity avg `0.1491` n `12`; crypto_alt avg `1.8858` n `232`; crypto_major avg `2.097` n `8`; equity avg `0.4467` n `134`; fx avg `-0.0212` n `6`; index avg `0.0856` n `26`; metal avg `-0.0054` n `20`; unknown avg `493.4905` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
