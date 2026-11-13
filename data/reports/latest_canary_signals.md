# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T12:07:32.813070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0784` n `13`; crypto_alt avg `0.2388` n `239`; crypto_major avg `0.1889` n `8`; equity avg `0.2339` n `162`; fx avg `-0.0089` n `6`; index avg `0.0131` n `27`; metal avg `0.0015` n `20`; unknown avg `40.1906` n `1250`
- 1h: commodity avg `0.0382` n `13`; crypto_alt avg `0.2557` n `239`; crypto_major avg `0.3336` n `8`; equity avg `0.215` n `162`; fx avg `0.0261` n `6`; index avg `0.0127` n `27`; metal avg `0.105` n `20`; unknown avg `0.064` n `1250`
- 4h: commodity avg `0.0115` n `13`; crypto_alt avg `0.2581` n `239`; crypto_major avg `1.0488` n `8`; equity avg `0.8031` n `162`; fx avg `-0.0189` n `6`; index avg `0.0769` n `27`; metal avg `0.0602` n `20`; unknown avg `44.2338` n `1184`
- 24h: commodity avg `0.8344` n `13`; crypto_alt avg `0.1108` n `239`; crypto_major avg `-1.323` n `8`; equity avg `-0.1347` n `162`; fx avg `-0.0187` n `6`; index avg `0.0981` n `27`; metal avg `-0.2907` n `20`; unknown avg `2.8194` n `1073`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
