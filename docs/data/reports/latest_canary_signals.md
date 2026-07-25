# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T20:07:31.181009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `-0.0298` n `230`; crypto_major avg `-0.0233` n `8`; equity avg `-0.0088` n `100`; fx avg `-0.0027` n `6`; index avg `0.0009` n `25`; metal avg `0.0021` n `20`; unknown avg `0.0479` n `774`
- 1h: commodity avg `-0.0045` n `12`; crypto_alt avg `-0.0794` n `230`; crypto_major avg `-0.1339` n `8`; equity avg `0.0324` n `100`; fx avg `0.0035` n `6`; index avg `0.0139` n `25`; metal avg `-0.0074` n `20`; unknown avg `0.1057` n `774`
- 4h: commodity avg `-0.0521` n `12`; crypto_alt avg `0.2268` n `230`; crypto_major avg `0.5081` n `8`; equity avg `0.2352` n `100`; fx avg `-0.0061` n `6`; index avg `0.0459` n `25`; metal avg `0.0204` n `20`; unknown avg `-0.1134` n `774`
- 24h: commodity avg `-0.5103` n `12`; crypto_alt avg `0.3835` n `230`; crypto_major avg `1.0774` n `8`; equity avg `0.3269` n `100`; fx avg `-0.0111` n `6`; index avg `0.135` n `25`; metal avg `0.0354` n `20`; unknown avg `-0.2667` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1332`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.119`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1152`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1118`, n `666`, weak_sample_signal
