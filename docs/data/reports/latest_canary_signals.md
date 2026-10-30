# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T22:52:32.163144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `13`; crypto_alt avg `0.0151` n `238`; crypto_major avg `0.0457` n `8`; equity avg `-0.0062` n `156`; fx avg `-0.0149` n `6`; index avg `0.0025` n `27`; metal avg `0.0048` n `20`; unknown avg `0.2224` n `1261`
- 1h: commodity avg `-0.0133` n `13`; crypto_alt avg `0.6031` n `238`; crypto_major avg `0.2913` n `8`; equity avg `0.1055` n `156`; fx avg `0.0022` n `6`; index avg `0.0126` n `27`; metal avg `0.0237` n `20`; unknown avg `199.3887` n `1255`
- 4h: commodity avg `-0.3083` n `13`; crypto_alt avg `2.0012` n `238`; crypto_major avg `0.9928` n `8`; equity avg `1.5979` n `156`; fx avg `-0.0337` n `6`; index avg `0.1882` n `27`; metal avg `0.1528` n `20`; unknown avg `1.2503` n `1149`
- 24h: commodity avg `0.0911` n `13`; crypto_alt avg `1.3434` n `238`; crypto_major avg `-0.935` n `8`; equity avg `-2.6453` n `156`; fx avg `-0.1585` n `6`; index avg `-0.2277` n `27`; metal avg `-0.9445` n `20`; unknown avg `5.7048` n `1016`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
