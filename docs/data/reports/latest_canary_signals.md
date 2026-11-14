# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T00:07:24.972676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3028` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0213` n `13`; crypto_alt avg `0.247` n `239`; crypto_major avg `0.2844` n `8`; equity avg `0.1019` n `162`; fx avg `0.002` n `6`; index avg `0.0034` n `27`; metal avg `-0.0012` n `20`; unknown avg `1.3407` n `1250`
- 1h: commodity avg `0.0117` n `13`; crypto_alt avg `0.6429` n `239`; crypto_major avg `0.552` n `8`; equity avg `0.0738` n `162`; fx avg `-0.024` n `6`; index avg `0.1141` n `27`; metal avg `0.0108` n `20`; unknown avg `1.9821` n `1250`
- 4h: commodity avg `0.046` n `13`; crypto_alt avg `-1.0133` n `239`; crypto_major avg `-1.2506` n `8`; equity avg `-0.8606` n `162`; fx avg `-0.0208` n `6`; index avg `0.0522` n `27`; metal avg `-0.0227` n `20`; unknown avg `3.999` n `1166`
- 24h: commodity avg `-0.2747` n `13`; crypto_alt avg `-1.3306` n `239`; crypto_major avg `-2.9049` n `8`; equity avg `-4.1507` n `162`; fx avg `-0.099` n `6`; index avg `-0.2322` n `27`; metal avg `-0.4082` n `20`; unknown avg `61.277` n `1035`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
