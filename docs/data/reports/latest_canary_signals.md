# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T20:07:30.316612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `0.0022` n `229`; crypto_major avg `0.036` n `8`; equity avg `0.0273` n `88`; fx avg `-0.0011` n `6`; index avg `0.0004` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.099` n `765`
- 1h: commodity avg `0.0107` n `12`; crypto_alt avg `-0.063` n `229`; crypto_major avg `-0.1164` n `8`; equity avg `0.0905` n `88`; fx avg `-0.0471` n `6`; index avg `0.0202` n `25`; metal avg `0.0208` n `20`; unknown avg `-0.3929` n `765`
- 4h: commodity avg `-0.0337` n `12`; crypto_alt avg `-0.208` n `229`; crypto_major avg `-0.031` n `8`; equity avg `0.0167` n `88`; fx avg `-0.0576` n `6`; index avg `-0.0073` n `25`; metal avg `0.0175` n `20`; unknown avg `-0.675` n `765`
- 24h: commodity avg `0.0088` n `12`; crypto_alt avg `0.7464` n `229`; crypto_major avg `0.9069` n `8`; equity avg `0.3052` n `88`; fx avg `-0.0585` n `6`; index avg `-0.0347` n `25`; metal avg `0.0832` n `20`; unknown avg `0.5256` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
