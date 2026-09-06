# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T01:52:23.727641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0196` n `12`; crypto_alt avg `0.1454` n `232`; crypto_major avg `-0.0317` n `8`; equity avg `-0.0111` n `134`; fx avg `0.0` n `6`; index avg `-0.0091` n `26`; metal avg `0.0052` n `20`; unknown avg `1.5121` n `794`
- 1h: commodity avg `-0.027` n `12`; crypto_alt avg `0.454` n `232`; crypto_major avg `0.2035` n `8`; equity avg `0.0487` n `134`; fx avg `-0.0132` n `6`; index avg `-0.0128` n `26`; metal avg `-0.0035` n `20`; unknown avg `-0.0706` n `792`
- 4h: commodity avg `-0.0159` n `12`; crypto_alt avg `0.7985` n `232`; crypto_major avg `0.032` n `8`; equity avg `0.1189` n `134`; fx avg `-0.0223` n `6`; index avg `-0.0133` n `26`; metal avg `-0.0104` n `20`; unknown avg `0.1474` n `786`
- 24h: commodity avg `0.13` n `12`; crypto_alt avg `3.5999` n `232`; crypto_major avg `2.6391` n `8`; equity avg `0.44` n `134`; fx avg `-0.0826` n `6`; index avg `0.0562` n `26`; metal avg `0.0382` n `20`; unknown avg `0.4335` n `694`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
