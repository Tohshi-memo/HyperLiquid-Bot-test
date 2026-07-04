# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T12:37:30.442101+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `12`; crypto_alt avg `-0.0088` n `229`; crypto_major avg `0.0413` n `8`; equity avg `0.0134` n `88`; fx avg `-0.0025` n `6`; index avg `0.0217` n `25`; metal avg `-0.009` n `20`; unknown avg `-0.0342` n `765`
- 1h: commodity avg `0.0193` n `12`; crypto_alt avg `0.1913` n `229`; crypto_major avg `0.0846` n `8`; equity avg `-0.0487` n `88`; fx avg `0.001` n `6`; index avg `0.0166` n `25`; metal avg `-0.0198` n `20`; unknown avg `-0.0653` n `765`
- 4h: commodity avg `0.1313` n `12`; crypto_alt avg `0.4461` n `229`; crypto_major avg `-0.2225` n `8`; equity avg `-0.0864` n `88`; fx avg `0.0009` n `6`; index avg `0.0251` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.2844` n `765`
- 24h: commodity avg `0.1935` n `12`; crypto_alt avg `1.1297` n `229`; crypto_major avg `1.6174` n `8`; equity avg `0.1417` n `88`; fx avg `-0.0604` n `6`; index avg `-0.0151` n `25`; metal avg `-0.0052` n `20`; unknown avg `2.9499` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
