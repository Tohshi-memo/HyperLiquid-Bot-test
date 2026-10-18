# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T02:37:28.165802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `13`; crypto_alt avg `-0.0499` n `237`; crypto_major avg `0.0843` n `8`; equity avg `-0.0419` n `151`; fx avg `-0.0058` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0024` n `20`; unknown avg `0.0745` n `1193`
- 1h: commodity avg `0.0857` n `13`; crypto_alt avg `-0.2601` n `237`; crypto_major avg `0.0672` n `8`; equity avg `-0.139` n `151`; fx avg `-0.0048` n `6`; index avg `-0.0161` n `26`; metal avg `-0.0012` n `20`; unknown avg `-0.0334` n `1191`
- 4h: commodity avg `0.0062` n `13`; crypto_alt avg `0.1048` n `236`; crypto_major avg `0.6295` n `8`; equity avg `0.1346` n `151`; fx avg `0.0041` n `6`; index avg `0.0461` n `26`; metal avg `0.0233` n `20`; unknown avg `0.1274` n `1185`
- 24h: commodity avg `-0.1116` n `13`; crypto_alt avg `-2.0813` n `236`; crypto_major avg `-0.2646` n `8`; equity avg `-0.8378` n `151`; fx avg `-0.0365` n `6`; index avg `-0.096` n `26`; metal avg `-0.0684` n `20`; unknown avg `4.2918` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1624`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1352`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.105`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0755`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
