# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T04:07:30.619341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0295` n `13`; crypto_alt avg `-0.026` n `237`; crypto_major avg `-0.0166` n `8`; equity avg `-0.0199` n `151`; fx avg `-0.0162` n `6`; index avg `0.0037` n `26`; metal avg `0.0089` n `20`; unknown avg `1.9535` n `1186`
- 1h: commodity avg `-0.0622` n `13`; crypto_alt avg `-0.2426` n `237`; crypto_major avg `-0.1185` n `8`; equity avg `0.1453` n `151`; fx avg `0.0055` n `6`; index avg `0.0424` n `26`; metal avg `0.0308` n `20`; unknown avg `1.9085` n `1186`
- 4h: commodity avg `-0.0229` n `13`; crypto_alt avg `0.2092` n `237`; crypto_major avg `0.4298` n `8`; equity avg `0.9589` n `151`; fx avg `-0.0289` n `6`; index avg `0.1379` n `26`; metal avg `0.0773` n `20`; unknown avg `0.3145` n `1130`
- 24h: commodity avg `-0.4701` n `13`; crypto_alt avg `-0.5219` n `237`; crypto_major avg `0.4563` n `8`; equity avg `2.7161` n `151`; fx avg `-0.0052` n `6`; index avg `0.521` n `26`; metal avg `0.323` n `20`; unknown avg `4.1785` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1972`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1441`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1188`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.078`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0707`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0634`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
