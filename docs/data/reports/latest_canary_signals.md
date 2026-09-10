# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T20:07:26.293365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0504` n `12`; crypto_alt avg `0.1425` n `233`; crypto_major avg `0.1415` n `8`; equity avg `-0.125` n `135`; fx avg `0.0089` n `6`; index avg `0.001` n `26`; metal avg `0.0037` n `20`; unknown avg `0.1401` n `775`
- 1h: commodity avg `0.115` n `12`; crypto_alt avg `-0.0594` n `233`; crypto_major avg `0.0303` n `8`; equity avg `-0.29` n `135`; fx avg `0.0229` n `6`; index avg `0.0187` n `26`; metal avg `0.016` n `20`; unknown avg `-0.2419` n `775`
- 4h: commodity avg `0.2901` n `12`; crypto_alt avg `0.3952` n `233`; crypto_major avg `0.5554` n `8`; equity avg `-0.7515` n `135`; fx avg `0.0295` n `6`; index avg `-0.0406` n `26`; metal avg `-0.2667` n `20`; unknown avg `-0.4595` n `768`
- 24h: commodity avg `1.04` n `12`; crypto_alt avg `-3.0658` n `233`; crypto_major avg `-2.2995` n `8`; equity avg `-2.2254` n `135`; fx avg `0.1175` n `6`; index avg `-0.3201` n `26`; metal avg `-1.2387` n `20`; unknown avg `-1.1985` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
