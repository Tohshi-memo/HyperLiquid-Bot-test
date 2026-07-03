# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T21:52:26.231558+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0174` n `12`; crypto_alt avg `0.2355` n `229`; crypto_major avg `0.2468` n `8`; equity avg `0.0035` n `88`; fx avg `0.0249` n `6`; index avg `0.0003` n `25`; metal avg `-0.0138` n `20`; unknown avg `0.0384` n `765`
- 1h: commodity avg `0.0392` n `12`; crypto_alt avg `0.039` n `229`; crypto_major avg `-0.1187` n `8`; equity avg `0.0683` n `88`; fx avg `0.0066` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0001` n `20`; unknown avg `0.3985` n `765`
- 4h: commodity avg `-0.0615` n `12`; crypto_alt avg `0.7339` n `229`; crypto_major avg `0.9646` n `8`; equity avg `0.041` n `88`; fx avg `-0.01` n `6`; index avg `-0.0518` n `25`; metal avg `-0.0141` n `20`; unknown avg `0.3131` n `765`
- 24h: commodity avg `0.1241` n `12`; crypto_alt avg `3.4578` n `229`; crypto_major avg `3.5448` n `8`; equity avg `1.8703` n `88`; fx avg `-0.0746` n `6`; index avg `0.4596` n `25`; metal avg `0.532` n `20`; unknown avg `10.9726` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
