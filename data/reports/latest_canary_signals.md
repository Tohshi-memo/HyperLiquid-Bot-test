# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T00:07:32.151231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `12`; crypto_alt avg `0.1398` n `228`; crypto_major avg `0.1154` n `8`; equity avg `-0.2334` n `86`; fx avg `0.0343` n `6`; index avg `-0.0931` n `23`; metal avg `-0.0179` n `20`; unknown avg `0.0241` n `764`
- 1h: commodity avg `0.0394` n `12`; crypto_alt avg `0.292` n `228`; crypto_major avg `0.3659` n `8`; equity avg `0.1056` n `86`; fx avg `0.07` n `6`; index avg `-0.144` n `23`; metal avg `0.1309` n `20`; unknown avg `-0.4303` n `764`
- 4h: commodity avg `0.0433` n `12`; crypto_alt avg `0.7609` n `228`; crypto_major avg `1.1402` n `8`; equity avg `1.5229` n `86`; fx avg `0.0334` n `6`; index avg `0.2411` n `23`; metal avg `0.0495` n `20`; unknown avg `-0.4503` n `748`
- 24h: commodity avg `-0.4163` n `12`; crypto_alt avg `-2.1691` n `228`; crypto_major avg `-1.8091` n `8`; equity avg `4.8405` n `86`; fx avg `0.065` n `6`; index avg `0.4627` n `23`; metal avg `-1.5977` n `20`; unknown avg `-1.4221` n `716`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
