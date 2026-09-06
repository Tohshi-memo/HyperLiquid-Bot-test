# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T03:22:29.773044+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `0.0599` n `232`; crypto_major avg `0.0555` n `8`; equity avg `0.0139` n `134`; fx avg `-0.0016` n `6`; index avg `0.0122` n `26`; metal avg `0.001` n `20`; unknown avg `8.0133` n `794`
- 1h: commodity avg `-0.0175` n `12`; crypto_alt avg `0.0144` n `232`; crypto_major avg `0.2556` n `8`; equity avg `0.0435` n `134`; fx avg `-0.0136` n `6`; index avg `0.0028` n `26`; metal avg `-0.0049` n `20`; unknown avg `9.719` n `792`
- 4h: commodity avg `0.0207` n `12`; crypto_alt avg `0.7304` n `232`; crypto_major avg `0.5913` n `8`; equity avg `0.1113` n `134`; fx avg `-0.0132` n `6`; index avg `0.0094` n `26`; metal avg `-0.0261` n `20`; unknown avg `1.2212` n `784`
- 24h: commodity avg `0.1138` n `12`; crypto_alt avg `3.041` n `232`; crypto_major avg `2.8086` n `8`; equity avg `0.4929` n `134`; fx avg `-0.0737` n `6`; index avg `0.069` n `26`; metal avg `0.0198` n `20`; unknown avg `0.9065` n `692`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
