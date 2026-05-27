# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T17:37:24.234583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.108` n `12`; crypto_alt avg `-0.1142` n `228`; crypto_major avg `-0.1605` n `8`; equity avg `0.1105` n `67`; fx avg `-0.0078` n `6`; index avg `0.0378` n `23`; metal avg `0.0442` n `18`; unknown avg `-0.0661` n `418`
- 1h: commodity avg `-0.2375` n `12`; crypto_alt avg `-0.4851` n `228`; crypto_major avg `-0.3871` n `8`; equity avg `-0.0586` n `67`; fx avg `0.0112` n `6`; index avg `-0.0403` n `23`; metal avg `-0.0769` n `18`; unknown avg `-0.0061` n `418`
- 4h: commodity avg `0.1142` n `12`; crypto_alt avg `0.1854` n `228`; crypto_major avg `-0.3384` n `8`; equity avg `-0.1022` n `67`; fx avg `-0.0115` n `6`; index avg `-0.2815` n `23`; metal avg `0.3085` n `18`; unknown avg `-0.8671` n `418`
- 24h: commodity avg `-1.2508` n `12`; crypto_alt avg `-0.6186` n `228`; crypto_major avg `-0.7498` n `8`; equity avg `-0.4365` n `67`; fx avg `-0.0655` n `6`; index avg `-0.4729` n `23`; metal avg `-0.8155` n `18`; unknown avg `-0.9078` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
