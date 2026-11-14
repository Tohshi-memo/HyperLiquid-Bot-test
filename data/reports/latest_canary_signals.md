# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T13:07:28.301661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `-0.2141` n `239`; crypto_major avg `-0.3206` n `8`; equity avg `-0.1017` n `162`; fx avg `-0.0057` n `6`; index avg `-0.0047` n `27`; metal avg `-0.0079` n `20`; unknown avg `0.454` n `1256`
- 1h: commodity avg `-0.0053` n `13`; crypto_alt avg `-0.5691` n `239`; crypto_major avg `-0.6798` n `8`; equity avg `-0.1653` n `162`; fx avg `0.0021` n `6`; index avg `-0.0083` n `27`; metal avg `-0.0192` n `20`; unknown avg `0.0096` n `1258`
- 4h: commodity avg `-0.0496` n `13`; crypto_alt avg `-0.7203` n `239`; crypto_major avg `-0.4475` n `8`; equity avg `-0.1013` n `162`; fx avg `0.0055` n `6`; index avg `-0.0036` n `27`; metal avg `-0.0022` n `20`; unknown avg `90.6069` n `1194`
- 24h: commodity avg `-0.1536` n `13`; crypto_alt avg `-3.8068` n `239`; crypto_major avg `-4.1757` n `8`; equity avg `-2.9292` n `162`; fx avg `-0.1413` n `6`; index avg `-0.2557` n `27`; metal avg `-0.4313` n `20`; unknown avg `1.3287` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
