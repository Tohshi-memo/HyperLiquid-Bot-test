# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T03:07:28.713574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.0319` n `232`; crypto_major avg `0.0592` n `8`; equity avg `0.0116` n `134`; fx avg `-0.0045` n `6`; index avg `-0.0134` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.2806` n `792`
- 1h: commodity avg `-0.0212` n `12`; crypto_alt avg `-0.3721` n `232`; crypto_major avg `0.0807` n `8`; equity avg `0.0495` n `134`; fx avg `-0.0046` n `6`; index avg `0.001` n `26`; metal avg `-0.0157` n `20`; unknown avg `1.5809` n `790`
- 4h: commodity avg `-0.0026` n `12`; crypto_alt avg `0.6443` n `232`; crypto_major avg `0.4973` n `8`; equity avg `0.1059` n `134`; fx avg `-0.0119` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0277` n `20`; unknown avg `0.1348` n `784`
- 24h: commodity avg `0.1168` n `12`; crypto_alt avg `3.0387` n `232`; crypto_major avg `2.7609` n `8`; equity avg `0.458` n `134`; fx avg `-0.0721` n `6`; index avg `0.0661` n `26`; metal avg `0.0251` n `20`; unknown avg `0.9021` n `692`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
