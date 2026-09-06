# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T13:52:24.540394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `12`; crypto_alt avg `0.156` n `232`; crypto_major avg `0.1888` n `8`; equity avg `0.0117` n `134`; fx avg `0.0038` n `6`; index avg `0.003` n `26`; metal avg `-0.0006` n `20`; unknown avg `1.1077` n `792`
- 1h: commodity avg `0.0066` n `12`; crypto_alt avg `-0.0646` n `232`; crypto_major avg `-0.188` n `8`; equity avg `-0.1604` n `134`; fx avg `0.0129` n `6`; index avg `-0.0079` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.4369` n `726`
- 4h: commodity avg `-0.0143` n `12`; crypto_alt avg `0.2707` n `232`; crypto_major avg `0.04` n `8`; equity avg `0.0027` n `134`; fx avg `0.0244` n `6`; index avg `-0.0034` n `26`; metal avg `-0.0119` n `20`; unknown avg `67.3324` n `720`
- 24h: commodity avg `0.0691` n `12`; crypto_alt avg `2.1137` n `232`; crypto_major avg `1.6497` n `8`; equity avg `0.4373` n `134`; fx avg `-0.0175` n `6`; index avg `0.066` n `26`; metal avg `0.0117` n `20`; unknown avg `0.0861` n `664`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
