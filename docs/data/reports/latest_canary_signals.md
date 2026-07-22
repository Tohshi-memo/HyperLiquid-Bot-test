# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T19:07:31.807389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0284` n `12`; crypto_alt avg `-0.1032` n `230`; crypto_major avg `-0.0639` n `8`; equity avg `0.0466` n `98`; fx avg `-0.0047` n `6`; index avg `0.0036` n `25`; metal avg `-0.0121` n `20`; unknown avg `-0.0555` n `773`
- 1h: commodity avg `0.0843` n `12`; crypto_alt avg `-0.3603` n `230`; crypto_major avg `-0.2895` n `8`; equity avg `-0.1471` n `98`; fx avg `0.001` n `6`; index avg `-0.0158` n `25`; metal avg `-0.0247` n `20`; unknown avg `0.0962` n `773`
- 4h: commodity avg `0.1331` n `12`; crypto_alt avg `-0.3181` n `230`; crypto_major avg `-0.0584` n `8`; equity avg `-0.6258` n `98`; fx avg `0.0191` n `6`; index avg `-0.0179` n `25`; metal avg `-0.1536` n `20`; unknown avg `-0.0454` n `773`
- 24h: commodity avg `0.6103` n `12`; crypto_alt avg `-0.5652` n `230`; crypto_major avg `-0.6376` n `8`; equity avg `-0.3657` n `98`; fx avg `-0.0417` n `6`; index avg `-0.1141` n `25`; metal avg `0.2519` n `20`; unknown avg `1.3583` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0876`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.073`, n `666`, weak_sample_signal
