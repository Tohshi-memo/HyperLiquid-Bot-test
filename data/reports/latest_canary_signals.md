# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T19:22:31.333210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `12`; crypto_alt avg `-0.1024` n `232`; crypto_major avg `-0.1093` n `8`; equity avg `0.0126` n `134`; fx avg `-0.0026` n `6`; index avg `-0.0001` n `26`; metal avg `0.0052` n `20`; unknown avg `1.6322` n `793`
- 1h: commodity avg `-0.0087` n `12`; crypto_alt avg `-0.1524` n `232`; crypto_major avg `-0.2239` n `8`; equity avg `0.0628` n `134`; fx avg `-0.0012` n `6`; index avg `0.0033` n `26`; metal avg `0.0115` n `20`; unknown avg `1.7159` n `775`
- 4h: commodity avg `-0.003` n `12`; crypto_alt avg `0.3886` n `232`; crypto_major avg `-0.0525` n `8`; equity avg `0.2486` n `134`; fx avg `-0.0104` n `6`; index avg `0.0231` n `26`; metal avg `0.0117` n `20`; unknown avg `152.8986` n `754`
- 24h: commodity avg `0.0108` n `12`; crypto_alt avg `0.8673` n `232`; crypto_major avg `-0.2522` n `8`; equity avg `0.3687` n `134`; fx avg `-0.0145` n `6`; index avg `0.0118` n `26`; metal avg `-0.0218` n `20`; unknown avg `72.5255` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
