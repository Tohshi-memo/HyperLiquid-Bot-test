# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T02:37:29.830669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3699` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1146` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.023` n `13`; crypto_alt avg `-0.0826` n `239`; crypto_major avg `0.0401` n `8`; equity avg `-0.1422` n `165`; fx avg `0.0178` n `6`; index avg `-0.0387` n `27`; metal avg `0.1129` n `20`; unknown avg `160.0958` n `1262`
- 1h: commodity avg `-0.0043` n `13`; crypto_alt avg `-1.2766` n `239`; crypto_major avg `-1.1323` n `8`; equity avg `-0.3916` n `165`; fx avg `0.0272` n `6`; index avg `-0.0177` n `27`; metal avg `-0.1889` n `20`; unknown avg `2.9551` n `1260`
- 4h: commodity avg `-0.0842` n `13`; crypto_alt avg `-1.9892` n `239`; crypto_major avg `-1.5181` n `8`; equity avg `-1.6882` n `165`; fx avg `0.024` n `6`; index avg `-0.1482` n `27`; metal avg `-0.7123` n `20`; unknown avg `18.6407` n `1248`
- 24h: commodity avg `-0.0789` n `13`; crypto_alt avg `-2.6722` n `239`; crypto_major avg `-1.5891` n `8`; equity avg `-5.2228` n `165`; fx avg `0.033` n `6`; index avg `-0.3723` n `27`; metal avg `-1.5767` n `20`; unknown avg `13.1153` n `1168`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
