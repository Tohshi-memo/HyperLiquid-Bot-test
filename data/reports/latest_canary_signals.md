# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T16:22:30.556972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0232` n `12`; crypto_alt avg `0.1975` n `234`; crypto_major avg `0.1209` n `8`; equity avg `0.0218` n `140`; fx avg `-0.005` n `6`; index avg `0.0094` n `26`; metal avg `-0.0013` n `20`; unknown avg `-0.0565` n `943`
- 1h: commodity avg `-0.1133` n `12`; crypto_alt avg `0.1843` n `234`; crypto_major avg `0.0443` n `8`; equity avg `0.0151` n `140`; fx avg `-0.0035` n `6`; index avg `0.0064` n `26`; metal avg `-0.0138` n `20`; unknown avg `3.9528` n `925`
- 4h: commodity avg `-0.1592` n `12`; crypto_alt avg `0.0693` n `234`; crypto_major avg `0.3379` n `8`; equity avg `0.0468` n `140`; fx avg `-0.01` n `6`; index avg `0.0129` n `26`; metal avg `0.0036` n `20`; unknown avg `4.6291` n `922`
- 24h: commodity avg `-0.25` n `12`; crypto_alt avg `2.5432` n `234`; crypto_major avg `1.3638` n `8`; equity avg `0.7403` n `140`; fx avg `0.0097` n `6`; index avg `0.1722` n `26`; metal avg `-0.0168` n `20`; unknown avg `1.7405` n `806`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
