# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T23:52:27.064602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `0.1062` n `230`; crypto_major avg `0.1328` n `8`; equity avg `0.1666` n `98`; fx avg `-0.003` n `6`; index avg `0.0392` n `25`; metal avg `0.0427` n `20`; unknown avg `-0.0309` n `773`
- 1h: commodity avg `-0.0186` n `12`; crypto_alt avg `-0.1285` n `230`; crypto_major avg `0.0207` n `8`; equity avg `0.1859` n `98`; fx avg `0.0133` n `6`; index avg `0.0645` n `25`; metal avg `0.0764` n `20`; unknown avg `0.0542` n `773`
- 4h: commodity avg `0.1942` n `12`; crypto_alt avg `0.015` n `230`; crypto_major avg `0.2358` n `8`; equity avg `0.2351` n `98`; fx avg `-0.006` n `6`; index avg `0.0177` n `25`; metal avg `-0.0446` n `20`; unknown avg `0.1365` n `773`
- 24h: commodity avg `0.652` n `12`; crypto_alt avg `-0.527` n `230`; crypto_major avg `-0.5272` n `8`; equity avg `-1.0975` n `98`; fx avg `-0.0576` n `6`; index avg `-0.1467` n `25`; metal avg `0.1973` n `20`; unknown avg `1.6601` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0929`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0784`, n `666`, weak_sample_signal
