# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T23:22:26.903622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0297` n `13`; crypto_alt avg `-0.1577` n `239`; crypto_major avg `-0.0948` n `8`; equity avg `-0.016` n `160`; fx avg `0.0123` n `6`; index avg `0.0025` n `27`; metal avg `0.053` n `20`; unknown avg `1.9523` n `1261`
- 1h: commodity avg `-0.1322` n `13`; crypto_alt avg `-0.2422` n `239`; crypto_major avg `0.1571` n `8`; equity avg `-0.0383` n `160`; fx avg `0.0356` n `6`; index avg `0.0013` n `27`; metal avg `0.0389` n `20`; unknown avg `1.8127` n `1253`
- 4h: commodity avg `-0.3415` n `13`; crypto_alt avg `-0.711` n `239`; crypto_major avg `0.27` n `8`; equity avg `0.5355` n `160`; fx avg `0.0308` n `6`; index avg `0.1` n `27`; metal avg `0.2962` n `20`; unknown avg `1.6636` n `1205`
- 24h: commodity avg `-0.4037` n `13`; crypto_alt avg `0.6921` n `239`; crypto_major avg `-1.07` n `8`; equity avg `4.5406` n `160`; fx avg `-0.0805` n `6`; index avg `0.5623` n `27`; metal avg `0.6091` n `20`; unknown avg `8.9776` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
