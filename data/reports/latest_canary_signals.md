# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T11:07:23.033898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `13`; crypto_alt avg `-0.0467` n `238`; crypto_major avg `-0.0205` n `8`; equity avg `-0.0107` n `156`; fx avg `-0.0032` n `6`; index avg `-0.0007` n `27`; metal avg `-0.005` n `20`; unknown avg `0.0907` n `1244`
- 1h: commodity avg `0.0486` n `13`; crypto_alt avg `0.038` n `238`; crypto_major avg `0.1463` n `8`; equity avg `-0.0353` n `156`; fx avg `0.0073` n `6`; index avg `-0.0088` n `27`; metal avg `0.0044` n `20`; unknown avg `0.0977` n `1238`
- 4h: commodity avg `0.0214` n `13`; crypto_alt avg `-0.2554` n `238`; crypto_major avg `-0.0997` n `8`; equity avg `-0.0932` n `156`; fx avg `0.0079` n `6`; index avg `-0.0106` n `27`; metal avg `0.0054` n `20`; unknown avg `0.7994` n `1222`
- 24h: commodity avg `-0.2654` n `13`; crypto_alt avg `-0.0763` n `238`; crypto_major avg `-1.1728` n `8`; equity avg `-1.4325` n `156`; fx avg `-0.0605` n `6`; index avg `-0.145` n `27`; metal avg `-0.4055` n `20`; unknown avg `5.1405` n `1043`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
