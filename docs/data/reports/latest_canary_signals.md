# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T00:07:24.389311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0358` n `12`; crypto_alt avg `-0.045` n `232`; crypto_major avg `-0.0243` n `8`; equity avg `0.016` n `134`; fx avg `0.0006` n `6`; index avg `0.0046` n `26`; metal avg `0.0001` n `20`; unknown avg `0.9569` n `792`
- 1h: commodity avg `-0.0429` n `12`; crypto_alt avg `-0.0083` n `232`; crypto_major avg `0.0238` n `8`; equity avg `0.0408` n `134`; fx avg `-0.0071` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0098` n `20`; unknown avg `-0.2365` n `792`
- 4h: commodity avg `-0.0274` n `12`; crypto_alt avg `0.2547` n `232`; crypto_major avg `-0.3502` n `8`; equity avg `0.0516` n `134`; fx avg `-0.008` n `6`; index avg `-0.0084` n `26`; metal avg `-0.005` n `20`; unknown avg `0.0822` n `770`
- 24h: commodity avg `0.1084` n `12`; crypto_alt avg `2.9147` n `232`; crypto_major avg `2.1919` n `8`; equity avg `0.3395` n `134`; fx avg `-0.0617` n `6`; index avg `0.0691` n `26`; metal avg `0.0527` n `20`; unknown avg `1.8998` n `698`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
