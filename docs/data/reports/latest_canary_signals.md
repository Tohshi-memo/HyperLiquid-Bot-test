# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T17:37:23.203620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `0.088` n `229`; crypto_major avg `0.1978` n `8`; equity avg `0.0089` n `88`; fx avg `0.0` n `6`; index avg `0.014` n `25`; metal avg `0.0052` n `20`; unknown avg `0.2102` n `765`
- 1h: commodity avg `-0.0081` n `12`; crypto_alt avg `0.0993` n `229`; crypto_major avg `0.1304` n `8`; equity avg `-0.0095` n `88`; fx avg `0.0022` n `6`; index avg `-0.0258` n `25`; metal avg `0.0038` n `20`; unknown avg `0.22` n `765`
- 4h: commodity avg `-0.0157` n `12`; crypto_alt avg `1.0539` n `229`; crypto_major avg `0.9908` n `8`; equity avg `0.0586` n `88`; fx avg `0.0213` n `6`; index avg `-0.0203` n `25`; metal avg `0.013` n `20`; unknown avg `0.5731` n `765`
- 24h: commodity avg `-0.0237` n `12`; crypto_alt avg `1.3711` n `229`; crypto_major avg `1.7508` n `8`; equity avg `0.1969` n `88`; fx avg `-0.0066` n `6`; index avg `-0.0933` n `25`; metal avg `0.0303` n `20`; unknown avg `2.0155` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
