# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T22:07:31.887244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1092` n `12`; crypto_alt avg `-0.019` n `230`; crypto_major avg `-0.0498` n `8`; equity avg `-0.0729` n `98`; fx avg `-0.0068` n `6`; index avg `-0.022` n `25`; metal avg `-0.088` n `20`; unknown avg `-0.091` n `773`
- 1h: commodity avg `0.247` n `12`; crypto_alt avg `0.0548` n `230`; crypto_major avg `0.1195` n `8`; equity avg `-0.406` n `98`; fx avg `-0.0236` n `6`; index avg `-0.0921` n `25`; metal avg `-0.0876` n `20`; unknown avg `-0.0641` n `773`
- 4h: commodity avg `0.2203` n `12`; crypto_alt avg `-0.095` n `230`; crypto_major avg `-0.185` n `8`; equity avg `-0.0253` n `98`; fx avg `-0.0209` n `6`; index avg `-0.0569` n `25`; metal avg `-0.136` n `20`; unknown avg `0.0316` n `773`
- 24h: commodity avg `0.7175` n `12`; crypto_alt avg `-0.284` n `230`; crypto_major avg `-0.439` n `8`; equity avg `-1.0032` n `98`; fx avg `-0.0551` n `6`; index avg `-0.1764` n `25`; metal avg `0.1788` n `20`; unknown avg `1.6401` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0897`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.074`, n `666`, weak_sample_signal
