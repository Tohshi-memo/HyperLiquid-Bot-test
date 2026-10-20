# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T22:22:36.803323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `13`; crypto_alt avg `0.0121` n `237`; crypto_major avg `0.062` n `8`; equity avg `0.0817` n `151`; fx avg `-0.0044` n `6`; index avg `-0.0041` n `26`; metal avg `0.0216` n `20`; unknown avg `-0.0658` n `1199`
- 1h: commodity avg `-0.016` n `13`; crypto_alt avg `0.1269` n `237`; crypto_major avg `0.1846` n `8`; equity avg `0.5036` n `151`; fx avg `0.0094` n `6`; index avg `0.0538` n `26`; metal avg `0.0277` n `20`; unknown avg `-0.2892` n `1169`
- 4h: commodity avg `0.1714` n `13`; crypto_alt avg `0.6916` n `237`; crypto_major avg `0.8192` n `8`; equity avg `1.4504` n `151`; fx avg `0.0106` n `6`; index avg `0.1521` n `26`; metal avg `0.0282` n `20`; unknown avg `0.6283` n `1105`
- 24h: commodity avg `-0.0156` n `13`; crypto_alt avg `2.3616` n `237`; crypto_major avg `1.6998` n `8`; equity avg `1.4846` n `151`; fx avg `0.0426` n `6`; index avg `0.1494` n `26`; metal avg `0.0964` n `20`; unknown avg `197.2803` n `1058`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
