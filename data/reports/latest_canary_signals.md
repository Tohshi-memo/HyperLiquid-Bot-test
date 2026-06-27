# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T15:52:26.779008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0258` n `12`; crypto_alt avg `-0.025` n `228`; crypto_major avg `-0.1006` n `8`; equity avg `-0.0214` n `88`; fx avg `-0.0151` n `6`; index avg `0.0161` n `23`; metal avg `-0.005` n `20`; unknown avg `0.0372` n `764`
- 1h: commodity avg `-0.0452` n `12`; crypto_alt avg `0.4171` n `228`; crypto_major avg `0.3735` n `8`; equity avg `0.0183` n `88`; fx avg `-0.0044` n `6`; index avg `0.027` n `23`; metal avg `-0.0002` n `20`; unknown avg `0.0634` n `764`
- 4h: commodity avg `-0.0069` n `12`; crypto_alt avg `1.0144` n `228`; crypto_major avg `1.023` n `8`; equity avg `0.1473` n `88`; fx avg `-0.0067` n `6`; index avg `0.038` n `23`; metal avg `0.0148` n `20`; unknown avg `0.2361` n `764`
- 24h: commodity avg `0.1918` n `12`; crypto_alt avg `1.444` n `228`; crypto_major avg `1.128` n `8`; equity avg `0.5843` n `87`; fx avg `0.0448` n `6`; index avg `-0.0673` n `23`; metal avg `0.0129` n `20`; unknown avg `0.3609` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2066`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
