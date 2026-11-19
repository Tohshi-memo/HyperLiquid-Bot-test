# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T02:37:27.158133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0146` n `13`; crypto_alt avg `-0.1302` n `239`; crypto_major avg `-0.178` n `8`; equity avg `-0.2994` n `164`; fx avg `-0.0018` n `6`; index avg `-0.0372` n `27`; metal avg `-0.0922` n `20`; unknown avg `0.366` n `1265`
- 1h: commodity avg `-0.0356` n `13`; crypto_alt avg `0.4748` n `239`; crypto_major avg `0.2692` n `8`; equity avg `0.2675` n `164`; fx avg `-0.0105` n `6`; index avg `0.0297` n `27`; metal avg `-0.0419` n `20`; unknown avg `2.2019` n `1263`
- 4h: commodity avg `0.0827` n `13`; crypto_alt avg `0.73` n `239`; crypto_major avg `0.1597` n `8`; equity avg `0.847` n `164`; fx avg `-0.0486` n `6`; index avg `0.0839` n `27`; metal avg `0.0794` n `20`; unknown avg `2.9926` n `1257`
- 24h: commodity avg `0.0176` n `13`; crypto_alt avg `-0.3291` n `239`; crypto_major avg `-1.7697` n `8`; equity avg `-0.532` n `164`; fx avg `-0.1084` n `6`; index avg `0.0307` n `27`; metal avg `-0.6395` n `20`; unknown avg `46.7033` n `1127`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
