# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T08:52:23.829625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0175` n `12`; crypto_alt avg `0.0804` n `232`; crypto_major avg `0.2527` n `8`; equity avg `0.0052` n `128`; fx avg `-0.0135` n `6`; index avg `0.0001` n `26`; metal avg `-0.0214` n `20`; unknown avg `0.4665` n `793`
- 1h: commodity avg `0.2106` n `12`; crypto_alt avg `-0.1473` n `232`; crypto_major avg `0.1403` n `8`; equity avg `-0.0486` n `128`; fx avg `-0.0442` n `6`; index avg `0.0018` n `26`; metal avg `-0.0368` n `20`; unknown avg `0.3993` n `791`
- 4h: commodity avg `0.1318` n `12`; crypto_alt avg `0.8571` n `232`; crypto_major avg `1.1549` n `8`; equity avg `0.7747` n `128`; fx avg `-0.0969` n `6`; index avg `0.1311` n `26`; metal avg `0.1189` n `20`; unknown avg `0.8481` n `773`
- 24h: commodity avg `0.5079` n `12`; crypto_alt avg `0.1675` n `231`; crypto_major avg `-0.9848` n `8`; equity avg `-0.2385` n `128`; fx avg `-0.1464` n `6`; index avg `-0.0309` n `26`; metal avg `-0.2519` n `20`; unknown avg `-0.2126` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
