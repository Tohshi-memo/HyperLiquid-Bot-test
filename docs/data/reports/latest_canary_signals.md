# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T17:07:25.867642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `12`; crypto_alt avg `-0.2314` n `232`; crypto_major avg `-0.1165` n `8`; equity avg `0.026` n `134`; fx avg `-0.0185` n `6`; index avg `0.005` n `26`; metal avg `-0.0052` n `20`; unknown avg `0.1245` n `791`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `0.1199` n `232`; crypto_major avg `0.0899` n `8`; equity avg `0.0405` n `134`; fx avg `-0.0078` n `6`; index avg `0.003` n `26`; metal avg `-0.0186` n `20`; unknown avg `0.1576` n `785`
- 4h: commodity avg `0.0455` n `12`; crypto_alt avg `-0.4705` n `232`; crypto_major avg `-0.7712` n `8`; equity avg `-0.1949` n `134`; fx avg `-0.0224` n `6`; index avg `-0.0228` n `26`; metal avg `-0.0319` n `20`; unknown avg `155.8625` n `736`
- 24h: commodity avg `0.1119` n `12`; crypto_alt avg `1.013` n `232`; crypto_major avg `0.0235` n `8`; equity avg `0.2194` n `134`; fx avg `-0.0466` n `6`; index avg `0.0214` n `26`; metal avg `-0.0526` n `20`; unknown avg `1.2115` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
