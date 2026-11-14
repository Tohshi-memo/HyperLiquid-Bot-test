# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T01:52:25.476586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `13`; crypto_alt avg `-0.1544` n `239`; crypto_major avg `-0.0919` n `8`; equity avg `-0.0311` n `162`; fx avg `0.0021` n `6`; index avg `0.0013` n `27`; metal avg `-0.0019` n `20`; unknown avg `1.2112` n `1260`
- 1h: commodity avg `-0.0024` n `13`; crypto_alt avg `-0.2992` n `239`; crypto_major avg `-0.2087` n `8`; equity avg `0.0198` n `162`; fx avg `0.0087` n `6`; index avg `-0.0194` n `27`; metal avg `0.0166` n `20`; unknown avg `1.4614` n `1260`
- 4h: commodity avg `0.0002` n `13`; crypto_alt avg `-0.5581` n `239`; crypto_major avg `-0.6321` n `8`; equity avg `-0.4384` n `162`; fx avg `-0.0212` n `6`; index avg `-0.0442` n `27`; metal avg `0.0213` n `20`; unknown avg `0.5838` n `1198`
- 24h: commodity avg `-0.0841` n `13`; crypto_alt avg `-1.7611` n `239`; crypto_major avg `-2.8992` n `8`; equity avg `-4.1163` n `162`; fx avg `-0.0701` n `6`; index avg `-0.3776` n `27`; metal avg `-0.6052` n `20`; unknown avg `61.6135` n `1036`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
