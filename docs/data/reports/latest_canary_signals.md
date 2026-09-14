# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T02:07:30.982556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0586` n `12`; crypto_alt avg `0.5108` n `233`; crypto_major avg `0.4051` n `8`; equity avg `0.2719` n `136`; fx avg `0.0056` n `6`; index avg `0.0585` n `27`; metal avg `0.039` n `20`; unknown avg `1.8745` n `892`
- 1h: commodity avg `-0.1934` n `12`; crypto_alt avg `0.7384` n `233`; crypto_major avg `0.497` n `8`; equity avg `0.4441` n `136`; fx avg `0.0001` n `6`; index avg `0.0886` n `27`; metal avg `0.1539` n `20`; unknown avg `1.9134` n `892`
- 4h: commodity avg `-0.0346` n `12`; crypto_alt avg `0.1355` n `233`; crypto_major avg `0.0814` n `8`; equity avg `-0.2016` n `136`; fx avg `0.0139` n `6`; index avg `-0.0104` n `27`; metal avg `0.0877` n `20`; unknown avg `11.6719` n `768`
- 24h: commodity avg `0.6278` n `12`; crypto_alt avg `-1.1052` n `233`; crypto_major avg `-1.0521` n `8`; equity avg `-1.4148` n `136`; fx avg `0.0656` n `6`; index avg `-0.2977` n `26`; metal avg `-0.0361` n `20`; unknown avg `1.6365` n `682`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
