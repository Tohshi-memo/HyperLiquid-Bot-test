# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T09:52:31.893254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.371` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `-0.0279` n `234`; crypto_major avg `-0.1298` n `8`; equity avg `-0.0153` n `141`; fx avg `-0.018` n `6`; index avg `-0.0142` n `26`; metal avg `-0.0106` n `20`; unknown avg `2.1472` n `945`
- 1h: commodity avg `-0.0986` n `12`; crypto_alt avg `-0.6713` n `234`; crypto_major avg `-0.6314` n `8`; equity avg `-0.0081` n `141`; fx avg `-0.0223` n `6`; index avg `-0.0168` n `26`; metal avg `-0.077` n `20`; unknown avg `0.1807` n `943`
- 4h: commodity avg `0.267` n `12`; crypto_alt avg `-1.6186` n `234`; crypto_major avg `-1.5352` n `8`; equity avg `-1.1048` n `141`; fx avg `0.0297` n `6`; index avg `-0.1642` n `26`; metal avg `-0.2021` n `20`; unknown avg `3.3241` n `921`
- 24h: commodity avg `0.6968` n `12`; crypto_alt avg `-5.1743` n `234`; crypto_major avg `-4.1036` n `8`; equity avg `-2.7888` n `140`; fx avg `0.0297` n `6`; index avg `-0.51` n `26`; metal avg `-0.513` n `20`; unknown avg `587.6624` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
