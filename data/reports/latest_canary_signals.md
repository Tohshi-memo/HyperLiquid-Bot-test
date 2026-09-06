# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T16:22:27.651567+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `12`; crypto_alt avg `0.2625` n `232`; crypto_major avg `0.0951` n `8`; equity avg `0.0173` n `134`; fx avg `0.0069` n `6`; index avg `0.0012` n `26`; metal avg `-0.0066` n `20`; unknown avg `0.6574` n `793`
- 1h: commodity avg `0.0146` n `12`; crypto_alt avg `0.5273` n `232`; crypto_major avg `-0.0376` n `8`; equity avg `0.0679` n `134`; fx avg `-0.0041` n `6`; index avg `0.0061` n `26`; metal avg `-0.0129` n `20`; unknown avg `0.4369` n `790`
- 4h: commodity avg `0.0217` n `12`; crypto_alt avg `-0.5132` n `232`; crypto_major avg `-0.8027` n `8`; equity avg `-0.2846` n `134`; fx avg `0.0015` n `6`; index avg `-0.0336` n `26`; metal avg `-0.02` n `20`; unknown avg `1.1113` n `720`
- 24h: commodity avg `0.0921` n `12`; crypto_alt avg `1.5529` n `232`; crypto_major avg `0.5953` n `8`; equity avg `0.2253` n `134`; fx avg `-0.0115` n `6`; index avg `0.0339` n `26`; metal avg `-0.0215` n `20`; unknown avg `1.7616` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
