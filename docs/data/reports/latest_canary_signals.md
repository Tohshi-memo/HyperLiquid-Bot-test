# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T21:37:30.751674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `0.0881` n `232`; crypto_major avg `0.0312` n `8`; equity avg `0.0029` n `134`; fx avg `-0.0024` n `6`; index avg `-0.0041` n `26`; metal avg `-0.03` n `20`; unknown avg `4.4084` n `793`
- 1h: commodity avg `0.0259` n `12`; crypto_alt avg `0.4219` n `232`; crypto_major avg `0.3496` n `8`; equity avg `0.0106` n `134`; fx avg `0.015` n `6`; index avg `0.0012` n `26`; metal avg `-0.0286` n `20`; unknown avg `147.8298` n `787`
- 4h: commodity avg `-0.0507` n `12`; crypto_alt avg `0.7483` n `232`; crypto_major avg `0.5621` n `8`; equity avg `0.147` n `134`; fx avg `0.0163` n `6`; index avg `0.0216` n `26`; metal avg `0.004` n `20`; unknown avg `0.4973` n `755`
- 24h: commodity avg `0.0031` n `12`; crypto_alt avg `1.3798` n `232`; crypto_major avg `0.4671` n `8`; equity avg `0.3538` n `134`; fx avg `0.0159` n `6`; index avg `0.0292` n `26`; metal avg `-0.0354` n `20`; unknown avg `105.8308` n `678`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
