# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T12:07:43.015802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.079` n `13`; crypto_alt avg `0.0223` n `239`; crypto_major avg `-0.1126` n `8`; equity avg `-0.2454` n `166`; fx avg `-0.0027` n `6`; index avg `-0.0251` n `27`; metal avg `-0.0136` n `20`; unknown avg `0.0159` n `1250`
- 1h: commodity avg `-0.0341` n `13`; crypto_alt avg `0.2266` n `239`; crypto_major avg `0.0729` n `8`; equity avg `-0.2883` n `166`; fx avg `-0.0146` n `6`; index avg `-0.0277` n `27`; metal avg `-0.0344` n `20`; unknown avg `0.2524` n `1256`
- 4h: commodity avg `-0.3611` n `13`; crypto_alt avg `0.0392` n `239`; crypto_major avg `0.1416` n `8`; equity avg `0.1151` n `166`; fx avg `-0.0779` n `6`; index avg `0.0214` n `27`; metal avg `0.1257` n `20`; unknown avg `448.8857` n `1112`
- 24h: commodity avg `-0.9839` n `13`; crypto_alt avg `0.7808` n `239`; crypto_major avg `1.0812` n `8`; equity avg `1.7853` n `166`; fx avg `0.1722` n `6`; index avg `0.117` n `27`; metal avg `0.3689` n `20`; unknown avg `-0.1735` n `1061`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
