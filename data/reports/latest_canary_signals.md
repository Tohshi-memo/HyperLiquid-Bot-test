# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T08:37:25.430370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0951` n `12`; crypto_alt avg `0.0385` n `232`; crypto_major avg `0.0855` n `8`; equity avg `-0.0325` n `128`; fx avg `0.0092` n `6`; index avg `0.0011` n `26`; metal avg `0.011` n `20`; unknown avg `0.1172` n `793`
- 1h: commodity avg `0.2504` n `12`; crypto_alt avg `-0.2367` n `232`; crypto_major avg `-0.0818` n `8`; equity avg `-0.1256` n `128`; fx avg `-0.0202` n `6`; index avg `0.002` n `26`; metal avg `-0.0495` n `20`; unknown avg `0.1556` n `791`
- 4h: commodity avg `0.0966` n `12`; crypto_alt avg `0.8652` n `232`; crypto_major avg `0.8437` n `8`; equity avg `0.8766` n `128`; fx avg `-0.0787` n `6`; index avg `0.1543` n `26`; metal avg `0.1442` n `20`; unknown avg `0.6058` n `773`
- 24h: commodity avg `0.4947` n `12`; crypto_alt avg `0.1146` n `231`; crypto_major avg `-1.3142` n `8`; equity avg `-0.2567` n `128`; fx avg `-0.134` n `6`; index avg `-0.0285` n `26`; metal avg `-0.2323` n `20`; unknown avg `-0.3265` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
