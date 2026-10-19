# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T12:07:29.754534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `13`; crypto_alt avg `0.3967` n `237`; crypto_major avg `0.1942` n `8`; equity avg `0.1139` n `151`; fx avg `0.0202` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0077` n `20`; unknown avg `0.0294` n `1183`
- 1h: commodity avg `-0.0968` n `13`; crypto_alt avg `0.3892` n `237`; crypto_major avg `0.3253` n `8`; equity avg `0.3278` n `151`; fx avg `0.019` n `6`; index avg `-0.0098` n `26`; metal avg `-0.0477` n `20`; unknown avg `0.0774` n `1181`
- 4h: commodity avg `0.3692` n `13`; crypto_alt avg `-0.4299` n `237`; crypto_major avg `-0.184` n `8`; equity avg `0.3345` n `151`; fx avg `0.054` n `6`; index avg `-0.0153` n `26`; metal avg `0.0164` n `20`; unknown avg `0.2271` n `1181`
- 24h: commodity avg `-0.1912` n `13`; crypto_alt avg `-0.3564` n `237`; crypto_major avg `0.2727` n `8`; equity avg `2.795` n `151`; fx avg `-0.0177` n `6`; index avg `0.4268` n `26`; metal avg `0.2309` n `20`; unknown avg `0.8671` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1973`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1475`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.132`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1123`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
