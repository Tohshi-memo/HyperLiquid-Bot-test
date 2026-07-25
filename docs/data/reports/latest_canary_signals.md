# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T04:22:28.722816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `12`; crypto_alt avg `0.0944` n `230`; crypto_major avg `0.0311` n `8`; equity avg `0.0452` n `100`; fx avg `-0.0003` n `6`; index avg `0.0162` n `25`; metal avg `0.0006` n `20`; unknown avg `0.0087` n `774`
- 1h: commodity avg `-0.0005` n `12`; crypto_alt avg `0.1277` n `230`; crypto_major avg `0.0427` n `8`; equity avg `0.071` n `100`; fx avg `0.0012` n `6`; index avg `0.0106` n `25`; metal avg `-0.0074` n `20`; unknown avg `-0.1456` n `774`
- 4h: commodity avg `-0.1078` n `12`; crypto_alt avg `0.0515` n `230`; crypto_major avg `0.0468` n `8`; equity avg `0.2596` n `100`; fx avg `-0.0117` n `6`; index avg `0.0362` n `25`; metal avg `-0.0313` n `20`; unknown avg `0.0945` n `774`
- 24h: commodity avg `-0.4909` n `12`; crypto_alt avg `-1.0739` n `230`; crypto_major avg `-0.9357` n `8`; equity avg `-2.0877` n `100`; fx avg `-0.0585` n `6`; index avg `-0.1179` n `25`; metal avg `0.1751` n `20`; unknown avg `13.8193` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1152`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1072`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.102`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.102`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
