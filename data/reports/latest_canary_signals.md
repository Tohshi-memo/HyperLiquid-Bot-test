# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T03:23:11.078857+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.2526` n `234`; crypto_major avg `-0.2068` n `8`; equity avg `-0.0232` n `140`; fx avg `-0.003` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0065` n `20`; unknown avg `0.8419` n `942`
- 1h: commodity avg `-0.0048` n `12`; crypto_alt avg `0.1142` n `234`; crypto_major avg `-0.1239` n `8`; equity avg `-0.0363` n `140`; fx avg `0.003` n `6`; index avg `-0.0171` n `26`; metal avg `0.0092` n `20`; unknown avg `4.1656` n `940`
- 4h: commodity avg `0.1553` n `12`; crypto_alt avg `0.5662` n `234`; crypto_major avg `0.3537` n `8`; equity avg `-0.1012` n `140`; fx avg `-0.0246` n `6`; index avg `-0.0256` n `26`; metal avg `-0.0316` n `20`; unknown avg `0.5229` n `934`
- 24h: commodity avg `0.1232` n `12`; crypto_alt avg `4.7024` n `234`; crypto_major avg `5.2303` n `8`; equity avg `0.8789` n `140`; fx avg `0.051` n `6`; index avg `0.0186` n `26`; metal avg `0.2424` n `20`; unknown avg `4.1337` n `787`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
