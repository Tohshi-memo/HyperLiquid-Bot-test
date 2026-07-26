# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T01:37:32.333418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `0.0721` n `230`; crypto_major avg `0.0466` n `8`; equity avg `0.0967` n `100`; fx avg `-0.0022` n `6`; index avg `0.0176` n `25`; metal avg `0.003` n `20`; unknown avg `-0.1288` n `774`
- 1h: commodity avg `-0.0032` n `12`; crypto_alt avg `0.1121` n `230`; crypto_major avg `0.0814` n `8`; equity avg `0.1618` n `100`; fx avg `-0.0119` n `6`; index avg `0.0149` n `25`; metal avg `0.0027` n `20`; unknown avg `-0.1911` n `774`
- 4h: commodity avg `-0.1051` n `12`; crypto_alt avg `0.0175` n `230`; crypto_major avg `0.0696` n `8`; equity avg `0.2347` n `100`; fx avg `-0.0085` n `6`; index avg `0.0362` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.3478` n `774`
- 24h: commodity avg `-0.6073` n `12`; crypto_alt avg `0.5222` n `230`; crypto_major avg `1.0972` n `8`; equity avg `0.6157` n `100`; fx avg `-0.0352` n `6`; index avg `0.1636` n `25`; metal avg `0.0339` n `20`; unknown avg `-0.2479` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1798`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1346`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1234`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1175`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1162`, n `666`, weak_sample_signal
