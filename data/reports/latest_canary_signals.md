# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T22:07:22.521102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `-0.2825` n `228`; crypto_major avg `-0.4537` n `8`; equity avg `-0.092` n `74`; fx avg `-0.0026` n `6`; index avg `-0.0374` n `23`; metal avg `-0.011` n `18`; unknown avg `-0.0841` n `515`
- 1h: commodity avg `0.0074` n `12`; crypto_alt avg `0.0108` n `228`; crypto_major avg `-0.2507` n `8`; equity avg `-0.0551` n `74`; fx avg `-0.0171` n `6`; index avg `-0.0375` n `23`; metal avg `-0.0068` n `18`; unknown avg `0.2279` n `515`
- 4h: commodity avg `0.0754` n `12`; crypto_alt avg `0.514` n `228`; crypto_major avg `0.0718` n `8`; equity avg `0.2741` n `74`; fx avg `-0.1245` n `6`; index avg `0.0773` n `23`; metal avg `-0.0048` n `18`; unknown avg `-0.0655` n `515`
- 24h: commodity avg `0.8781` n `12`; crypto_alt avg `-2.1071` n `228`; crypto_major avg `-1.9758` n `8`; equity avg `-1.2037` n `74`; fx avg `0.0223` n `6`; index avg `-0.0887` n `23`; metal avg `-0.6018` n `18`; unknown avg `-0.6296` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
