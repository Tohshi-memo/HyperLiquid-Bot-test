# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T16:52:32.510656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `0.0172` n `228`; crypto_major avg `0.1126` n `8`; equity avg `0.0127` n `88`; fx avg `-0.0022` n `6`; index avg `0.0033` n `23`; metal avg `0.0076` n `20`; unknown avg `0.0662` n `764`
- 1h: commodity avg `-0.04` n `12`; crypto_alt avg `0.0402` n `228`; crypto_major avg `0.0074` n `8`; equity avg `-0.0525` n `88`; fx avg `0.0079` n `6`; index avg `-0.0392` n `23`; metal avg `-0.0017` n `20`; unknown avg `0.0524` n `764`
- 4h: commodity avg `-0.0859` n `12`; crypto_alt avg `0.924` n `228`; crypto_major avg `0.9264` n `8`; equity avg `0.0826` n `88`; fx avg `0.0001` n `6`; index avg `-0.003` n `23`; metal avg `0.012` n `20`; unknown avg `0.1308` n `764`
- 24h: commodity avg `0.1544` n `12`; crypto_alt avg `0.8842` n `228`; crypto_major avg `0.8031` n `8`; equity avg `0.4716` n `87`; fx avg `0.0745` n `6`; index avg `-0.1397` n `23`; metal avg `-0.0018` n `20`; unknown avg `0.309` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2073`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
