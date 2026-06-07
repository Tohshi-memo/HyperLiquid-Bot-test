# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T18:37:23.010554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1033` n `12`; crypto_alt avg `-0.1564` n `228`; crypto_major avg `0.0063` n `8`; equity avg `0.027` n `74`; fx avg `0.0006` n `6`; index avg `0.0025` n `23`; metal avg `-0.0313` n `18`; unknown avg `-0.0026` n `516`
- 1h: commodity avg `0.1872` n `12`; crypto_alt avg `-0.4286` n `228`; crypto_major avg `-0.1221` n `8`; equity avg `-0.3145` n `74`; fx avg `-0.0091` n `6`; index avg `-0.1349` n `23`; metal avg `-0.0751` n `18`; unknown avg `0.1003` n `516`
- 4h: commodity avg `0.4289` n `12`; crypto_alt avg `-0.5624` n `228`; crypto_major avg `0.1965` n `8`; equity avg `-0.2135` n `74`; fx avg `-0.0027` n `6`; index avg `-0.2108` n `23`; metal avg `0.0212` n `18`; unknown avg `-2.3328` n `516`
- 24h: commodity avg `0.4151` n `12`; crypto_alt avg `2.8763` n `228`; crypto_major avg `3.8469` n `8`; equity avg `1.8511` n `74`; fx avg `-0.1921` n `6`; index avg `0.3293` n `23`; metal avg `0.5786` n `18`; unknown avg `-4.5281` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
