# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T16:07:30.746645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.2649` n `232`; crypto_major avg `-0.3115` n `8`; equity avg `-0.0953` n `131`; fx avg `-0.005` n `6`; index avg `-0.0276` n `26`; metal avg `0.0075` n `20`; unknown avg `-0.243` n `791`
- 1h: commodity avg `0.047` n `12`; crypto_alt avg `0.1757` n `232`; crypto_major avg `0.1972` n `8`; equity avg `0.2757` n `131`; fx avg `-0.0209` n `6`; index avg `0.0528` n `26`; metal avg `0.1336` n `20`; unknown avg `0.1837` n `790`
- 4h: commodity avg `0.0774` n `12`; crypto_alt avg `-0.1432` n `232`; crypto_major avg `-0.4538` n `8`; equity avg `0.0441` n `130`; fx avg `-0.0449` n `6`; index avg `0.0898` n `26`; metal avg `0.1019` n `20`; unknown avg `0.2706` n `790`
- 24h: commodity avg `0.3743` n `12`; crypto_alt avg `1.1364` n `232`; crypto_major avg `-0.3856` n `8`; equity avg `-0.6394` n `130`; fx avg `0.0215` n `6`; index avg `-0.0685` n `26`; metal avg `-0.417` n `20`; unknown avg `-0.0827` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0388`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0326`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0322`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0316`, n `668`, weak_sample_signal
