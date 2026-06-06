# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T23:37:22.424747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0372` n `12`; crypto_alt avg `0.1463` n `228`; crypto_major avg `0.1552` n `8`; equity avg `0.0867` n `74`; fx avg `-0.0027` n `6`; index avg `0.0126` n `23`; metal avg `0.032` n `18`; unknown avg `0.0369` n `515`
- 1h: commodity avg `0.0401` n `12`; crypto_alt avg `0.2875` n `228`; crypto_major avg `0.3779` n `8`; equity avg `0.2492` n `74`; fx avg `-0.0128` n `6`; index avg `0.0489` n `23`; metal avg `0.0145` n `18`; unknown avg `0.185` n `515`
- 4h: commodity avg `0.3395` n `12`; crypto_alt avg `0.5159` n `228`; crypto_major avg `0.383` n `8`; equity avg `0.3122` n `74`; fx avg `-0.0535` n `6`; index avg `0.1375` n `23`; metal avg `0.0072` n `18`; unknown avg `1.9815` n `515`
- 24h: commodity avg `0.4382` n `12`; crypto_alt avg `-0.5319` n `228`; crypto_major avg `-0.685` n `8`; equity avg `-0.1951` n `74`; fx avg `0.0113` n `6`; index avg `0.1481` n `23`; metal avg `-0.3915` n `18`; unknown avg `-0.0804` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
