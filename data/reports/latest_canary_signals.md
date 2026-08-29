# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T15:07:23.696341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.1223` n `231`; crypto_major avg `-0.0561` n `8`; equity avg `-0.0258` n `128`; fx avg `-0.0012` n `6`; index avg `0.0055` n `26`; metal avg `0.0033` n `20`; unknown avg `-0.102` n `792`
- 1h: commodity avg `-0.0061` n `12`; crypto_alt avg `0.5015` n `231`; crypto_major avg `0.5664` n `8`; equity avg `0.0156` n `128`; fx avg `0.0081` n `6`; index avg `0.0147` n `26`; metal avg `0.032` n `20`; unknown avg `0.1798` n `784`
- 4h: commodity avg `0.0062` n `12`; crypto_alt avg `1.0693` n `231`; crypto_major avg `0.8273` n `8`; equity avg `0.0051` n `128`; fx avg `-0.0022` n `6`; index avg `0.0093` n `26`; metal avg `0.0498` n `20`; unknown avg `0.1498` n `754`
- 24h: commodity avg `0.0161` n `12`; crypto_alt avg `-1.3021` n `231`; crypto_major avg `-1.4717` n `8`; equity avg `-1.1371` n `128`; fx avg `-0.0651` n `6`; index avg `-0.2288` n `26`; metal avg `-0.7634` n `20`; unknown avg `-0.3692` n `734`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2103`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
