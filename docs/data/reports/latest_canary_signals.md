# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T12:37:25.428205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `12`; crypto_alt avg `-0.132` n `232`; crypto_major avg `0.0123` n `8`; equity avg `0.0015` n `134`; fx avg `0.0052` n `6`; index avg `0.0061` n `26`; metal avg `0.0064` n `20`; unknown avg `-0.3085` n `786`
- 1h: commodity avg `-0.0112` n `12`; crypto_alt avg `-0.1389` n `232`; crypto_major avg `0.2405` n `8`; equity avg `0.0673` n `134`; fx avg `-0.009` n `6`; index avg `0.0018` n `26`; metal avg `0.005` n `20`; unknown avg `61.371` n `784`
- 4h: commodity avg `-0.0148` n `12`; crypto_alt avg `0.8319` n `232`; crypto_major avg `0.6476` n `8`; equity avg `0.2375` n `134`; fx avg `0.0046` n `6`; index avg `0.0272` n `26`; metal avg `0.0119` n `20`; unknown avg `61.7021` n `784`
- 24h: commodity avg `0.1088` n `12`; crypto_alt avg `1.9819` n `232`; crypto_major avg `1.9587` n `8`; equity avg `0.5613` n `134`; fx avg `-0.0187` n `6`; index avg `0.0809` n `26`; metal avg `0.0222` n `20`; unknown avg `491.6993` n `678`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
