# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T16:07:32.710224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `0.0115` n `229`; crypto_major avg `0.0285` n `8`; equity avg `0.073` n `88`; fx avg `-0.0084` n `6`; index avg `-0.0024` n `25`; metal avg `-0.0191` n `20`; unknown avg `-0.0677` n `765`
- 1h: commodity avg `0.0415` n `12`; crypto_alt avg `-0.3038` n `229`; crypto_major avg `-0.482` n `8`; equity avg `-0.0556` n `88`; fx avg `-0.0291` n `6`; index avg `-0.033` n `25`; metal avg `-0.1381` n `20`; unknown avg `0.8891` n `765`
- 4h: commodity avg `0.1321` n `12`; crypto_alt avg `0.1443` n `229`; crypto_major avg `0.1247` n `8`; equity avg `-0.1192` n `88`; fx avg `-0.033` n `6`; index avg `-0.0433` n `25`; metal avg `-0.1597` n `20`; unknown avg `1.8006` n `765`
- 24h: commodity avg `0.3464` n `12`; crypto_alt avg `2.3839` n `229`; crypto_major avg `1.9209` n `8`; equity avg `1.4912` n `88`; fx avg `-0.0614` n `6`; index avg `0.4293` n `25`; metal avg `0.4651` n `20`; unknown avg `8.13` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0491`, n `668`, weak_sample_signal
