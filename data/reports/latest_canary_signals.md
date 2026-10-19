# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T10:07:30.185342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0322` n `13`; crypto_alt avg `-0.08` n `237`; crypto_major avg `-0.1418` n `8`; equity avg `0.0361` n `151`; fx avg `0.0075` n `6`; index avg `0.0079` n `26`; metal avg `0.0004` n `20`; unknown avg `0.4791` n `1193`
- 1h: commodity avg `0.1399` n `13`; crypto_alt avg `-0.0306` n `237`; crypto_major avg `0.0364` n `8`; equity avg `0.2188` n `151`; fx avg `-0.0099` n `6`; index avg `0.0197` n `26`; metal avg `0.0209` n `20`; unknown avg `0.842` n `1193`
- 4h: commodity avg `0.343` n `13`; crypto_alt avg `-0.1611` n `237`; crypto_major avg `-0.0322` n `8`; equity avg `-0.156` n `151`; fx avg `-0.0153` n `6`; index avg `-0.0514` n `26`; metal avg `-0.0986` n `20`; unknown avg `0.9771` n `1146`
- 24h: commodity avg `-0.2136` n `13`; crypto_alt avg `-0.0328` n `237`; crypto_major avg `0.7567` n `8`; equity avg `2.4853` n `151`; fx avg `-0.0429` n `6`; index avg `0.4336` n `26`; metal avg `0.2311` n `20`; unknown avg `1.9971` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1986`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1453`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1292`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0619`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
