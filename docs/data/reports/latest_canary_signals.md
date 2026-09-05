# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T16:52:30.968717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `0.0487` n `232`; crypto_major avg `0.1956` n `8`; equity avg `-0.0071` n `134`; fx avg `0.0194` n `6`; index avg `0.0083` n `26`; metal avg `0.0093` n `20`; unknown avg `-0.1363` n `794`
- 1h: commodity avg `-0.0119` n `12`; crypto_alt avg `0.2136` n `232`; crypto_major avg `0.3827` n `8`; equity avg `0.0193` n `134`; fx avg `0.002` n `6`; index avg `0.0175` n `26`; metal avg `0.0151` n `20`; unknown avg `-0.2737` n `786`
- 4h: commodity avg `0.035` n `12`; crypto_alt avg `-0.0784` n `232`; crypto_major avg `0.5586` n `8`; equity avg `0.051` n `134`; fx avg `0.0067` n `6`; index avg `0.015` n `26`; metal avg `0.0285` n `20`; unknown avg `-0.4109` n `730`
- 24h: commodity avg `0.0851` n `12`; crypto_alt avg `1.9597` n `232`; crypto_major avg `1.8284` n `8`; equity avg `0.1119` n `134`; fx avg `0.0016` n `6`; index avg `-0.0013` n `26`; metal avg `0.0263` n `20`; unknown avg `0.0518` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
