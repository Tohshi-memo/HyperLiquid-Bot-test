# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T22:52:33.328110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `13`; crypto_alt avg `-0.0656` n `235`; crypto_major avg `-0.0147` n `8`; equity avg `0.026` n `143`; fx avg `-0.0031` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0022` n `20`; unknown avg `0.1574` n `1079`
- 1h: commodity avg `-0.0502` n `13`; crypto_alt avg `0.0529` n `235`; crypto_major avg `0.1187` n `8`; equity avg `0.0662` n `143`; fx avg `0.0121` n `6`; index avg `0.0034` n `26`; metal avg `-0.0022` n `20`; unknown avg `0.2794` n `1075`
- 4h: commodity avg `0.1096` n `13`; crypto_alt avg `0.5062` n `235`; crypto_major avg `0.0538` n `8`; equity avg `0.1242` n `143`; fx avg `0.0322` n `6`; index avg `0.0097` n `26`; metal avg `0.0057` n `20`; unknown avg `0.5561` n `1046`
- 24h: commodity avg `-0.0774` n `13`; crypto_alt avg `2.3342` n `235`; crypto_major avg `1.0503` n `8`; equity avg `0.2501` n `143`; fx avg `-0.0018` n `6`; index avg `0.0462` n `26`; metal avg `-0.0295` n `20`; unknown avg `0.1484` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1997`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
