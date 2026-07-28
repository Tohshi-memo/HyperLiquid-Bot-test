# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T02:07:33.527621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5465` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5443` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0733` n `12`; crypto_alt avg `0.1034` n `230`; crypto_major avg `0.0283` n `8`; equity avg `-0.1229` n `102`; fx avg `0.0025` n `6`; index avg `-0.0412` n `25`; metal avg `0.0026` n `20`; unknown avg `0.0047` n `774`
- 1h: commodity avg `-0.0536` n `12`; crypto_alt avg `0.4143` n `230`; crypto_major avg `0.3521` n `8`; equity avg `-0.3758` n `102`; fx avg `-0.0038` n `6`; index avg `-0.0856` n `25`; metal avg `-0.0905` n `20`; unknown avg `-0.0312` n `774`
- 4h: commodity avg `-0.1353` n `12`; crypto_alt avg `-2.1018` n `230`; crypto_major avg `-1.9061` n `8`; equity avg `-1.7873` n `102`; fx avg `0.0631` n `6`; index avg `-0.3618` n `25`; metal avg `-0.3596` n `20`; unknown avg `2.0433` n `774`
- 24h: commodity avg `-0.8959` n `12`; crypto_alt avg `-4.0823` n `230`; crypto_major avg `-3.3271` n `8`; equity avg `-2.939` n `102`; fx avg `-0.0724` n `6`; index avg `-0.6749` n `25`; metal avg `-0.4359` n `20`; unknown avg `1161.8341` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2905`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.252`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1828`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
