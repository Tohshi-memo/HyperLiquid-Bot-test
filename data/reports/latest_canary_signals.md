# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T06:52:26.960055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `13`; crypto_alt avg `-0.2407` n `239`; crypto_major avg `0.032` n `8`; equity avg `-0.0035` n `162`; fx avg `-0.0241` n `6`; index avg `-0.0075` n `27`; metal avg `0.0032` n `20`; unknown avg `11.1147` n `1262`
- 1h: commodity avg `0.0344` n `13`; crypto_alt avg `-0.4262` n `239`; crypto_major avg `0.2513` n `8`; equity avg `0.0486` n `162`; fx avg `-0.0189` n `6`; index avg `-0.004` n `27`; metal avg `0.017` n `20`; unknown avg `11.9488` n `1234`
- 4h: commodity avg `-0.025` n `13`; crypto_alt avg `-0.6595` n `239`; crypto_major avg `-0.6667` n `8`; equity avg `0.0293` n `162`; fx avg `-0.0261` n `6`; index avg `-0.0086` n `27`; metal avg `0.0028` n `20`; unknown avg `5.0921` n `1218`
- 24h: commodity avg `-0.1849` n `13`; crypto_alt avg `-1.8771` n `239`; crypto_major avg `-2.2513` n `8`; equity avg `-2.3693` n `162`; fx avg `-0.1319` n `6`; index avg `-0.1884` n `27`; metal avg `-0.4084` n `20`; unknown avg `64.9123` n `1020`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
