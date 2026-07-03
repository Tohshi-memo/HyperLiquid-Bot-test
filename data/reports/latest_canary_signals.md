# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T09:37:26.831034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `12`; crypto_alt avg `-0.1228` n `229`; crypto_major avg `-0.2386` n `8`; equity avg `-0.0144` n `88`; fx avg `0.0268` n `6`; index avg `0.0037` n `25`; metal avg `-0.0554` n `20`; unknown avg `0.0482` n `755`
- 1h: commodity avg `0.0774` n `12`; crypto_alt avg `-0.059` n `229`; crypto_major avg `-0.1567` n `8`; equity avg `0.0487` n `88`; fx avg `0.0246` n `6`; index avg `-0.0185` n `25`; metal avg `-0.1267` n `20`; unknown avg `0.1313` n `755`
- 4h: commodity avg `-0.0828` n `12`; crypto_alt avg `0.2535` n `229`; crypto_major avg `-0.1297` n `8`; equity avg `0.1532` n `88`; fx avg `-0.1123` n `6`; index avg `0.0344` n `25`; metal avg `-0.0333` n `20`; unknown avg `0.1336` n `739`
- 24h: commodity avg `0.4833` n `12`; crypto_alt avg `1.4797` n `229`; crypto_major avg `2.1996` n `8`; equity avg `0.0912` n `88`; fx avg `-0.0799` n `6`; index avg `0.1867` n `25`; metal avg `1.1257` n `20`; unknown avg `5.2665` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
