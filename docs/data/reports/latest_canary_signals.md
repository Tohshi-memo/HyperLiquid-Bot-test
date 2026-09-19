# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T13:07:28.236786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.1795` n `234`; crypto_major avg `-0.0206` n `8`; equity avg `-0.0162` n `140`; fx avg `-0.0019` n `6`; index avg `-0.003` n `26`; metal avg `-0.0041` n `20`; unknown avg `-0.3158` n `940`
- 1h: commodity avg `0.0232` n `12`; crypto_alt avg `-0.2592` n `234`; crypto_major avg `0.0248` n `8`; equity avg `-0.0014` n `140`; fx avg `-0.008` n `6`; index avg `0.0001` n `26`; metal avg `0.0031` n `20`; unknown avg `0.0659` n `940`
- 4h: commodity avg `0.0115` n `12`; crypto_alt avg `0.6437` n `234`; crypto_major avg `0.3016` n `8`; equity avg `0.0076` n `140`; fx avg `-0.0255` n `6`; index avg `-0.0013` n `26`; metal avg `0.0304` n `20`; unknown avg `0.386` n `934`
- 24h: commodity avg `-0.0307` n `12`; crypto_alt avg `4.0428` n `234`; crypto_major avg `4.1661` n `8`; equity avg `0.7796` n `140`; fx avg `-0.0098` n `6`; index avg `0.0621` n `26`; metal avg `-0.0462` n `20`; unknown avg `2.5185` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
