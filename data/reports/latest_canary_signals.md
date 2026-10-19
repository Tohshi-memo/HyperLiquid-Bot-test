# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T21:22:31.551051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0105` n `13`; crypto_alt avg `0.2605` n `237`; crypto_major avg `0.2016` n `8`; equity avg `0.0504` n `151`; fx avg `-0.0012` n `6`; index avg `0.0052` n `26`; metal avg `0.0069` n `20`; unknown avg `2.226` n `1196`
- 1h: commodity avg `-0.031` n `13`; crypto_alt avg `-0.0163` n `237`; crypto_major avg `0.1698` n `8`; equity avg `0.1097` n `151`; fx avg `0.0078` n `6`; index avg `0.0065` n `26`; metal avg `0.015` n `20`; unknown avg `2.1333` n `1180`
- 4h: commodity avg `-0.2841` n `13`; crypto_alt avg `0.0703` n `237`; crypto_major avg `0.2082` n `8`; equity avg `-0.1561` n `151`; fx avg `0.0053` n `6`; index avg `-0.0113` n `26`; metal avg `-0.0023` n `20`; unknown avg `2.1813` n `1122`
- 24h: commodity avg `-0.338` n `13`; crypto_alt avg `2.8719` n `237`; crypto_major avg `2.1794` n `8`; equity avg `2.8946` n `151`; fx avg `0.0282` n `6`; index avg `0.5717` n `26`; metal avg `0.103` n `20`; unknown avg `5.995` n `908`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1944`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
