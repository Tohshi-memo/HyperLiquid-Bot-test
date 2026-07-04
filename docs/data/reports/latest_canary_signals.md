# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T11:37:25.842729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `0.3092` n `229`; crypto_major avg `0.1269` n `8`; equity avg `-0.0005` n `88`; fx avg `0.0088` n `6`; index avg `-0.0061` n `25`; metal avg `0.0041` n `20`; unknown avg `0.0282` n `765`
- 1h: commodity avg `0.0141` n `12`; crypto_alt avg `0.5053` n `229`; crypto_major avg `0.1335` n `8`; equity avg `-0.045` n `88`; fx avg `0.0062` n `6`; index avg `-0.0037` n `25`; metal avg `0.0095` n `20`; unknown avg `0.0093` n `765`
- 4h: commodity avg `0.1052` n `12`; crypto_alt avg `0.4341` n `229`; crypto_major avg `-0.0003` n `8`; equity avg `0.0505` n `88`; fx avg `0.0029` n `6`; index avg `0.0401` n `25`; metal avg `0.0276` n `20`; unknown avg `0.1602` n `765`
- 24h: commodity avg `0.1204` n `12`; crypto_alt avg `1.0423` n `229`; crypto_major avg `1.3446` n `8`; equity avg `0.1313` n `88`; fx avg `-0.0735` n `6`; index avg `-0.0303` n `25`; metal avg `-0.0772` n `20`; unknown avg `2.8458` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
