# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T02:52:24.409060+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0511` n `12`; crypto_alt avg `0.032` n `230`; crypto_major avg `0.1026` n `8`; equity avg `0.1088` n `98`; fx avg `-0.0014` n `6`; index avg `0.0105` n `25`; metal avg `0.056` n `20`; unknown avg `-0.0037` n `773`
- 1h: commodity avg `0.0717` n `12`; crypto_alt avg `-0.1836` n `230`; crypto_major avg `-0.1155` n `8`; equity avg `-0.4515` n `98`; fx avg `0.0182` n `6`; index avg `-0.1066` n `25`; metal avg `0.0445` n `20`; unknown avg `0.027` n `773`
- 4h: commodity avg `0.1621` n `12`; crypto_alt avg `-0.3538` n `230`; crypto_major avg `-0.2519` n `8`; equity avg `-0.0433` n `98`; fx avg `-0.0582` n `6`; index avg `0.0419` n `25`; metal avg `0.1903` n `20`; unknown avg `-0.0636` n `773`
- 24h: commodity avg `0.7654` n `12`; crypto_alt avg `-0.8221` n `230`; crypto_major avg `-0.8121` n `8`; equity avg `-0.9154` n `98`; fx avg `-0.1275` n `6`; index avg `-0.1702` n `25`; metal avg `-0.0548` n `20`; unknown avg `1.7681` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0892`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
