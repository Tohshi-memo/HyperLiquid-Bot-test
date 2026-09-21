# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T16:22:34.301198+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0517` n `12`; crypto_alt avg `0.3678` n `234`; crypto_major avg `0.0804` n `8`; equity avg `0.0589` n `140`; fx avg `-0.0176` n `6`; index avg `0.0214` n `26`; metal avg `0.0182` n `20`; unknown avg `-0.1826` n `942`
- 1h: commodity avg `-0.1394` n `12`; crypto_alt avg `0.6159` n `234`; crypto_major avg `0.23` n `8`; equity avg `0.1556` n `140`; fx avg `-0.0196` n `6`; index avg `0.0585` n `26`; metal avg `0.0428` n `20`; unknown avg `-0.4132` n `928`
- 4h: commodity avg `-0.3181` n `12`; crypto_alt avg `0.3615` n `234`; crypto_major avg `0.7272` n `8`; equity avg `0.8591` n `140`; fx avg `-0.0269` n `6`; index avg `0.222` n `26`; metal avg `-0.0729` n `20`; unknown avg `10.3102` n `870`
- 24h: commodity avg `-1.0919` n `12`; crypto_alt avg `5.8689` n `234`; crypto_major avg `5.6341` n `8`; equity avg `2.6864` n `140`; fx avg `-0.0998` n `6`; index avg `0.5776` n `26`; metal avg `0.0763` n `20`; unknown avg `4.2686` n `731`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
