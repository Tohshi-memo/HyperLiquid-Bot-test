# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T22:52:16.130578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0732` n `12`; crypto_alt avg `-0.2386` n `228`; crypto_major avg `-0.2666` n `8`; equity avg `0.0207` n `67`; fx avg `0.0067` n `6`; index avg `-0.0048` n `23`; metal avg `-0.0597` n `18`; unknown avg `-0.3371` n `419`
- 1h: commodity avg `-0.0621` n `12`; crypto_alt avg `0.0994` n `228`; crypto_major avg `0.0155` n `8`; equity avg `-0.0862` n `67`; fx avg `-0.0125` n `6`; index avg `-0.0445` n `23`; metal avg `0.0892` n `18`; unknown avg `-0.039` n `419`
- 4h: commodity avg `0.1377` n `12`; crypto_alt avg `-1.7212` n `228`; crypto_major avg `-0.932` n `8`; equity avg `-0.1134` n `67`; fx avg `-0.0075` n `6`; index avg `0.0023` n `23`; metal avg `0.073` n `18`; unknown avg `-0.1854` n `419`
- 24h: commodity avg `-1.1818` n `12`; crypto_alt avg `-1.9293` n `228`; crypto_major avg `-1.0672` n `8`; equity avg `-0.2911` n `67`; fx avg `-0.1058` n `6`; index avg `-0.4455` n `23`; metal avg `-1.306` n `18`; unknown avg `-0.3963` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
