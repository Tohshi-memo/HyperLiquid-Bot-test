# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T07:37:31.167820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0049` n `12`; crypto_alt avg `-0.0491` n `232`; crypto_major avg `0.0128` n `8`; equity avg `0.0273` n `128`; fx avg `-0.011` n `6`; index avg `0.0015` n `26`; metal avg `0.0169` n `20`; unknown avg `-0.0131` n `793`
- 1h: commodity avg `-0.1908` n `12`; crypto_alt avg `0.1712` n `232`; crypto_major avg `0.1505` n `8`; equity avg `0.0659` n `128`; fx avg `-0.0218` n `6`; index avg `0.0118` n `26`; metal avg `0.0599` n `20`; unknown avg `0.1186` n `791`
- 4h: commodity avg `-0.1302` n `12`; crypto_alt avg `0.7506` n `231`; crypto_major avg `0.6344` n `8`; equity avg `1.0376` n `128`; fx avg `-0.0596` n `6`; index avg `0.1893` n `26`; metal avg `0.2325` n `20`; unknown avg `0.3493` n `773`
- 24h: commodity avg `0.2637` n `12`; crypto_alt avg `0.2854` n `231`; crypto_major avg `-1.2751` n `8`; equity avg `-0.1231` n `128`; fx avg `-0.114` n `6`; index avg `-0.044` n `26`; metal avg `-0.1814` n `20`; unknown avg `-0.4187` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
