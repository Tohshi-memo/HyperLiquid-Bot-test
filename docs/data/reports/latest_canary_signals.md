# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T01:22:26.384143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0329` n `12`; crypto_alt avg `0.0123` n `232`; crypto_major avg `-0.0396` n `8`; equity avg `-0.002` n `134`; fx avg `0.0494` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.291` n `794`
- 1h: commodity avg `0.026` n `12`; crypto_alt avg `0.4968` n `232`; crypto_major avg `0.2098` n `8`; equity avg `0.0509` n `134`; fx avg `0.0393` n `6`; index avg `0.0041` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.5205` n `786`
- 4h: commodity avg `0.0301` n `12`; crypto_alt avg `0.8133` n `232`; crypto_major avg `-0.0795` n `8`; equity avg `0.1316` n `134`; fx avg `0.0195` n `6`; index avg `0.0089` n `26`; metal avg `-0.0113` n `20`; unknown avg `0.157` n `786`
- 24h: commodity avg `0.1279` n `12`; crypto_alt avg `3.3356` n `232`; crypto_major avg `2.5173` n `8`; equity avg `0.4362` n `134`; fx avg `-0.0455` n `6`; index avg `0.0782` n `26`; metal avg `0.0362` n `20`; unknown avg `0.4466` n `694`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
