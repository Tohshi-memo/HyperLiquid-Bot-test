# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T20:22:27.502781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `13`; crypto_alt avg `-0.6134` n `239`; crypto_major avg `-0.4624` n `8`; equity avg `-0.1058` n `162`; fx avg `0.0117` n `6`; index avg `-0.0042` n `27`; metal avg `-0.0349` n `20`; unknown avg `3.0351` n `1250`
- 1h: commodity avg `0.0272` n `13`; crypto_alt avg `-1.0713` n `239`; crypto_major avg `-0.5514` n `8`; equity avg `-0.0475` n `162`; fx avg `-0.0035` n `6`; index avg `0.0084` n `27`; metal avg `-0.02` n `20`; unknown avg `0.3149` n `1236`
- 4h: commodity avg `-0.0072` n `13`; crypto_alt avg `-1.6424` n `239`; crypto_major avg `-0.9811` n `8`; equity avg `-0.1371` n `162`; fx avg `0.0105` n `6`; index avg `0.0002` n `27`; metal avg `-0.0013` n `20`; unknown avg `0.7846` n `1238`
- 24h: commodity avg `-0.0221` n `13`; crypto_alt avg `-8.3404` n `239`; crypto_major avg `-7.4343` n `8`; equity avg `-2.1105` n `162`; fx avg `-0.0247` n `6`; index avg `-0.1762` n `27`; metal avg `-0.2793` n `20`; unknown avg `1.6573` n `1082`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
