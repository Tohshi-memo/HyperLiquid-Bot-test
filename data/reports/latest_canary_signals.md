# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T05:52:29.607781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0551` n `12`; crypto_alt avg `-0.1415` n `230`; crypto_major avg `-0.1676` n `8`; equity avg `-0.2538` n `98`; fx avg `0.007` n `6`; index avg `-0.0545` n `25`; metal avg `-0.027` n `20`; unknown avg `0.1487` n `773`
- 1h: commodity avg `0.0315` n `12`; crypto_alt avg `0.0028` n `230`; crypto_major avg `-0.0609` n `8`; equity avg `-0.0434` n `98`; fx avg `-0.0064` n `6`; index avg `-0.0098` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.1419` n `773`
- 4h: commodity avg `0.0737` n `12`; crypto_alt avg `-0.2191` n `230`; crypto_major avg `-0.3414` n `8`; equity avg `-0.2453` n `98`; fx avg `0.0233` n `6`; index avg `-0.0474` n `25`; metal avg `0.0234` n `20`; unknown avg `-0.3056` n `773`
- 24h: commodity avg `0.8223` n `12`; crypto_alt avg `-0.1966` n `230`; crypto_major avg `-0.1261` n `8`; equity avg `0.2995` n `98`; fx avg `-0.1368` n `6`; index avg `0.081` n `25`; metal avg `-0.1208` n `20`; unknown avg `1.6005` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0773`, n `666`, weak_sample_signal
