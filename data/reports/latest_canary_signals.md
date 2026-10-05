# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T09:52:30.803554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0261` n `13`; crypto_alt avg `0.0856` n `235`; crypto_major avg `0.0505` n `8`; equity avg `-0.0322` n `144`; fx avg `-0.0223` n `6`; index avg `0.0019` n `26`; metal avg `-0.0188` n `20`; unknown avg `1.7536` n `1079`
- 1h: commodity avg `-0.0065` n `13`; crypto_alt avg `-0.077` n `235`; crypto_major avg `-0.2031` n `8`; equity avg `-0.1352` n `144`; fx avg `-0.0163` n `6`; index avg `-0.0328` n `26`; metal avg `-0.0561` n `20`; unknown avg `0.7932` n `1077`
- 4h: commodity avg `0.2078` n `13`; crypto_alt avg `0.5382` n `235`; crypto_major avg `0.5649` n `8`; equity avg `-0.1338` n `144`; fx avg `0.0075` n `6`; index avg `-0.0257` n `26`; metal avg `0.1961` n `20`; unknown avg `-0.3343` n `981`
- 24h: commodity avg `-0.1313` n `13`; crypto_alt avg `0.8657` n `235`; crypto_major avg `0.9133` n `8`; equity avg `0.0903` n `144`; fx avg `-0.0483` n `6`; index avg `-0.0818` n `26`; metal avg `0.2607` n `20`; unknown avg `-0.1389` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2082`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1898`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
