# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T12:22:34.097623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0582` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.0262` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0975` n `12`; crypto_alt avg `0.6453` n `229`; crypto_major avg `0.4764` n `8`; equity avg `0.0175` n `88`; fx avg `0.0019` n `6`; index avg `-0.0037` n `25`; metal avg `-0.1093` n `20`; unknown avg `0.1166` n `765`
- 1h: commodity avg `0.0094` n `12`; crypto_alt avg `-1.1227` n `229`; crypto_major avg `-1.0386` n `8`; equity avg `-0.0703` n `88`; fx avg `0.0056` n `6`; index avg `0.0196` n `25`; metal avg `-0.1252` n `20`; unknown avg `-0.0325` n `765`
- 4h: commodity avg `0.1097` n `12`; crypto_alt avg `-0.8657` n `229`; crypto_major avg `-1.015` n `8`; equity avg `-0.1289` n `88`; fx avg `0.0063` n `6`; index avg `0.0112` n `25`; metal avg `-0.1413` n `20`; unknown avg `-0.0565` n `765`
- 24h: commodity avg `-0.1364` n `12`; crypto_alt avg `-0.7252` n `229`; crypto_major avg `-0.2961` n `8`; equity avg `-0.797` n `88`; fx avg `0.0837` n `6`; index avg `-0.0025` n `25`; metal avg `-0.2729` n `20`; unknown avg `0.7584` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
