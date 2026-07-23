# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T07:07:30.019366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0411` n `12`; crypto_alt avg `-0.0017` n `230`; crypto_major avg `-0.1227` n `8`; equity avg `-0.1983` n `98`; fx avg `0.0036` n `6`; index avg `-0.0319` n `25`; metal avg `-0.145` n `20`; unknown avg `-0.0216` n `773`
- 1h: commodity avg `0.137` n `12`; crypto_alt avg `0.128` n `230`; crypto_major avg `0.0155` n `8`; equity avg `-0.092` n `98`; fx avg `-0.0006` n `6`; index avg `-0.0199` n `25`; metal avg `-0.1488` n `20`; unknown avg `0.0249` n `773`
- 4h: commodity avg `0.1624` n `12`; crypto_alt avg `0.1812` n `230`; crypto_major avg `-0.0711` n `8`; equity avg `0.1052` n `98`; fx avg `0.0176` n `6`; index avg `0.0268` n `25`; metal avg `-0.2238` n `20`; unknown avg `-0.0842` n `741`
- 24h: commodity avg `0.6972` n `12`; crypto_alt avg `0.3014` n `230`; crypto_major avg `0.1824` n `8`; equity avg `0.4729` n `98`; fx avg `-0.083` n `6`; index avg `0.1586` n `25`; metal avg `-0.1419` n `20`; unknown avg `1.6082` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0795`, n `666`, weak_sample_signal
