# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T13:24:49.808562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `-0.0941` n `234`; crypto_major avg `0.0304` n `8`; equity avg `0.0007` n `140`; fx avg `-0.0056` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0021` n `20`; unknown avg `-0.3518` n `942`
- 1h: commodity avg `0.0182` n `12`; crypto_alt avg `-0.2041` n `234`; crypto_major avg `0.1753` n `8`; equity avg `-0.0007` n `140`; fx avg `-0.0065` n `6`; index avg `-0.0017` n `26`; metal avg `-0.0009` n `20`; unknown avg `-0.2205` n `940`
- 4h: commodity avg `0.0162` n `12`; crypto_alt avg `0.6336` n `234`; crypto_major avg `0.2733` n `8`; equity avg `0.0207` n `140`; fx avg `-0.0329` n `6`; index avg `-0.002` n `26`; metal avg `0.0199` n `20`; unknown avg `0.3304` n `934`
- 24h: commodity avg `-0.075` n `12`; crypto_alt avg `3.7258` n `234`; crypto_major avg `3.8936` n `8`; equity avg `0.6565` n `140`; fx avg `-0.0212` n `6`; index avg `0.052` n `26`; metal avg `-0.0426` n `20`; unknown avg `2.1953` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1637`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
