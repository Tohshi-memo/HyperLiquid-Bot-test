# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T16:37:24.488268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.0594` n `232`; crypto_major avg `0.0981` n `8`; equity avg `0.0087` n `134`; fx avg `0.0012` n `6`; index avg `0.0084` n `26`; metal avg `0.0056` n `20`; unknown avg `-0.0793` n `788`
- 1h: commodity avg `-0.0063` n `12`; crypto_alt avg `0.1714` n `232`; crypto_major avg `0.2076` n `8`; equity avg `0.026` n `134`; fx avg `-0.0229` n `6`; index avg `0.0151` n `26`; metal avg `0.0049` n `20`; unknown avg `-0.1881` n `786`
- 4h: commodity avg `0.0347` n `12`; crypto_alt avg `-0.0198` n `232`; crypto_major avg `0.6301` n `8`; equity avg `0.0553` n `134`; fx avg `-0.0097` n `6`; index avg `0.0156` n `26`; metal avg `0.023` n `20`; unknown avg `-0.4051` n `730`
- 24h: commodity avg `0.1419` n `12`; crypto_alt avg `2.0511` n `232`; crypto_major avg `1.7191` n `8`; equity avg `0.2783` n `134`; fx avg `-0.0161` n `6`; index avg `0.0024` n `26`; metal avg `0.0203` n `20`; unknown avg `0.1197` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
