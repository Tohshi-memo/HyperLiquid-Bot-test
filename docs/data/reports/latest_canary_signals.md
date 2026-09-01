# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T14:07:43.919790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `0.3684` n `232`; crypto_major avg `0.3304` n `8`; equity avg `0.1921` n `131`; fx avg `0.0024` n `6`; index avg `0.0263` n `26`; metal avg `0.0202` n `20`; unknown avg `0.2196` n `790`
- 1h: commodity avg `-0.0149` n `12`; crypto_alt avg `1.0675` n `232`; crypto_major avg `0.726` n `8`; equity avg `-0.1211` n `131`; fx avg `-0.0058` n `6`; index avg `0.0544` n `26`; metal avg `0.0727` n `20`; unknown avg `1.1047` n `790`
- 4h: commodity avg `-0.089` n `12`; crypto_alt avg `1.0247` n `232`; crypto_major avg `0.5961` n `8`; equity avg `-0.7133` n `130`; fx avg `-0.0089` n `6`; index avg `-0.0195` n `26`; metal avg `0.02` n `20`; unknown avg `0.0463` n `790`
- 24h: commodity avg `0.3533` n `12`; crypto_alt avg `1.8671` n `232`; crypto_major avg `0.9047` n `8`; equity avg `-1.1953` n `130`; fx avg `0.0717` n `6`; index avg `-0.2141` n `26`; metal avg `-0.5464` n `20`; unknown avg `0.2296` n `750`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0399`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0316`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0305`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0305`, n `668`, weak_sample_signal
