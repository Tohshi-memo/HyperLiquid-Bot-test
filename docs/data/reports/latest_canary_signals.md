# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T19:23:00.220061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0333` n `12`; crypto_alt avg `0.0163` n `230`; crypto_major avg `0.0253` n `8`; equity avg `0.075` n `98`; fx avg `-0.0003` n `6`; index avg `-0.0049` n `25`; metal avg `-0.0152` n `20`; unknown avg `0.0467` n `773`
- 1h: commodity avg `0.0029` n `12`; crypto_alt avg `-0.1838` n `230`; crypto_major avg `-0.0777` n `8`; equity avg `0.0841` n `98`; fx avg `-0.0036` n `6`; index avg `-0.0016` n `25`; metal avg `-0.007` n `20`; unknown avg `0.0798` n `773`
- 4h: commodity avg `0.111` n `12`; crypto_alt avg `-0.4994` n `230`; crypto_major avg `-0.32` n `8`; equity avg `-0.6832` n `98`; fx avg `0.0092` n `6`; index avg `-0.047` n `25`; metal avg `-0.1989` n `20`; unknown avg `0.1789` n `773`
- 24h: commodity avg `0.5757` n `12`; crypto_alt avg `-0.4897` n `230`; crypto_major avg `-0.5623` n `8`; equity avg `-0.3435` n `98`; fx avg `-0.0472` n `6`; index avg `-0.1185` n `25`; metal avg `0.2342` n `20`; unknown avg `1.3921` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0886`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0736`, n `666`, weak_sample_signal
