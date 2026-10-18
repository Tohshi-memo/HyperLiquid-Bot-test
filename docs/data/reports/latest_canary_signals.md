# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T13:22:25.022261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `13`; crypto_alt avg `-0.019` n `237`; crypto_major avg `-0.1011` n `8`; equity avg `-0.0795` n `151`; fx avg `-0.0023` n `6`; index avg `-0.0098` n `26`; metal avg `-0.0016` n `20`; unknown avg `-0.3967` n `1193`
- 1h: commodity avg `-0.034` n `13`; crypto_alt avg `0.0906` n `237`; crypto_major avg `-0.2921` n `8`; equity avg `-0.1976` n `151`; fx avg `-0.0079` n `6`; index avg `-0.0345` n `26`; metal avg `-0.0039` n `20`; unknown avg `-0.4364` n `1191`
- 4h: commodity avg `0.0163` n `13`; crypto_alt avg `0.3376` n `237`; crypto_major avg `-0.0338` n `8`; equity avg `-0.1731` n `151`; fx avg `0.0014` n `6`; index avg `-0.0312` n `26`; metal avg `0.0207` n `20`; unknown avg `3.6271` n `1185`
- 24h: commodity avg `0.0533` n `13`; crypto_alt avg `-1.451` n `236`; crypto_major avg `-0.0225` n `8`; equity avg `-0.5875` n `151`; fx avg `-0.05` n `6`; index avg `-0.061` n `26`; metal avg `-0.0266` n `20`; unknown avg `1.4296` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2081`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1387`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1319`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.081`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
