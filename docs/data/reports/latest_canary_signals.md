# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T17:37:26.642459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.0133` n `232`; crypto_major avg `0.0307` n `8`; equity avg `0.0134` n `134`; fx avg `-0.0005` n `6`; index avg `-0.0046` n `26`; metal avg `0.008` n `20`; unknown avg `-0.0867` n `794`
- 1h: commodity avg `-0.0048` n `12`; crypto_alt avg `0.3062` n `232`; crypto_major avg `0.5021` n `8`; equity avg `0.0577` n `134`; fx avg `0.0053` n `6`; index avg `0.0097` n `26`; metal avg `0.0147` n `20`; unknown avg `0.0611` n `792`
- 4h: commodity avg `-0.0067` n `12`; crypto_alt avg `0.3822` n `232`; crypto_major avg `0.7561` n `8`; equity avg `0.1037` n `134`; fx avg `-0.0133` n `6`; index avg `0.0271` n `26`; metal avg `0.0296` n `20`; unknown avg `-0.5768` n `740`
- 24h: commodity avg `0.0445` n `12`; crypto_alt avg `2.6692` n `232`; crypto_major avg `2.6095` n `8`; equity avg `0.4709` n `134`; fx avg `-0.0026` n `6`; index avg `0.0552` n `26`; metal avg `0.1258` n `20`; unknown avg `0.2218` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
