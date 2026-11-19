# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T12:52:28.906538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.014` n `13`; crypto_alt avg `0.4815` n `239`; crypto_major avg `0.4105` n `8`; equity avg `0.1023` n `164`; fx avg `0.0119` n `6`; index avg `0.016` n `27`; metal avg `0.027` n `20`; unknown avg `7.6966` n `1266`
- 1h: commodity avg `0.1766` n `13`; crypto_alt avg `-0.1764` n `239`; crypto_major avg `-0.0504` n `8`; equity avg `-0.2396` n `164`; fx avg `0.0024` n `6`; index avg `-0.0385` n `27`; metal avg `-0.0425` n `20`; unknown avg `8.5507` n `1258`
- 4h: commodity avg `0.1213` n `13`; crypto_alt avg `0.0391` n `239`; crypto_major avg `0.3282` n `8`; equity avg `0.5056` n `164`; fx avg `0.0145` n `6`; index avg `0.0935` n `27`; metal avg `-0.1443` n `20`; unknown avg `210.5256` n `1254`
- 24h: commodity avg `0.1369` n `13`; crypto_alt avg `0.5168` n `239`; crypto_major avg `0.3731` n `8`; equity avg `1.3199` n `164`; fx avg `0.0398` n `6`; index avg `0.3442` n `27`; metal avg `-0.1066` n `20`; unknown avg `3.2732` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
