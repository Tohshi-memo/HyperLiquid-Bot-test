# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T21:07:34.785303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0605` n `13`; crypto_alt avg `-0.3349` n `239`; crypto_major avg `-0.4592` n `8`; equity avg `-0.6006` n `162`; fx avg `0.008` n `6`; index avg `-0.0647` n `27`; metal avg `-0.0425` n `20`; unknown avg `3.3794` n `1224`
- 1h: commodity avg `0.0677` n `13`; crypto_alt avg `-0.7968` n `239`; crypto_major avg `-0.607` n `8`; equity avg `-0.363` n `162`; fx avg `0.0117` n `6`; index avg `-0.0348` n `27`; metal avg `-0.0349` n `20`; unknown avg `10.669` n `1226`
- 4h: commodity avg `0.1659` n `13`; crypto_alt avg `-0.0538` n `239`; crypto_major avg `0.0946` n `8`; equity avg `0.1146` n `162`; fx avg `-0.034` n `6`; index avg `0.0433` n `27`; metal avg `-0.1375` n `20`; unknown avg `2.8713` n `1214`
- 24h: commodity avg `-0.3038` n `13`; crypto_alt avg `-0.6314` n `239`; crypto_major avg `-1.7643` n `8`; equity avg `-2.6889` n `162`; fx avg `-0.0708` n `6`; index avg `-0.2215` n `27`; metal avg `-0.2777` n `20`; unknown avg `3.0415` n `1069`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
