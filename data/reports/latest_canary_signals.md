# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T01:22:29.532386+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0549` n `12`; crypto_alt avg `-0.1626` n `234`; crypto_major avg `-0.0869` n `8`; equity avg `-0.0025` n `140`; fx avg `-0.0023` n `6`; index avg `0.0038` n `26`; metal avg `0.0112` n `20`; unknown avg `-0.023` n `943`
- 1h: commodity avg `0.0353` n `12`; crypto_alt avg `-0.0786` n `234`; crypto_major avg `-0.0991` n `8`; equity avg `0.0256` n `140`; fx avg `0.0159` n `6`; index avg `-0.0018` n `26`; metal avg `0.0052` n `20`; unknown avg `0.2311` n `941`
- 4h: commodity avg `0.1444` n `12`; crypto_alt avg `0.679` n `234`; crypto_major avg `-0.1162` n `8`; equity avg `0.0347` n `140`; fx avg `0.0104` n `6`; index avg `-0.0073` n `26`; metal avg `0.0041` n `20`; unknown avg `0.2297` n `911`
- 24h: commodity avg `0.0451` n `12`; crypto_alt avg `1.5035` n `234`; crypto_major avg `-0.2859` n `8`; equity avg `0.0979` n `140`; fx avg `-0.0483` n `6`; index avg `0.0021` n `26`; metal avg `0.0402` n `20`; unknown avg `0.3419` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
