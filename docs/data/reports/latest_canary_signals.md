# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T08:37:32.066827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2474` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0838` n `12`; crypto_alt avg `0.0767` n `234`; crypto_major avg `-0.0844` n `8`; equity avg `-0.0362` n `140`; fx avg `0.0153` n `6`; index avg `-0.0087` n `26`; metal avg `-0.0299` n `20`; unknown avg `13.363` n `945`
- 1h: commodity avg `0.1624` n `12`; crypto_alt avg `0.2588` n `234`; crypto_major avg `-0.1384` n `8`; equity avg `0.018` n `140`; fx avg `-0.0038` n `6`; index avg `-0.0206` n `26`; metal avg `-0.0087` n `20`; unknown avg `13.1421` n `937`
- 4h: commodity avg `0.2857` n `12`; crypto_alt avg `-0.0864` n `234`; crypto_major avg `-1.2742` n `8`; equity avg `-0.1733` n `140`; fx avg `0.1703` n `6`; index avg `-0.0268` n `26`; metal avg `-0.2934` n `20`; unknown avg `14.1331` n `921`
- 24h: commodity avg `0.2071` n `12`; crypto_alt avg `3.5345` n `234`; crypto_major avg `1.4301` n `8`; equity avg `1.7231` n `140`; fx avg `0.0079` n `6`; index avg `0.2005` n `26`; metal avg `0.1224` n `20`; unknown avg `15.5247` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
