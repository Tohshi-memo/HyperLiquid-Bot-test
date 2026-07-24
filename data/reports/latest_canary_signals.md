# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T04:52:29.617669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0347` n `12`; crypto_alt avg `-0.0253` n `230`; crypto_major avg `-0.0818` n `8`; equity avg `-0.0485` n `100`; fx avg `-0.0017` n `6`; index avg `-0.018` n `25`; metal avg `-0.0063` n `20`; unknown avg `1.3915` n `772`
- 1h: commodity avg `-0.0666` n `12`; crypto_alt avg `-0.0803` n `230`; crypto_major avg `-0.232` n `8`; equity avg `0.01` n `100`; fx avg `0.016` n `6`; index avg `-0.0153` n `25`; metal avg `-0.0491` n `20`; unknown avg `0.1854` n `772`
- 4h: commodity avg `-0.0504` n `12`; crypto_alt avg `0.543` n `230`; crypto_major avg `0.2979` n `8`; equity avg `-0.5693` n `100`; fx avg `-0.039` n `6`; index avg `-0.1932` n `25`; metal avg `-0.2179` n `20`; unknown avg `0.7447` n `772`
- 24h: commodity avg `0.4968` n `12`; crypto_alt avg `-1.0856` n `230`; crypto_major avg `-1.7544` n `8`; equity avg `-2.2273` n `99`; fx avg `-0.1008` n `6`; index avg `-0.6125` n `25`; metal avg `-1.0195` n `20`; unknown avg `-0.1171` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1705`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1112`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0976`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0927`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
