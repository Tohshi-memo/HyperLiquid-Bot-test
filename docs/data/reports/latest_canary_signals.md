# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T02:07:27.612534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `0.002` n `232`; crypto_major avg `-0.0321` n `8`; equity avg `-0.0283` n `134`; fx avg `0.0117` n `6`; index avg `0.0092` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.8293` n `792`
- 1h: commodity avg `-0.0218` n `12`; crypto_alt avg `0.283` n `232`; crypto_major avg `0.0493` n `8`; equity avg `-0.0271` n `134`; fx avg `0.0205` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0007` n `20`; unknown avg `1.4612` n `792`
- 4h: commodity avg `0.0018` n `12`; crypto_alt avg `0.8153` n `232`; crypto_major avg `-0.0035` n `8`; equity avg `0.082` n `134`; fx avg `-0.0089` n `6`; index avg `0.007` n `26`; metal avg `-0.0127` n `20`; unknown avg `1.2631` n `786`
- 24h: commodity avg `0.1407` n `12`; crypto_alt avg `3.7987` n `232`; crypto_major avg `2.7255` n `8`; equity avg `0.4233` n `134`; fx avg `-0.0707` n `6`; index avg `0.0697` n `26`; metal avg `0.0398` n `20`; unknown avg `0.5906` n `694`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
