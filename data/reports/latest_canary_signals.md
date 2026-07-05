# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T15:52:29.736678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.0559` n `229`; crypto_major avg `0.004` n `8`; equity avg `-0.0181` n `88`; fx avg `0.0103` n `6`; index avg `0.005` n `25`; metal avg `0.0034` n `20`; unknown avg `-0.0003` n `765`
- 1h: commodity avg `-0.0085` n `12`; crypto_alt avg `0.0764` n `229`; crypto_major avg `0.1807` n `8`; equity avg `0.0308` n `88`; fx avg `-0.0041` n `6`; index avg `-0.0089` n `25`; metal avg `0.0015` n `20`; unknown avg `0.0068` n `747`
- 4h: commodity avg `-0.0193` n `12`; crypto_alt avg `0.5918` n `229`; crypto_major avg `0.8158` n `8`; equity avg `-0.0072` n `88`; fx avg `-0.077` n `6`; index avg `0.0304` n `25`; metal avg `-0.0091` n `20`; unknown avg `0.224` n `747`
- 24h: commodity avg `-0.027` n `12`; crypto_alt avg `-1.4697` n `229`; crypto_major avg `-0.7755` n `8`; equity avg `0.2133` n `88`; fx avg `-0.0865` n `6`; index avg `0.0648` n `25`; metal avg `0.0606` n `20`; unknown avg `-0.6138` n `713`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
