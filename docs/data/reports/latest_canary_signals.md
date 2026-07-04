# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T13:52:24.969561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0` n `12`; crypto_alt avg `-0.0297` n `229`; crypto_major avg `-0.0774` n `8`; equity avg `0.0055` n `88`; fx avg `0.0079` n `6`; index avg `0.0115` n `25`; metal avg `-0.0074` n `20`; unknown avg `-0.0448` n `765`
- 1h: commodity avg `-0.0501` n `12`; crypto_alt avg `-0.1383` n `229`; crypto_major avg `-0.0225` n `8`; equity avg `-0.0329` n `88`; fx avg `0.0054` n `6`; index avg `0.0199` n `25`; metal avg `0.0076` n `20`; unknown avg `-0.0125` n `759`
- 4h: commodity avg `0.0154` n `12`; crypto_alt avg `0.6627` n `229`; crypto_major avg `0.0821` n `8`; equity avg `-0.0911` n `88`; fx avg `0.0036` n `6`; index avg `0.0114` n `25`; metal avg `0.0059` n `20`; unknown avg `-0.1065` n `759`
- 24h: commodity avg `0.0055` n `12`; crypto_alt avg `0.4662` n `229`; crypto_major avg `0.9274` n `8`; equity avg `0.2179` n `88`; fx avg `-0.0531` n `6`; index avg `-0.0679` n `25`; metal avg `0.0392` n `20`; unknown avg `2.3663` n `741`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
