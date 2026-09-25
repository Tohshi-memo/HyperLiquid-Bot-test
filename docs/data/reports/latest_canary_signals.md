# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T12:37:29.028299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0871` n `12`; crypto_alt avg `0.5629` n `234`; crypto_major avg `0.589` n `8`; equity avg `-0.0045` n `141`; fx avg `0.0238` n `6`; index avg `-0.013` n `26`; metal avg `-0.0162` n `20`; unknown avg `3.2345` n `944`
- 1h: commodity avg `0.2066` n `12`; crypto_alt avg `-0.2155` n `234`; crypto_major avg `0.1069` n `8`; equity avg `-0.1162` n `141`; fx avg `0.0277` n `6`; index avg `-0.0334` n `26`; metal avg `0.0275` n `20`; unknown avg `5.1161` n `936`
- 4h: commodity avg `-0.0103` n `12`; crypto_alt avg `1.095` n `234`; crypto_major avg `1.4433` n `8`; equity avg `-0.0102` n `141`; fx avg `0.0012` n `6`; index avg `0.0071` n `26`; metal avg `0.1544` n `20`; unknown avg `5.4507` n `936`
- 24h: commodity avg `0.1463` n `12`; crypto_alt avg `5.671` n `234`; crypto_major avg `3.9016` n `8`; equity avg `2.041` n `141`; fx avg `-0.1748` n `6`; index avg `0.2985` n `26`; metal avg `0.2672` n `20`; unknown avg `14.6081` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
