# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T21:37:27.674210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0263` n `12`; crypto_alt avg `-0.1639` n `230`; crypto_major avg `-0.1212` n `8`; equity avg `-0.0104` n `102`; fx avg `-0.0011` n `6`; index avg `0.0083` n `25`; metal avg `-0.0025` n `20`; unknown avg `0.1482` n `774`
- 1h: commodity avg `0.0401` n `12`; crypto_alt avg `-0.2038` n `230`; crypto_major avg `-0.3019` n `8`; equity avg `0.0189` n `102`; fx avg `-0.009` n `6`; index avg `-0.0208` n `25`; metal avg `0.0106` n `20`; unknown avg `3.7016` n `774`
- 4h: commodity avg `-0.1358` n `12`; crypto_alt avg `-0.1656` n `230`; crypto_major avg `-0.401` n `8`; equity avg `0.9684` n `102`; fx avg `0.0052` n `6`; index avg `0.1678` n `25`; metal avg `0.04` n `20`; unknown avg `98.6383` n `774`
- 24h: commodity avg `-0.9628` n `12`; crypto_alt avg `-1.1815` n `230`; crypto_major avg `-0.6368` n `8`; equity avg `-0.9731` n `102`; fx avg `-0.0417` n `6`; index avg `-0.3289` n `25`; metal avg `0.1497` n `20`; unknown avg `97.6232` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.194`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
