# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T11:22:32.207239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0314` n `12`; crypto_alt avg `-0.0767` n `230`; crypto_major avg `-0.031` n `8`; equity avg `-0.0129` n `100`; fx avg `-0.0082` n `6`; index avg `0.0022` n `25`; metal avg `-0.0017` n `20`; unknown avg `-0.0474` n `774`
- 1h: commodity avg `-0.069` n `12`; crypto_alt avg `0.0134` n `230`; crypto_major avg `0.0123` n `8`; equity avg `0.0048` n `100`; fx avg `-0.0094` n `6`; index avg `0.0088` n `25`; metal avg `0.0114` n `20`; unknown avg `-0.0624` n `774`
- 4h: commodity avg `-0.0703` n `12`; crypto_alt avg `-0.0253` n `230`; crypto_major avg `0.1649` n `8`; equity avg `-0.0339` n `100`; fx avg `-0.0375` n `6`; index avg `0.0233` n `25`; metal avg `0.0014` n `20`; unknown avg `-0.3047` n `774`
- 24h: commodity avg `-0.1043` n `12`; crypto_alt avg `-1.3024` n `230`; crypto_major avg `-1.0029` n `8`; equity avg `-2.8675` n `100`; fx avg `-0.0203` n `6`; index avg `-0.2529` n `25`; metal avg `-0.141` n `20`; unknown avg `13.1281` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1165`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1007`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
