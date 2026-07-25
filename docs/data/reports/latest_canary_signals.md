# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T02:22:29.067315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0892` n `12`; crypto_alt avg `-0.0348` n `230`; crypto_major avg `-0.0301` n `8`; equity avg `0.0061` n `100`; fx avg `-0.0197` n `6`; index avg `0.0027` n `25`; metal avg `-0.0046` n `20`; unknown avg `0.0082` n `774`
- 1h: commodity avg `-0.077` n `12`; crypto_alt avg `-0.1077` n `230`; crypto_major avg `0.1132` n `8`; equity avg `0.0182` n `100`; fx avg `-0.0282` n `6`; index avg `-0.0034` n `25`; metal avg `-0.004` n `20`; unknown avg `-0.0169` n `774`
- 4h: commodity avg `-0.1185` n `12`; crypto_alt avg `0.2166` n `230`; crypto_major avg `0.3019` n `8`; equity avg `0.0069` n `100`; fx avg `0.0074` n `6`; index avg `0.0225` n `25`; metal avg `-0.0184` n `20`; unknown avg `-0.0853` n `774`
- 24h: commodity avg `-0.3854` n `12`; crypto_alt avg `-1.0867` n `230`; crypto_major avg `-0.8612` n `8`; equity avg `-2.7681` n `100`; fx avg `-0.0426` n `6`; index avg `-0.2547` n `25`; metal avg `0.0821` n `20`; unknown avg `14.0175` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1219`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1153`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1068`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1061`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1032`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
