# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T02:52:24.240585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.25` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.6061` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0146` n `13`; crypto_alt avg `-0.0301` n `237`; crypto_major avg `-0.1217` n `8`; equity avg `-0.0782` n `151`; fx avg `-0.0047` n `6`; index avg `0.004` n `26`; metal avg `-0.0525` n `20`; unknown avg `5.6489` n `1199`
- 1h: commodity avg `-0.0013` n `13`; crypto_alt avg `-0.7498` n `237`; crypto_major avg `-0.6985` n `8`; equity avg `-0.4807` n `151`; fx avg `-0.0137` n `6`; index avg `-0.0351` n `26`; metal avg `-0.0974` n `20`; unknown avg `2.4236` n `1197`
- 4h: commodity avg `0.1231` n `13`; crypto_alt avg `-1.7733` n `237`; crypto_major avg `-1.7166` n `8`; equity avg `-1.1263` n `151`; fx avg `-0.0396` n `6`; index avg `-0.1105` n `26`; metal avg `-0.3654` n `20`; unknown avg `10.8558` n `1191`
- 24h: commodity avg `-0.6006` n `13`; crypto_alt avg `-0.5242` n `237`; crypto_major avg `-0.6971` n `8`; equity avg `-1.868` n `151`; fx avg `-0.0519` n `6`; index avg `-0.2515` n `26`; metal avg `-0.428` n `20`; unknown avg `119.8175` n `944`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
