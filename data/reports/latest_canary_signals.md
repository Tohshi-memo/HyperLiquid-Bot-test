# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T04:37:29.762573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0252` n `12`; crypto_alt avg `0.1654` n `229`; crypto_major avg `0.3196` n `8`; equity avg `0.0665` n `88`; fx avg `0.0037` n `6`; index avg `-0.0008` n `25`; metal avg `0.0013` n `20`; unknown avg `1.5638` n `765`
- 1h: commodity avg `-0.0372` n `12`; crypto_alt avg `-0.0497` n `229`; crypto_major avg `0.3781` n `8`; equity avg `0.0346` n `88`; fx avg `0.0094` n `6`; index avg `-0.0002` n `25`; metal avg `0.0141` n `20`; unknown avg `1.752` n `765`
- 4h: commodity avg `-0.0819` n `12`; crypto_alt avg `-0.1763` n `229`; crypto_major avg `0.3943` n `8`; equity avg `0.255` n `88`; fx avg `-0.009` n `6`; index avg `0.027` n `25`; metal avg `0.0056` n `20`; unknown avg `-0.3418` n `763`
- 24h: commodity avg `-0.0944` n `12`; crypto_alt avg `2.535` n `229`; crypto_major avg `3.4757` n `8`; equity avg `0.5487` n `88`; fx avg `-0.1405` n `6`; index avg `0.0412` n `25`; metal avg `-0.1144` n `20`; unknown avg `2.5553` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
