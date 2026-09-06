# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T00:52:25.280247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0282` n `12`; crypto_alt avg `0.1842` n `232`; crypto_major avg `0.0385` n `8`; equity avg `0.0016` n `134`; fx avg `0.0031` n `6`; index avg `0.0029` n `26`; metal avg `0.0001` n `20`; unknown avg `0.2319` n `794`
- 1h: commodity avg `0.0367` n `12`; crypto_alt avg `0.5319` n `232`; crypto_major avg `0.1964` n `8`; equity avg `0.0111` n `134`; fx avg `0.0019` n `6`; index avg `0.0009` n `26`; metal avg `0.0033` n `20`; unknown avg `0.6861` n `786`
- 4h: commodity avg `0.042` n `12`; crypto_alt avg `0.8279` n `232`; crypto_major avg `-0.0016` n `8`; equity avg `0.1134` n `134`; fx avg `-0.0035` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0055` n `20`; unknown avg `33.5908` n `782`
- 24h: commodity avg `0.1749` n `12`; crypto_alt avg `3.2501` n `232`; crypto_major avg `2.3472` n `8`; equity avg `0.3674` n `134`; fx avg `-0.0699` n `6`; index avg `0.0667` n `26`; metal avg `0.0587` n `20`; unknown avg `0.3125` n `694`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
