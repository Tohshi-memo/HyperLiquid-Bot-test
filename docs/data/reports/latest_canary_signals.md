# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T02:37:26.531582+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0116` n `12`; crypto_alt avg `-0.0055` n `230`; crypto_major avg `0.0469` n `8`; equity avg `-0.0663` n `98`; fx avg `0.0085` n `6`; index avg `-0.0176` n `25`; metal avg `0.021` n `20`; unknown avg `0.0129` n `773`
- 1h: commodity avg `0.0438` n `12`; crypto_alt avg `-0.1991` n `230`; crypto_major avg `-0.1255` n `8`; equity avg `-0.7335` n `98`; fx avg `-0.0142` n `6`; index avg `-0.1503` n `25`; metal avg `0.0012` n `20`; unknown avg `0.0008` n `773`
- 4h: commodity avg `0.0583` n `12`; crypto_alt avg `-0.3128` n `230`; crypto_major avg `-0.2073` n `8`; equity avg `-0.1544` n `98`; fx avg `-0.0575` n `6`; index avg `0.0226` n `25`; metal avg `0.1131` n `20`; unknown avg `0.0088` n `773`
- 24h: commodity avg `0.7237` n `12`; crypto_alt avg `-0.8635` n `230`; crypto_major avg `-0.9003` n `8`; equity avg `-1.0901` n `98`; fx avg `-0.1298` n `6`; index avg `-0.183` n `25`; metal avg `-0.1524` n `20`; unknown avg `1.7425` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0848`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
