# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T01:22:28.891542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `12`; crypto_alt avg `0.0653` n `230`; crypto_major avg `0.0055` n `8`; equity avg `0.0358` n `100`; fx avg `-0.0014` n `6`; index avg `0.003` n `25`; metal avg `-0.0` n `20`; unknown avg `-0.0458` n `774`
- 1h: commodity avg `-0.0193` n `12`; crypto_alt avg `0.0402` n `230`; crypto_major avg `-0.0146` n `8`; equity avg `0.0253` n `100`; fx avg `0.0026` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0002` n `20`; unknown avg `-0.0612` n `774`
- 4h: commodity avg `-0.0709` n `12`; crypto_alt avg `0.1501` n `230`; crypto_major avg `0.1985` n `8`; equity avg `0.1279` n `100`; fx avg `-0.0078` n `6`; index avg `0.0252` n `25`; metal avg `0.002` n `20`; unknown avg `-0.2632` n `774`
- 24h: commodity avg `-0.6163` n `12`; crypto_alt avg `0.4578` n `230`; crypto_major avg `1.1864` n `8`; equity avg `0.547` n `100`; fx avg `-0.04` n `6`; index avg `0.1426` n `25`; metal avg `0.0227` n `20`; unknown avg `-0.2438` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1798`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1348`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1236`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1172`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1167`, n `666`, weak_sample_signal
