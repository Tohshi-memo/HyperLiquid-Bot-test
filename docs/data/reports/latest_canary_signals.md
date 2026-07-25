# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T04:37:34.099230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0261` n `12`; crypto_alt avg `-0.0605` n `230`; crypto_major avg `-0.0073` n `8`; equity avg `-0.0368` n `100`; fx avg `-0.0061` n `6`; index avg `-0.0005` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.101` n `774`
- 1h: commodity avg `-0.0048` n `12`; crypto_alt avg `-0.0196` n `230`; crypto_major avg `-0.0007` n `8`; equity avg `0.0399` n `100`; fx avg `-0.0064` n `6`; index avg `0.0093` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.2668` n `774`
- 4h: commodity avg `-0.0851` n `12`; crypto_alt avg `-0.0518` n `230`; crypto_major avg `-0.02` n `8`; equity avg `0.2301` n `100`; fx avg `-0.0277` n `6`; index avg `0.0427` n `25`; metal avg `-0.0313` n `20`; unknown avg `0.0082` n `774`
- 24h: commodity avg `-0.4672` n `12`; crypto_alt avg `-1.1083` n `230`; crypto_major avg `-0.9392` n `8`; equity avg `-2.2431` n `100`; fx avg `-0.0788` n `6`; index avg `-0.1325` n `25`; metal avg `0.1897` n `20`; unknown avg `13.8575` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1149`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1065`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1022`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1016`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
