# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T15:22:26.586553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0272` n `12`; crypto_alt avg `-0.1633` n `232`; crypto_major avg `-0.0603` n `8`; equity avg `0.0014` n `134`; fx avg `-0.0077` n `6`; index avg `-0.0` n `26`; metal avg `0.0058` n `20`; unknown avg `-0.1806` n `794`
- 1h: commodity avg `0.0251` n `12`; crypto_alt avg `0.0337` n `232`; crypto_major avg `0.1088` n `8`; equity avg `0.0365` n `134`; fx avg `-0.0016` n `6`; index avg `0.0248` n `26`; metal avg `0.0047` n `20`; unknown avg `-0.2394` n `792`
- 4h: commodity avg `0.0863` n `12`; crypto_alt avg `0.2188` n `232`; crypto_major avg `0.7472` n `8`; equity avg `0.0414` n `134`; fx avg `0.015` n `6`; index avg `0.0139` n `26`; metal avg `0.0009` n `20`; unknown avg `-0.3325` n `729`
- 24h: commodity avg `0.1159` n `12`; crypto_alt avg `2.7356` n `232`; crypto_major avg `1.9492` n `8`; equity avg `0.5863` n `134`; fx avg `-0.0116` n `6`; index avg `0.0575` n `26`; metal avg `-0.035` n `20`; unknown avg `0.2803` n `656`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
