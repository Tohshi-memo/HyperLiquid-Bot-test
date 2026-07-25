# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T22:37:27.141029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0811` n `12`; crypto_alt avg `-0.0334` n `230`; crypto_major avg `-0.0077` n `8`; equity avg `-0.0038` n `100`; fx avg `0.0013` n `6`; index avg `0.0029` n `25`; metal avg `-0.0038` n `20`; unknown avg `-0.0071` n `774`
- 1h: commodity avg `-0.1151` n `12`; crypto_alt avg `-0.0096` n `230`; crypto_major avg `-0.0387` n `8`; equity avg `0.0279` n `100`; fx avg `-0.0008` n `6`; index avg `0.0026` n `25`; metal avg `-0.0005` n `20`; unknown avg `-0.0773` n `774`
- 4h: commodity avg `-0.1477` n `12`; crypto_alt avg `-0.049` n `230`; crypto_major avg `-0.245` n `8`; equity avg `0.091` n `100`; fx avg `0.0217` n `6`; index avg `0.0216` n `25`; metal avg `-0.0002` n `20`; unknown avg `-0.071` n `774`
- 24h: commodity avg `-0.6533` n `12`; crypto_alt avg `0.5709` n `230`; crypto_major avg `1.1248` n `8`; equity avg `0.3879` n `100`; fx avg `0.0025` n `6`; index avg `0.1482` n `25`; metal avg `0.0064` n `20`; unknown avg `-0.2886` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1349`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1228`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1165`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1153`, n `666`, weak_sample_signal
