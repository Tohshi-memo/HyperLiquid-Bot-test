# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T02:37:28.485389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `0.1491` n `230`; crypto_major avg `0.2134` n `8`; equity avg `0.3251` n `98`; fx avg `0.0021` n `6`; index avg `0.0758` n `25`; metal avg `0.1438` n `20`; unknown avg `0.1699` n `771`
- 1h: commodity avg `0.0244` n `12`; crypto_alt avg `-0.0806` n `230`; crypto_major avg `-0.0756` n `8`; equity avg `-0.1546` n `98`; fx avg `0.0126` n `6`; index avg `-0.0089` n `25`; metal avg `0.1207` n `20`; unknown avg `-0.1387` n `771`
- 4h: commodity avg `-0.023` n `12`; crypto_alt avg `0.2954` n `230`; crypto_major avg `0.458` n `8`; equity avg `0.4432` n `98`; fx avg `0.0652` n `6`; index avg `0.2088` n `25`; metal avg `0.2956` n `20`; unknown avg `-0.52` n `770`
- 24h: commodity avg `-0.3255` n `12`; crypto_alt avg `1.3531` n `230`; crypto_major avg `1.2494` n `8`; equity avg `0.2692` n `98`; fx avg `-0.0784` n `6`; index avg `0.1206` n `25`; metal avg `0.2671` n `20`; unknown avg `-0.0787` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.102`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0972`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0826`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
