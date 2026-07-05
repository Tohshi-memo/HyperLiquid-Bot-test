# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T19:37:28.235626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `12`; crypto_alt avg `-0.0483` n `229`; crypto_major avg `0.0184` n `8`; equity avg `0.0013` n `88`; fx avg `0.0316` n `6`; index avg `0.0005` n `25`; metal avg `0.0136` n `20`; unknown avg `0.1103` n `765`
- 1h: commodity avg `-0.0209` n `12`; crypto_alt avg `0.1396` n `229`; crypto_major avg `0.1559` n `8`; equity avg `0.0263` n `88`; fx avg `0.0083` n `6`; index avg `0.0027` n `25`; metal avg `0.0144` n `20`; unknown avg `0.7744` n `765`
- 4h: commodity avg `-0.0033` n `12`; crypto_alt avg `0.3156` n `229`; crypto_major avg `0.1195` n `8`; equity avg `0.0891` n `88`; fx avg `0.0227` n `6`; index avg `0.0223` n `25`; metal avg `0.0119` n `20`; unknown avg `0.8237` n `713`
- 24h: commodity avg `0.0299` n `12`; crypto_alt avg `-1.1525` n `229`; crypto_major avg `-0.5763` n `8`; equity avg `0.3122` n `88`; fx avg `-0.0283` n `6`; index avg `0.102` n `25`; metal avg `0.033` n `20`; unknown avg `0.9798` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
