# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T23:26:45.888473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `-0.1326` n `229`; crypto_major avg `-0.2054` n `8`; equity avg `-0.0511` n `88`; fx avg `0.0046` n `6`; index avg `0.0037` n `25`; metal avg `0.009` n `20`; unknown avg `0.2161` n `765`
- 1h: commodity avg `0.0288` n `12`; crypto_alt avg `-0.2572` n `229`; crypto_major avg `-0.2487` n `8`; equity avg `-0.0102` n `88`; fx avg `0.0148` n `6`; index avg `0.0117` n `25`; metal avg `0.0074` n `20`; unknown avg `-0.2426` n `765`
- 4h: commodity avg `0.0454` n `12`; crypto_alt avg `-0.699` n `229`; crypto_major avg `-0.5602` n `8`; equity avg `0.0242` n `88`; fx avg `-0.0132` n `6`; index avg `0.0377` n `25`; metal avg `0.0219` n `20`; unknown avg `9.024` n `765`
- 24h: commodity avg `0.0436` n `12`; crypto_alt avg `-0.07` n `229`; crypto_major avg `0.347` n `8`; equity avg `0.2474` n `88`; fx avg `-0.0098` n `6`; index avg `0.0093` n `25`; metal avg `0.076` n `20`; unknown avg `-0.708` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
