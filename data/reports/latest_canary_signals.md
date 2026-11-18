# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T04:37:29.627724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `13`; crypto_alt avg `-0.1499` n `239`; crypto_major avg `-0.0144` n `8`; equity avg `-0.2441` n `163`; fx avg `-0.005` n `6`; index avg `-0.0346` n `27`; metal avg `-0.0499` n `20`; unknown avg `2.7751` n `1264`
- 1h: commodity avg `-0.0207` n `13`; crypto_alt avg `-0.378` n `239`; crypto_major avg `-0.1518` n `8`; equity avg `0.021` n `163`; fx avg `-0.019` n `6`; index avg `0.0173` n `27`; metal avg `-0.1243` n `20`; unknown avg `13.4058` n `1254`
- 4h: commodity avg `-0.2126` n `13`; crypto_alt avg `-0.7827` n `239`; crypto_major avg `-0.7293` n `8`; equity avg `-1.3533` n `163`; fx avg `-0.0203` n `6`; index avg `-0.1417` n `27`; metal avg `-0.4398` n `20`; unknown avg `6.1438` n `1254`
- 24h: commodity avg `0.208` n `13`; crypto_alt avg `-0.3691` n `239`; crypto_major avg `0.0616` n `8`; equity avg `-0.2048` n `163`; fx avg `-0.083` n `6`; index avg `-0.0279` n `27`; metal avg `-0.8303` n `20`; unknown avg `240.3798` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
