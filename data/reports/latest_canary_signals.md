# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T22:22:25.371376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0196` n `12`; crypto_alt avg `-0.045` n `229`; crypto_major avg `-0.0584` n `8`; equity avg `-0.0545` n `88`; fx avg `-0.0015` n `6`; index avg `-0.0079` n `25`; metal avg `-0.016` n `20`; unknown avg `-0.0471` n `765`
- 1h: commodity avg `0.0456` n `12`; crypto_alt avg `-0.0232` n `229`; crypto_major avg `-0.0786` n `8`; equity avg `0.0105` n `88`; fx avg `-0.0025` n `6`; index avg `-0.015` n `25`; metal avg `-0.0221` n `20`; unknown avg `-0.0399` n `765`
- 4h: commodity avg `-0.0253` n `12`; crypto_alt avg `0.6911` n `229`; crypto_major avg `0.694` n `8`; equity avg `-0.0373` n `88`; fx avg `-0.0154` n `6`; index avg `-0.0576` n `25`; metal avg `-0.0141` n `20`; unknown avg `-0.306` n `765`
- 24h: commodity avg `0.1418` n `12`; crypto_alt avg `3.4496` n `229`; crypto_major avg `3.5984` n `8`; equity avg `1.8078` n `88`; fx avg `-0.0691` n `6`; index avg `0.4441` n `25`; metal avg `0.527` n `20`; unknown avg `5.1934` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
