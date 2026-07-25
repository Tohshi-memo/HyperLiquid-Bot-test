# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T00:07:31.183803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `12`; crypto_alt avg `0.0462` n `230`; crypto_major avg `0.0035` n `8`; equity avg `0.2056` n `100`; fx avg `0.019` n `6`; index avg `0.0582` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.1395` n `774`
- 1h: commodity avg `-0.0575` n `12`; crypto_alt avg `0.0109` n `230`; crypto_major avg `0.0538` n `8`; equity avg `0.043` n `100`; fx avg `0.0043` n `6`; index avg `0.042` n `25`; metal avg `-0.0017` n `20`; unknown avg `-0.1918` n `774`
- 4h: commodity avg `0.0518` n `12`; crypto_alt avg `-0.1081` n `230`; crypto_major avg `-0.0605` n `8`; equity avg `0.0228` n `100`; fx avg `0.0444` n `6`; index avg `0.0428` n `25`; metal avg `0.0276` n `20`; unknown avg `-0.1779` n `774`
- 24h: commodity avg `-0.3983` n `12`; crypto_alt avg `-0.6077` n `230`; crypto_major avg `-0.6395` n `8`; equity avg `-2.96` n `100`; fx avg `-0.0846` n `6`; index avg `-0.375` n `25`; metal avg `0.0491` n `20`; unknown avg `14.0058` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.128`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1213`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1116`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1112`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1081`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
