# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T12:07:28.800007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `12`; crypto_alt avg `0.1261` n `234`; crypto_major avg `0.0763` n `8`; equity avg `0.0109` n `140`; fx avg `-0.005` n `6`; index avg `0.0118` n `26`; metal avg `-0.0021` n `20`; unknown avg `0.0562` n `934`
- 1h: commodity avg `-0.0142` n `12`; crypto_alt avg `0.3877` n `234`; crypto_major avg `0.2452` n `8`; equity avg `0.0168` n `140`; fx avg `-0.0153` n `6`; index avg `0.0129` n `26`; metal avg `0.0106` n `20`; unknown avg `0.2312` n `934`
- 4h: commodity avg `-0.0304` n `12`; crypto_alt avg `1.5705` n `234`; crypto_major avg `0.5181` n `8`; equity avg `0.0343` n `140`; fx avg `-0.0061` n `6`; index avg `0.0227` n `26`; metal avg `0.0193` n `20`; unknown avg `0.7943` n `934`
- 24h: commodity avg `0.1133` n `12`; crypto_alt avg `4.5703` n `234`; crypto_major avg `4.217` n `8`; equity avg `0.6876` n `140`; fx avg `-0.0134` n `6`; index avg `0.0373` n `26`; metal avg `-0.1252` n `20`; unknown avg `2.5737` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
