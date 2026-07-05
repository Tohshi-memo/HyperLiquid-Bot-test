# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T14:37:24.675876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `12`; crypto_alt avg `-0.0579` n `229`; crypto_major avg `-0.0052` n `8`; equity avg `0.034` n `88`; fx avg `-0.0069` n `6`; index avg `0.0314` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.019` n `765`
- 1h: commodity avg `0.001` n `12`; crypto_alt avg `-0.0179` n `229`; crypto_major avg `0.227` n `8`; equity avg `-0.0592` n `88`; fx avg `-0.0359` n `6`; index avg `0.0303` n `25`; metal avg `-0.0127` n `20`; unknown avg `0.031` n `765`
- 4h: commodity avg `-0.0095` n `12`; crypto_alt avg `0.3356` n `229`; crypto_major avg `0.7553` n `8`; equity avg `0.049` n `88`; fx avg `-0.0721` n `6`; index avg `0.051` n `25`; metal avg `0.0115` n `20`; unknown avg `0.1622` n `765`
- 24h: commodity avg `0.0039` n `12`; crypto_alt avg `-1.0882` n `229`; crypto_major avg `-0.5157` n `8`; equity avg `0.2665` n `88`; fx avg `-0.0658` n `6`; index avg `0.0867` n `25`; metal avg `0.0819` n `20`; unknown avg `-1.191` n `731`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
