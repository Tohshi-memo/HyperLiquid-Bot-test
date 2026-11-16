# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T14:52:29.337213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.5291` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.5205` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0201` n `13`; crypto_alt avg `-0.2698` n `239`; crypto_major avg `-0.4877` n `8`; equity avg `0.1847` n `162`; fx avg `0.0038` n `6`; index avg `0.0019` n `27`; metal avg `0.0081` n `20`; unknown avg `3.3363` n `1265`
- 1h: commodity avg `-0.136` n `13`; crypto_alt avg `1.4445` n `239`; crypto_major avg `1.5968` n `8`; equity avg `0.1823` n `162`; fx avg `0.0087` n `6`; index avg `0.0238` n `27`; metal avg `0.0763` n `20`; unknown avg `1.2242` n `1253`
- 4h: commodity avg `-0.4072` n `13`; crypto_alt avg `1.2072` n `239`; crypto_major avg `1.0627` n `8`; equity avg `-0.4664` n `162`; fx avg `0.0235` n `6`; index avg `-0.0383` n `27`; metal avg `0.0368` n `20`; unknown avg `14.0403` n `1245`
- 24h: commodity avg `-0.6853` n `13`; crypto_alt avg `0.7052` n `239`; crypto_major avg `0.8013` n `8`; equity avg `-1.2672` n `162`; fx avg `-0.0158` n `6`; index avg `-0.1145` n `27`; metal avg `0.0801` n `20`; unknown avg `243.5222` n `1048`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
