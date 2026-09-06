# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T10:52:29.538529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `0.1801` n `232`; crypto_major avg `0.1013` n `8`; equity avg `0.0351` n `134`; fx avg `-0.0195` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0004` n `20`; unknown avg `2.3264` n `794`
- 1h: commodity avg `0.0007` n `12`; crypto_alt avg `0.3097` n `232`; crypto_major avg `0.0473` n `8`; equity avg `0.1117` n `134`; fx avg `0.0195` n `6`; index avg `0.0046` n `26`; metal avg `-0.0125` n `20`; unknown avg `2.2943` n `792`
- 4h: commodity avg `0.0046` n `12`; crypto_alt avg `0.3808` n `232`; crypto_major avg `0.103` n `8`; equity avg `0.1253` n `134`; fx avg `0.0218` n `6`; index avg `0.0068` n `26`; metal avg `-0.0121` n `20`; unknown avg `-0.1059` n `784`
- 24h: commodity avg `0.1659` n `12`; crypto_alt avg `2.175` n `232`; crypto_major avg `2.0925` n `8`; equity avg `0.5409` n `134`; fx avg `-0.0092` n `6`; index avg `0.0784` n `26`; metal avg `0.0041` n `20`; unknown avg `493.2575` n `676`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
