# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T20:07:43.405523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0212` n `12`; crypto_alt avg `0.1728` n `234`; crypto_major avg `0.0477` n `8`; equity avg `0.004` n `142`; fx avg `-0.0017` n `6`; index avg `0.0053` n `26`; metal avg `0.0293` n `20`; unknown avg `15.7009` n `952`
- 1h: commodity avg `-0.0555` n `12`; crypto_alt avg `-0.5014` n `234`; crypto_major avg `-0.4463` n `8`; equity avg `-0.1061` n `142`; fx avg `0.0096` n `6`; index avg `-0.007` n `26`; metal avg `0.014` n `20`; unknown avg `100.7687` n `952`
- 4h: commodity avg `-0.3678` n `12`; crypto_alt avg `-0.2155` n `234`; crypto_major avg `-0.0669` n `8`; equity avg `-0.0998` n `142`; fx avg `0.0033` n `6`; index avg `0.0653` n `26`; metal avg `0.2782` n `20`; unknown avg `12.4952` n `952`
- 24h: commodity avg `-0.9146` n `12`; crypto_alt avg `0.7139` n `234`; crypto_major avg `-0.4489` n `8`; equity avg `0.6978` n `142`; fx avg `-0.1716` n `6`; index avg `0.0646` n `26`; metal avg `0.2042` n `20`; unknown avg `-0.3101` n `832`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1944`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1925`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1884`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
