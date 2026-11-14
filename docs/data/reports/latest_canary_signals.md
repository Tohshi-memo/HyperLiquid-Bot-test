# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T20:37:26.500881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2259` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0123` n `13`; crypto_alt avg `-0.444` n `239`; crypto_major avg `-0.4056` n `8`; equity avg `-0.1654` n `162`; fx avg `0.004` n `6`; index avg `-0.0108` n `27`; metal avg `-0.0769` n `20`; unknown avg `0.1885` n `1252`
- 1h: commodity avg `0.0369` n `13`; crypto_alt avg `-1.347` n `239`; crypto_major avg `-0.8272` n `8`; equity avg `-0.1813` n `162`; fx avg `-0.0042` n `6`; index avg `-0.0015` n `27`; metal avg `-0.0975` n `20`; unknown avg `4.6915` n `1234`
- 4h: commodity avg `0.0185` n `13`; crypto_alt avg `-1.9077` n `239`; crypto_major avg `-1.2222` n `8`; equity avg `-0.1819` n `162`; fx avg `0.0124` n `6`; index avg `0.0037` n `27`; metal avg `-0.1083` n `20`; unknown avg `0.9702` n `1234`
- 24h: commodity avg `-0.0187` n `13`; crypto_alt avg `-8.3722` n `239`; crypto_major avg `-7.5689` n `8`; equity avg `-2.1173` n `162`; fx avg `-0.0158` n `6`; index avg `-0.174` n `27`; metal avg `-0.3283` n `20`; unknown avg `1.9602` n `1082`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
