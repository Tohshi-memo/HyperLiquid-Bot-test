# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T20:37:33.741568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `13`; crypto_alt avg `-0.1911` n `237`; crypto_major avg `-0.0426` n `8`; equity avg `0.0379` n `151`; fx avg `0.0092` n `6`; index avg `0.0119` n `26`; metal avg `-0.002` n `20`; unknown avg `1.0585` n `1194`
- 1h: commodity avg `-0.0258` n `13`; crypto_alt avg `0.0301` n `237`; crypto_major avg `0.1412` n `8`; equity avg `-0.3899` n `151`; fx avg `0.0069` n `6`; index avg `-0.0457` n `26`; metal avg `-0.0521` n `20`; unknown avg `0.0474` n `1128`
- 4h: commodity avg `-0.1429` n `13`; crypto_alt avg `-0.3315` n `237`; crypto_major avg `-0.0098` n `8`; equity avg `-0.5055` n `151`; fx avg `0.0101` n `6`; index avg `-0.0546` n `26`; metal avg `-0.0486` n `20`; unknown avg `-0.1293` n `1128`
- 24h: commodity avg `-0.3185` n `13`; crypto_alt avg `3.196` n `237`; crypto_major avg `2.4753` n `8`; equity avg `2.8999` n `151`; fx avg `-0.0029` n `6`; index avg `0.5918` n `26`; metal avg `0.1109` n `20`; unknown avg `3.0777` n `908`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
