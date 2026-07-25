# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T01:22:25.634876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0247` n `12`; crypto_alt avg `-0.1808` n `230`; crypto_major avg `-0.1694` n `8`; equity avg `-0.0546` n `100`; fx avg `-0.0081` n `6`; index avg `-0.0092` n `25`; metal avg `-0.0078` n `20`; unknown avg `0.1182` n `774`
- 1h: commodity avg `0.0568` n `12`; crypto_alt avg `-0.0378` n `230`; crypto_major avg `-0.1289` n `8`; equity avg `-0.0157` n `100`; fx avg `0.022` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0167` n `20`; unknown avg `0.0014` n `774`
- 4h: commodity avg `-0.0891` n `12`; crypto_alt avg `0.1371` n `230`; crypto_major avg `0.15` n `8`; equity avg `-0.0153` n `100`; fx avg `0.0452` n `6`; index avg `0.0163` n `25`; metal avg `-0.0003` n `20`; unknown avg `-0.1601` n `774`
- 24h: commodity avg `-0.2341` n `12`; crypto_alt avg `-0.8049` n `230`; crypto_major avg `-0.9067` n `8`; equity avg `-3.0214` n `100`; fx avg `-0.0408` n `6`; index avg `-0.3404` n `25`; metal avg `0.0818` n `20`; unknown avg `14.0143` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1245`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1166`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1089`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1071`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1051`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
