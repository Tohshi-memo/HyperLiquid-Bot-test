# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T10:52:27.560522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `13`; crypto_alt avg `-0.0957` n `239`; crypto_major avg `0.0029` n `8`; equity avg `0.0126` n `162`; fx avg `-0.0079` n `6`; index avg `-0.0037` n `27`; metal avg `0.0031` n `20`; unknown avg `0.3326` n `1260`
- 1h: commodity avg `0.0024` n `13`; crypto_alt avg `-0.6116` n `239`; crypto_major avg `-0.2012` n `8`; equity avg `-0.0394` n `162`; fx avg `-0.0021` n `6`; index avg `-0.0127` n `27`; metal avg `0.0055` n `20`; unknown avg `42.924` n `1244`
- 4h: commodity avg `-0.0268` n `13`; crypto_alt avg `-0.8623` n `239`; crypto_major avg `-0.1609` n `8`; equity avg `0.0465` n `162`; fx avg `0.0071` n `6`; index avg `0.003` n `27`; metal avg `0.0307` n `20`; unknown avg `43.6576` n `1168`
- 24h: commodity avg `-0.1737` n `13`; crypto_alt avg `-3.2147` n `239`; crypto_major avg `-3.23` n `8`; equity avg `-2.8218` n `162`; fx avg `-0.1133` n `6`; index avg `-0.2533` n `27`; metal avg `-0.2961` n `20`; unknown avg `1.6197` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
