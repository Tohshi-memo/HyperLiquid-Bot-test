# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T01:52:25.024238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0404` n `12`; crypto_alt avg `-0.2662` n `230`; crypto_major avg `-0.2753` n `8`; equity avg `-0.1405` n `102`; fx avg `0.0074` n `6`; index avg `-0.0391` n `25`; metal avg `0.016` n `20`; unknown avg `0.6317` n `779`
- 1h: commodity avg `-0.0855` n `12`; crypto_alt avg `-0.0761` n `230`; crypto_major avg `-0.0223` n `8`; equity avg `-0.3201` n `102`; fx avg `0.0264` n `6`; index avg `-0.0966` n `25`; metal avg `-0.1189` n `20`; unknown avg `2.0061` n `779`
- 4h: commodity avg `-0.2384` n `12`; crypto_alt avg `0.1336` n `230`; crypto_major avg `-0.0835` n `8`; equity avg `0.9472` n `102`; fx avg `0.2287` n `6`; index avg `0.296` n `25`; metal avg `-0.2239` n `20`; unknown avg `0.1499` n `779`
- 24h: commodity avg `-0.1609` n `12`; crypto_alt avg `0.1154` n `230`; crypto_major avg `0.7825` n `8`; equity avg `6.5836` n `102`; fx avg `-0.2127` n `6`; index avg `0.7675` n `25`; metal avg `0.2248` n `20`; unknown avg `0.0736` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
