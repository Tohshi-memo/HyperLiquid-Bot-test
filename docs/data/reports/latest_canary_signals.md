# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T21:37:24.233429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0134` n `12`; crypto_alt avg `0.1363` n `230`; crypto_major avg `0.119` n `8`; equity avg `0.0807` n `100`; fx avg `-0.0023` n `6`; index avg `0.0115` n `25`; metal avg `0.0075` n `20`; unknown avg `0.0041` n `774`
- 1h: commodity avg `0.077` n `12`; crypto_alt avg `-0.1211` n `230`; crypto_major avg `-0.2088` n `8`; equity avg `0.0054` n `100`; fx avg `-0.0084` n `6`; index avg `0.0229` n `25`; metal avg `0.0053` n `20`; unknown avg `0.0002` n `774`
- 4h: commodity avg `0.3296` n `12`; crypto_alt avg `-0.3297` n `230`; crypto_major avg `-0.3322` n `8`; equity avg `-1.0394` n `100`; fx avg `-0.0173` n `6`; index avg `-0.1762` n `25`; metal avg `-0.1541` n `20`; unknown avg `-0.0656` n `773`
- 24h: commodity avg `-0.2672` n `12`; crypto_alt avg `-1.0597` n `230`; crypto_major avg `-1.0802` n `8`; equity avg `-3.2529` n `100`; fx avg `-0.1686` n `6`; index avg `-0.4742` n `25`; metal avg `-0.0312` n `20`; unknown avg `14.0773` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1268`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.122`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1123`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.11`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
