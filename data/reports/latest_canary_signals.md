# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T12:37:39.434345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0432` n `13`; crypto_alt avg `0.0197` n `239`; crypto_major avg `-0.0169` n `8`; equity avg `-0.301` n `162`; fx avg `0.0096` n `6`; index avg `-0.0193` n `27`; metal avg `-0.0441` n `20`; unknown avg `136.594` n `1262`
- 1h: commodity avg `0.1425` n `13`; crypto_alt avg `0.3803` n `239`; crypto_major avg `0.2829` n `8`; equity avg `-0.1323` n `162`; fx avg `0.0042` n `6`; index avg `-0.0055` n `27`; metal avg `0.0443` n `20`; unknown avg `39.9751` n `1254`
- 4h: commodity avg `0.0663` n `13`; crypto_alt avg `0.6047` n `239`; crypto_major avg `1.0248` n `8`; equity avg `0.5257` n `162`; fx avg `-0.0291` n `6`; index avg `0.0596` n `27`; metal avg `0.0774` n `20`; unknown avg `43.3566` n `1200`
- 24h: commodity avg `0.8737` n `13`; crypto_alt avg `0.4177` n `239`; crypto_major avg `-1.3227` n `8`; equity avg `-0.266` n `162`; fx avg `0.0074` n `6`; index avg `0.0629` n `27`; metal avg `-0.2743` n `20`; unknown avg `2.4882` n `1073`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
