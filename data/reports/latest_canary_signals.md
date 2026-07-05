# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T07:22:25.643494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `-0.0295` n `229`; crypto_major avg `0.0171` n `8`; equity avg `0.0087` n `88`; fx avg `0.0` n `6`; index avg `0.0001` n `25`; metal avg `-0.0018` n `20`; unknown avg `-0.0317` n `765`
- 1h: commodity avg `0.0048` n `12`; crypto_alt avg `0.176` n `229`; crypto_major avg `0.0522` n `8`; equity avg `-0.0113` n `88`; fx avg `0.0119` n `6`; index avg `-0.0115` n `25`; metal avg `-0.0073` n `20`; unknown avg `-0.0779` n `765`
- 4h: commodity avg `-0.009` n `12`; crypto_alt avg `-0.1012` n `229`; crypto_major avg `0.0951` n `8`; equity avg `0.0956` n `88`; fx avg `0.0089` n `6`; index avg `0.0258` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0374` n `731`
- 24h: commodity avg `0.0638` n `12`; crypto_alt avg `-0.7699` n `229`; crypto_major avg `-0.8176` n `8`; equity avg `0.1853` n `88`; fx avg `0.001` n `6`; index avg `0.0595` n `25`; metal avg `0.0708` n `20`; unknown avg `-1.2404` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
