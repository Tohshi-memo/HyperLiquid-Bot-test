# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T08:22:31.252393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.1131` n `230`; crypto_major avg `0.0748` n `8`; equity avg `0.1229` n `98`; fx avg `0.0012` n `6`; index avg `0.0106` n `25`; metal avg `-0.0421` n `20`; unknown avg `-0.0205` n `773`
- 1h: commodity avg `-0.0446` n `12`; crypto_alt avg `0.2338` n `230`; crypto_major avg `0.134` n `8`; equity avg `0.2716` n `98`; fx avg `0.0047` n `6`; index avg `0.017` n `25`; metal avg `-0.1136` n `20`; unknown avg `-0.0478` n `773`
- 4h: commodity avg `0.1805` n `12`; crypto_alt avg `0.0629` n `230`; crypto_major avg `-0.2668` n `8`; equity avg `0.0089` n `98`; fx avg `0.0343` n `6`; index avg `-0.0448` n `25`; metal avg `-0.4242` n `20`; unknown avg `-0.2532` n `741`
- 24h: commodity avg `0.6528` n `12`; crypto_alt avg `-0.0891` n `230`; crypto_major avg `-0.1795` n `8`; equity avg `0.6036` n `98`; fx avg `-0.0847` n `6`; index avg `0.1448` n `25`; metal avg `-0.3193` n `20`; unknown avg `11.5525` n `741`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0833`, n `666`, weak_sample_signal
