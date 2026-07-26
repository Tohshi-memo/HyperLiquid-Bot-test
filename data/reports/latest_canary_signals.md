# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T19:37:27.336511+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `12`; crypto_alt avg `0.026` n `230`; crypto_major avg `-0.0041` n `8`; equity avg `-0.0196` n `100`; fx avg `0.0037` n `6`; index avg `-0.0001` n `25`; metal avg `-0.0019` n `20`; unknown avg `-0.0987` n `775`
- 1h: commodity avg `0.0916` n `12`; crypto_alt avg `0.019` n `230`; crypto_major avg `-0.0262` n `8`; equity avg `-0.0434` n `100`; fx avg `0.0253` n `6`; index avg `-0.0193` n `25`; metal avg `0.022` n `20`; unknown avg `-0.2301` n `775`
- 4h: commodity avg `0.223` n `12`; crypto_alt avg `-0.0759` n `230`; crypto_major avg `-0.1768` n `8`; equity avg `-0.0334` n `100`; fx avg `0.026` n `6`; index avg `-0.0119` n `25`; metal avg `0.052` n `20`; unknown avg `-0.3287` n `775`
- 24h: commodity avg `-0.1511` n `12`; crypto_alt avg `0.83` n `230`; crypto_major avg `0.7243` n `8`; equity avg `0.6478` n `100`; fx avg `0.0402` n `6`; index avg `0.1221` n `25`; metal avg `0.2119` n `20`; unknown avg `-0.1129` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
