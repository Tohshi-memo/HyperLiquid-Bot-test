# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T17:37:27.416512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `0.1003` n `232`; crypto_major avg `0.0277` n `8`; equity avg `0.024` n `134`; fx avg `0.0121` n `6`; index avg `0.0023` n `26`; metal avg `0.0031` n `20`; unknown avg `-0.1845` n `791`
- 1h: commodity avg `0.0061` n `12`; crypto_alt avg `-0.2022` n `232`; crypto_major avg `0.0142` n `8`; equity avg `0.0518` n `134`; fx avg `0.0029` n `6`; index avg `0.0041` n `26`; metal avg `0.0049` n `20`; unknown avg `146.617` n `783`
- 4h: commodity avg `0.0355` n `12`; crypto_alt avg `-0.1759` n `232`; crypto_major avg `-0.292` n `8`; equity avg `-0.0667` n `134`; fx avg `-0.0168` n `6`; index avg `-0.0154` n `26`; metal avg `-0.0215` n `20`; unknown avg `148.4504` n `776`
- 24h: commodity avg `0.1234` n `12`; crypto_alt avg `1.2381` n `232`; crypto_major avg `0.0893` n `8`; equity avg `0.2031` n `134`; fx avg `-0.0243` n `6`; index avg `0.0183` n `26`; metal avg `-0.0436` n `20`; unknown avg `2.3967` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
