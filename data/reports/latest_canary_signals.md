# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T09:22:28.142344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `13`; crypto_alt avg `0.126` n `235`; crypto_major avg `0.1816` n `8`; equity avg `0.0166` n `143`; fx avg `0.0005` n `6`; index avg `0.0038` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.3455` n `1079`
- 1h: commodity avg `0.0267` n `13`; crypto_alt avg `-0.1119` n `235`; crypto_major avg `0.1108` n `8`; equity avg `0.0145` n `143`; fx avg `0.0` n `6`; index avg `0.0054` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.4749` n `1077`
- 4h: commodity avg `0.0058` n `13`; crypto_alt avg `0.3054` n `235`; crypto_major avg `0.4774` n `8`; equity avg `-0.0121` n `143`; fx avg `-0.0163` n `6`; index avg `-0.0054` n `26`; metal avg `0.0029` n `20`; unknown avg `0.335` n `1033`
- 24h: commodity avg `0.1742` n `13`; crypto_alt avg `2.583` n `235`; crypto_major avg `1.3897` n `8`; equity avg `0.2577` n `143`; fx avg `-0.0323` n `6`; index avg `0.0243` n `26`; metal avg `0.0069` n `20`; unknown avg `-0.1741` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1941`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
