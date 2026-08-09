# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T08:07:34.134047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `0.1932` n `230`; crypto_major avg `0.1468` n `8`; equity avg `0.0034` n `112`; fx avg `0.0022` n `6`; index avg `0.0056` n `25`; metal avg `-0.019` n `20`; unknown avg `-0.0058` n `785`
- 1h: commodity avg `0.0159` n `12`; crypto_alt avg `0.0696` n `230`; crypto_major avg `0.0688` n `8`; equity avg `-0.0521` n `112`; fx avg `-0.0006` n `6`; index avg `0.0156` n `25`; metal avg `0.0141` n `20`; unknown avg `-0.0386` n `785`
- 4h: commodity avg `0.0354` n `12`; crypto_alt avg `0.1023` n `230`; crypto_major avg `0.2947` n `8`; equity avg `0.0521` n `112`; fx avg `-0.0208` n `6`; index avg `0.0079` n `25`; metal avg `0.0058` n `20`; unknown avg `0.0052` n `752`
- 24h: commodity avg `0.2394` n `12`; crypto_alt avg `1.4705` n `230`; crypto_major avg `0.6708` n `8`; equity avg `0.6363` n `112`; fx avg `-0.0176` n `6`; index avg `0.0674` n `25`; metal avg `0.031` n `20`; unknown avg `0.5118` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0423`, n `668`, weak_sample_signal
