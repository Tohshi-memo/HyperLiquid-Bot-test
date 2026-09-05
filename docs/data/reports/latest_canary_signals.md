# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T17:22:25.656929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0203` n `12`; crypto_alt avg `-0.123` n `232`; crypto_major avg `0.004` n `8`; equity avg `0.0244` n `134`; fx avg `-0.0134` n `6`; index avg `0.0085` n `26`; metal avg `-0.0068` n `20`; unknown avg `0.2994` n `794`
- 1h: commodity avg `-0.0197` n `12`; crypto_alt avg `0.2597` n `232`; crypto_major avg `0.5687` n `8`; equity avg `0.0529` n `134`; fx avg `0.0071` n `6`; index avg `0.0227` n `26`; metal avg `0.0123` n `20`; unknown avg `0.1436` n `786`
- 4h: commodity avg `0.0498` n `12`; crypto_alt avg `0.1474` n `232`; crypto_major avg `0.6044` n `8`; equity avg `0.0986` n `134`; fx avg `-0.0128` n `6`; index avg `0.0186` n `26`; metal avg `0.0261` n `20`; unknown avg `-0.4246` n `730`
- 24h: commodity avg `0.093` n `12`; crypto_alt avg `2.5629` n `232`; crypto_major avg `2.4022` n `8`; equity avg `0.3712` n `134`; fx avg `-0.0025` n `6`; index avg `0.0379` n `26`; metal avg `0.0432` n `20`; unknown avg `0.2291` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
