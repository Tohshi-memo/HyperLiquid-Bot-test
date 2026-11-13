# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T17:07:26.973651+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0158` n `13`; crypto_alt avg `-0.1027` n `239`; crypto_major avg `0.1598` n `8`; equity avg `0.6401` n `162`; fx avg `0.002` n `6`; index avg `0.0699` n `27`; metal avg `0.0693` n `20`; unknown avg `0.215` n `1256`
- 1h: commodity avg `-0.2658` n `13`; crypto_alt avg `-0.5173` n `239`; crypto_major avg `-0.2484` n `8`; equity avg `0.7481` n `162`; fx avg `-0.0064` n `6`; index avg `0.0575` n `27`; metal avg `0.0034` n `20`; unknown avg `54.8197` n `1258`
- 4h: commodity avg `-0.2879` n `13`; crypto_alt avg `-0.5265` n `239`; crypto_major avg `-0.9053` n `8`; equity avg `-2.2338` n `162`; fx avg `-0.0626` n `6`; index avg `-0.2391` n `27`; metal avg `-0.284` n `20`; unknown avg `5.0327` n `1248`
- 24h: commodity avg `0.1122` n `13`; crypto_alt avg `0.255` n `239`; crypto_major avg `-1.5514` n `8`; equity avg `-3.064` n `162`; fx avg `-0.0183` n `6`; index avg `-0.2807` n `27`; metal avg `-0.1786` n `20`; unknown avg `8.069` n `1089`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
