# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T11:22:24.900058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0199` n `13`; crypto_alt avg `0.157` n `239`; crypto_major avg `0.1301` n `8`; equity avg `0.0249` n `162`; fx avg `-0.0084` n `6`; index avg `0.0008` n `27`; metal avg `-0.0033` n `20`; unknown avg `158.6099` n `1262`
- 1h: commodity avg `-0.0203` n `13`; crypto_alt avg `-0.0643` n `239`; crypto_major avg `0.0454` n `8`; equity avg `-0.0042` n `162`; fx avg `-0.0063` n `6`; index avg `-0.0047` n `27`; metal avg `-0.0058` n `20`; unknown avg `80.7861` n `1252`
- 4h: commodity avg `-0.0549` n `13`; crypto_alt avg `-0.0117` n `239`; crypto_major avg `0.3907` n `8`; equity avg `0.1308` n `162`; fx avg `-0.0126` n `6`; index avg `0.0019` n `27`; metal avg `0.0203` n `20`; unknown avg `86.2378` n `1168`
- 24h: commodity avg `-0.1599` n `13`; crypto_alt avg `-3.2195` n `239`; crypto_major avg `-3.4648` n `8`; equity avg `-3.0919` n `162`; fx avg `-0.1313` n `6`; index avg `-0.2719` n `27`; metal avg `-0.3265` n `20`; unknown avg `2.034` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
