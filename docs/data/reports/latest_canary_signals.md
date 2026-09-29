# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T20:02:42.962547+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `-0.1834` n `234`; crypto_major avg `-0.1558` n `8`; equity avg `-0.0187` n `142`; fx avg `-0.0033` n `6`; index avg `0.0094` n `26`; metal avg `0.0247` n `20`; unknown avg `15.1332` n `952`
- 1h: commodity avg `-0.0517` n `12`; crypto_alt avg `-0.854` n `234`; crypto_major avg `-0.6483` n `8`; equity avg `-0.1286` n `142`; fx avg `0.008` n `6`; index avg `-0.0029` n `26`; metal avg `0.0094` n `20`; unknown avg `100.643` n `952`
- 4h: commodity avg `-0.364` n `12`; crypto_alt avg `-0.5696` n `234`; crypto_major avg `-0.2695` n `8`; equity avg `-0.1223` n `142`; fx avg `0.0017` n `6`; index avg `0.0694` n `26`; metal avg `0.2736` n `20`; unknown avg `12.5077` n `952`
- 24h: commodity avg `-0.911` n `12`; crypto_alt avg `0.3551` n `234`; crypto_major avg `-0.6507` n `8`; equity avg `0.6752` n `142`; fx avg `-0.1732` n `6`; index avg `0.0687` n `26`; metal avg `0.1996` n `20`; unknown avg `-0.2083` n `832`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1943`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1925`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1886`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
