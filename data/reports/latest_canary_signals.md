# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T06:07:31.708606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `0.0367` n `229`; crypto_major avg `0.1142` n `8`; equity avg `-0.0041` n `88`; fx avg `0.0026` n `6`; index avg `0.008` n `25`; metal avg `0.0002` n `20`; unknown avg `0.0953` n `745`
- 1h: commodity avg `0.0145` n `12`; crypto_alt avg `0.0119` n `229`; crypto_major avg `0.1226` n `8`; equity avg `0.0663` n `88`; fx avg `0.0053` n `6`; index avg `-0.0132` n `25`; metal avg `0.0018` n `20`; unknown avg `0.1706` n `745`
- 4h: commodity avg `-0.0264` n `12`; crypto_alt avg `0.4042` n `229`; crypto_major avg `0.7826` n `8`; equity avg `0.1961` n `88`; fx avg `0.0169` n `6`; index avg `0.0123` n `25`; metal avg `0.0235` n `20`; unknown avg `0.0545` n `745`
- 24h: commodity avg `-0.1416` n `12`; crypto_alt avg `2.0398` n `229`; crypto_major avg `2.6183` n `8`; equity avg `0.4038` n `88`; fx avg `-0.0813` n `6`; index avg `-0.0002` n `25`; metal avg `-0.0846` n `20`; unknown avg `4.4102` n `733`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
