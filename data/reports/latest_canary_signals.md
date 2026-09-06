# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T02:52:24.825206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0161` n `12`; crypto_alt avg `-0.0923` n `232`; crypto_major avg `0.0293` n `8`; equity avg `0.0116` n `134`; fx avg `-0.0002` n `6`; index avg `0.0188` n `26`; metal avg `-0.0053` n `20`; unknown avg `42.7259` n `794`
- 1h: commodity avg `-0.0016` n `12`; crypto_alt avg `-0.338` n `232`; crypto_major avg `-0.0106` n `8`; equity avg `0.0096` n `134`; fx avg `0.0116` n `6`; index avg `0.0236` n `26`; metal avg `-0.0172` n `20`; unknown avg `43.1473` n `790`
- 4h: commodity avg `-0.0118` n `12`; crypto_alt avg `0.6136` n `232`; crypto_major avg `0.2968` n `8`; equity avg `0.0947` n `134`; fx avg `-0.0081` n `6`; index avg `0.0129` n `26`; metal avg `-0.0295` n `20`; unknown avg `41.8818` n `784`
- 24h: commodity avg `0.1146` n `12`; crypto_alt avg `2.9778` n `232`; crypto_major avg `2.7355` n `8`; equity avg `0.4374` n `134`; fx avg `-0.0581` n `6`; index avg `0.1121` n `26`; metal avg `0.027` n `20`; unknown avg `0.7165` n `692`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
