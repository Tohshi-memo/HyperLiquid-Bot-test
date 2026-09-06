# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T09:37:26.542641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.0848` n `232`; crypto_major avg `0.105` n `8`; equity avg `0.0278` n `134`; fx avg `0.0045` n `6`; index avg `0.0003` n `26`; metal avg `-0.0098` n `20`; unknown avg `1.1998` n `794`
- 1h: commodity avg `0.0069` n `12`; crypto_alt avg `0.3566` n `232`; crypto_major avg `0.49` n `8`; equity avg `0.0842` n `134`; fx avg `-0.0083` n `6`; index avg `0.0106` n `26`; metal avg `0.0228` n `20`; unknown avg `323.1362` n `792`
- 4h: commodity avg `0.0143` n `12`; crypto_alt avg `-0.358` n `232`; crypto_major avg `-0.2246` n `8`; equity avg `0.0907` n `134`; fx avg `-0.0202` n `6`; index avg `0.0065` n `26`; metal avg `0.0084` n `20`; unknown avg `-0.2631` n `766`
- 24h: commodity avg `0.1458` n `12`; crypto_alt avg `1.7625` n `232`; crypto_major avg `2.1433` n `8`; equity avg `0.4638` n `134`; fx avg `-0.0332` n `6`; index avg `0.0888` n `26`; metal avg `0.0215` n `20`; unknown avg `493.2202` n `676`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
