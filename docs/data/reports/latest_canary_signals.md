# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T08:07:30.994099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `-0.0557` n `232`; crypto_major avg `0.0075` n `8`; equity avg `-0.0225` n `134`; fx avg `-0.0009` n `6`; index avg `0.0` n `26`; metal avg `-0.0092` n `20`; unknown avg `-0.0233` n `790`
- 1h: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.1037` n `232`; crypto_major avg `0.2267` n `8`; equity avg `-0.0459` n `134`; fx avg `0.0046` n `6`; index avg `-0.0237` n `26`; metal avg `0.0077` n `20`; unknown avg `0.2392` n `790`
- 4h: commodity avg `-0.0233` n `12`; crypto_alt avg `0.8503` n `232`; crypto_major avg `0.6931` n `8`; equity avg `0.0958` n `134`; fx avg `-0.0223` n `6`; index avg `0.0084` n `26`; metal avg `0.0211` n `20`; unknown avg `5.5812` n `744`
- 24h: commodity avg `0.1361` n `12`; crypto_alt avg `0.9999` n `232`; crypto_major avg `-0.9494` n `8`; equity avg `0.9424` n `134`; fx avg `-0.1371` n `6`; index avg `0.0614` n `26`; metal avg `-0.2528` n `20`; unknown avg `16.3842` n `648`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1712`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
