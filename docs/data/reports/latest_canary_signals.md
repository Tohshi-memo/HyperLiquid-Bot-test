# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T04:22:29.808023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `-0.1102` n `234`; crypto_major avg `-0.1001` n `8`; equity avg `-0.0088` n `141`; fx avg `-0.0024` n `6`; index avg `0.0003` n `26`; metal avg `-0.0` n `20`; unknown avg `-0.3659` n `961`
- 1h: commodity avg `-0.0147` n `12`; crypto_alt avg `0.4049` n `234`; crypto_major avg `-0.0848` n `8`; equity avg `-0.0032` n `141`; fx avg `-0.0109` n `6`; index avg `0.0004` n `26`; metal avg `-0.0031` n `20`; unknown avg `1.1374` n `953`
- 4h: commodity avg `0.2846` n `12`; crypto_alt avg `-0.5723` n `234`; crypto_major avg `-0.4898` n `8`; equity avg `-0.1595` n `141`; fx avg `-0.0043` n `6`; index avg `-0.0415` n `26`; metal avg `-0.0217` n `20`; unknown avg `-0.3413` n `952`
- 24h: commodity avg `0.0265` n `12`; crypto_alt avg `3.2493` n `234`; crypto_major avg `1.1526` n `8`; equity avg `-0.3244` n `141`; fx avg `-0.1149` n `6`; index avg `0.1486` n `26`; metal avg `0.2508` n `20`; unknown avg `1124.1917` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
