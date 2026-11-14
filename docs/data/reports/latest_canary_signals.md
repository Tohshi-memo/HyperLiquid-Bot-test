# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T09:07:30.898866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `13`; crypto_alt avg `0.2203` n `239`; crypto_major avg `0.2403` n `8`; equity avg `0.0276` n `162`; fx avg `-0.0143` n `6`; index avg `-0.0054` n `27`; metal avg `0.0075` n `20`; unknown avg `1.6892` n `1244`
- 1h: commodity avg `-0.0068` n `13`; crypto_alt avg `-0.0703` n `239`; crypto_major avg `-0.1185` n `8`; equity avg `-0.0223` n `162`; fx avg `-0.0017` n `6`; index avg `-0.0072` n `27`; metal avg `0.001` n `20`; unknown avg `2.6559` n `1244`
- 4h: commodity avg `0.0312` n `13`; crypto_alt avg `-0.4813` n `239`; crypto_major avg `0.0618` n `8`; equity avg `0.1348` n `162`; fx avg `-0.0037` n `6`; index avg `0.0082` n `27`; metal avg `0.0403` n `20`; unknown avg `1.0839` n `1206`
- 24h: commodity avg `-0.1703` n `13`; crypto_alt avg `-2.6919` n `239`; crypto_major avg `-2.8368` n `8`; equity avg `-2.4941` n `162`; fx avg `-0.1489` n `6`; index avg `-0.2069` n `27`; metal avg `-0.3873` n `20`; unknown avg `59.0607` n `1058`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
