# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T10:37:26.532691+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0364` n `13`; crypto_alt avg `-0.2149` n `235`; crypto_major avg `-0.0737` n `8`; equity avg `-0.0596` n `144`; fx avg `0.011` n `6`; index avg `-0.0089` n `26`; metal avg `-0.025` n `20`; unknown avg `1.5221` n `1079`
- 1h: commodity avg `0.0966` n `13`; crypto_alt avg `-0.0704` n `235`; crypto_major avg `0.0058` n `8`; equity avg `-0.0559` n `144`; fx avg `0.0018` n `6`; index avg `-0.0126` n `26`; metal avg `-0.0792` n `20`; unknown avg `43.9861` n `1077`
- 4h: commodity avg `0.2171` n `13`; crypto_alt avg `0.1834` n `235`; crypto_major avg `0.2066` n `8`; equity avg `-0.2196` n `144`; fx avg `0.0897` n `6`; index avg `-0.0482` n `26`; metal avg `0.0235` n `20`; unknown avg `8.4488` n `997`
- 24h: commodity avg `-0.0514` n `13`; crypto_alt avg `0.9231` n `235`; crypto_major avg `0.9036` n `8`; equity avg `0.0602` n `144`; fx avg `-0.0415` n `6`; index avg `-0.0969` n `26`; metal avg `0.2018` n `20`; unknown avg `2.3186` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.208`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1896`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
