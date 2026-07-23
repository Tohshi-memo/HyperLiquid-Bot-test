# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T07:22:38.528390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0511` n `12`; crypto_alt avg `-0.2712` n `230`; crypto_major avg `-0.232` n `8`; equity avg `-0.1084` n `98`; fx avg `0.0052` n `6`; index avg `-0.0162` n `25`; metal avg `-0.0337` n `20`; unknown avg `0.1475` n `773`
- 1h: commodity avg `0.1963` n `12`; crypto_alt avg `-0.226` n `230`; crypto_major avg `-0.2238` n `8`; equity avg `-0.2204` n `98`; fx avg `0.0242` n `6`; index avg `-0.0453` n `25`; metal avg `-0.1894` n `20`; unknown avg `0.1306` n `773`
- 4h: commodity avg `0.1594` n `12`; crypto_alt avg `0.0506` n `230`; crypto_major avg `-0.2843` n `8`; equity avg `-0.0014` n `98`; fx avg `0.019` n `6`; index avg `0.0225` n `25`; metal avg `-0.3125` n `20`; unknown avg `-0.2164` n `741`
- 24h: commodity avg `0.7322` n `12`; crypto_alt avg `-0.0088` n `230`; crypto_major avg `-0.0224` n `8`; equity avg `0.224` n `98`; fx avg `-0.0905` n `6`; index avg `0.1087` n `25`; metal avg `-0.2487` n `20`; unknown avg `1.6239` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0807`, n `666`, weak_sample_signal
