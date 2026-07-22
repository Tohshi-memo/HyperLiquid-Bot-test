# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T22:22:26.809737+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.021` n `12`; crypto_alt avg `-0.1068` n `230`; crypto_major avg `-0.0448` n `8`; equity avg `-0.034` n `98`; fx avg `-0.0056` n `6`; index avg `0.0083` n `25`; metal avg `0.0013` n `20`; unknown avg `0.0221` n `773`
- 1h: commodity avg `0.2082` n `12`; crypto_alt avg `-0.0267` n `230`; crypto_major avg `0.0936` n `8`; equity avg `-0.2941` n `98`; fx avg `-0.0277` n `6`; index avg `-0.0417` n `25`; metal avg `-0.1041` n `20`; unknown avg `-0.031` n `773`
- 4h: commodity avg `0.1932` n `12`; crypto_alt avg `-0.0412` n `230`; crypto_major avg `-0.0434` n `8`; equity avg `0.0959` n `98`; fx avg `-0.0308` n `6`; index avg `-0.0295` n `25`; metal avg `-0.1019` n `20`; unknown avg `0.0582` n `773`
- 24h: commodity avg `0.7418` n `12`; crypto_alt avg `-0.3353` n `230`; crypto_major avg `-0.468` n `8`; equity avg `-1.0889` n `98`; fx avg `-0.0607` n `6`; index avg `-0.1724` n `25`; metal avg `0.1751` n `20`; unknown avg `1.6876` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0902`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0748`, n `666`, weak_sample_signal
