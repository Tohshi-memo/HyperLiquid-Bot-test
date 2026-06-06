# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T00:22:21.304098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0358` n `12`; crypto_alt avg `-0.0538` n `228`; crypto_major avg `-0.1085` n `8`; equity avg `0.1892` n `74`; fx avg `0.0` n `6`; index avg `0.0837` n `23`; metal avg `0.0149` n `18`; unknown avg `0.2475` n `425`
- 1h: commodity avg `-0.0715` n `12`; crypto_alt avg `0.5463` n `228`; crypto_major avg `0.4106` n `8`; equity avg `0.1627` n `74`; fx avg `-0.0012` n `6`; index avg `0.2117` n `23`; metal avg `-0.0924` n `18`; unknown avg `0.4345` n `425`
- 4h: commodity avg `0.3783` n `12`; crypto_alt avg `0.7168` n `228`; crypto_major avg `0.5229` n `8`; equity avg `0.307` n `74`; fx avg `0.0151` n `6`; index avg `0.4913` n `23`; metal avg `0.1374` n `18`; unknown avg `0.8781` n `425`
- 24h: commodity avg `-1.2887` n `12`; crypto_alt avg `-6.0315` n `228`; crypto_major avg `-5.2409` n `8`; equity avg `-5.1205` n `74`; fx avg `-0.1069` n `6`; index avg `-3.4402` n `23`; metal avg `-4.1223` n `18`; unknown avg `-1.1786` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
