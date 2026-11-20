# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T12:52:32.350791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0048` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0969` n `13`; crypto_alt avg `0.0512` n `239`; crypto_major avg `0.0663` n `8`; equity avg `-0.024` n `165`; fx avg `-0.0079` n `6`; index avg `-0.0015` n `27`; metal avg `-0.0155` n `20`; unknown avg `0.184` n `1262`
- 1h: commodity avg `0.0937` n `13`; crypto_alt avg `-0.24` n `239`; crypto_major avg `-0.3641` n `8`; equity avg `-0.4189` n `165`; fx avg `0.0416` n `6`; index avg `-0.0574` n `27`; metal avg `-0.0539` n `20`; unknown avg `0.1909` n `1252`
- 4h: commodity avg `0.3216` n `13`; crypto_alt avg `-1.153` n `239`; crypto_major avg `-1.1688` n `8`; equity avg `-1.4369` n `165`; fx avg `0.0632` n `6`; index avg `-0.164` n `27`; metal avg `-0.0785` n `20`; unknown avg `30.8535` n `1240`
- 24h: commodity avg `-0.2812` n `13`; crypto_alt avg `-4.2921` n `239`; crypto_major avg `-4.0702` n `8`; equity avg `-8.5205` n `165`; fx avg `-0.0359` n `6`; index avg `-0.8632` n `27`; metal avg `-1.2773` n `20`; unknown avg `38.006` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
