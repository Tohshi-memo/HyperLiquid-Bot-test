# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T11:52:31.774780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0109` n `13`; crypto_alt avg `0.1986` n `239`; crypto_major avg `0.2353` n `8`; equity avg `0.0335` n `162`; fx avg `0.002` n `6`; index avg `0.0039` n `27`; metal avg `0.0063` n `20`; unknown avg `5.0058` n `1262`
- 1h: commodity avg `-0.0197` n `13`; crypto_alt avg `0.2251` n `239`; crypto_major avg `0.0174` n `8`; equity avg `-0.009` n `162`; fx avg `0.0084` n `6`; index avg `0.0021` n `27`; metal avg `-0.0053` n `20`; unknown avg `4.3231` n `1256`
- 4h: commodity avg `-0.0678` n `13`; crypto_alt avg `-0.0497` n `239`; crypto_major avg `0.4026` n `8`; equity avg `0.1084` n `162`; fx avg `0.0052` n `6`; index avg `0.0067` n `27`; metal avg `0.0251` n `20`; unknown avg `90.5078` n `1168`
- 24h: commodity avg `-0.1438` n `13`; crypto_alt avg `-3.1138` n `239`; crypto_major avg `-3.4489` n `8`; equity avg `-3.0533` n `162`; fx avg `-0.1431` n `6`; index avg `-0.2732` n `27`; metal avg `-0.4004` n `20`; unknown avg `6.0658` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
