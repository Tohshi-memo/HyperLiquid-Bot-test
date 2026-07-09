# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T19:07:28.804463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0546` n `12`; crypto_alt avg `-0.1258` n `229`; crypto_major avg `-0.1013` n `8`; equity avg `-0.1266` n `91`; fx avg `0.0009` n `6`; index avg `-0.0114` n `25`; metal avg `-0.1434` n `20`; unknown avg `-0.0235` n `765`
- 1h: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.2192` n `229`; crypto_major avg `-0.3925` n `8`; equity avg `-0.2393` n `91`; fx avg `-0.0269` n `6`; index avg `-0.0314` n `25`; metal avg `-0.2494` n `20`; unknown avg `-0.0021` n `765`
- 4h: commodity avg `-0.3132` n `12`; crypto_alt avg `0.1367` n `229`; crypto_major avg `-0.1669` n `8`; equity avg `0.0507` n `91`; fx avg `-0.0204` n `6`; index avg `0.0775` n `25`; metal avg `-0.2957` n `20`; unknown avg `-0.0847` n `765`
- 24h: commodity avg `-1.0502` n `12`; crypto_alt avg `1.2741` n `229`; crypto_major avg `0.8143` n `8`; equity avg `2.2497` n `91`; fx avg `0.052` n `6`; index avg `0.3742` n `25`; metal avg `0.5272` n `20`; unknown avg `0.9208` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
