# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T01:57:35.870215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0537` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.8205` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7987` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `-0.1057` n `230`; crypto_major avg `-0.0952` n `8`; equity avg `-0.4216` n `102`; fx avg `-0.0107` n `6`; index avg `-0.0644` n `25`; metal avg `-0.0718` n `20`; unknown avg `-0.1589` n `774`
- 1h: commodity avg `-0.0589` n `12`; crypto_alt avg `-0.4722` n `230`; crypto_major avg `-0.2931` n `8`; equity avg `-0.5603` n `102`; fx avg `0.0084` n `6`; index avg `-0.0705` n `25`; metal avg `-0.1691` n `20`; unknown avg `0.289` n `774`
- 4h: commodity avg `-0.106` n `12`; crypto_alt avg `-2.4368` n `230`; crypto_major avg `-2.1597` n `8`; equity avg `-1.8055` n `102`; fx avg `0.065` n `6`; index avg `-0.3392` n `25`; metal avg `-0.361` n `20`; unknown avg `2.1623` n `774`
- 24h: commodity avg `-0.795` n `12`; crypto_alt avg `-4.163` n `230`; crypto_major avg `-3.2879` n `8`; equity avg `-2.6799` n `102`; fx avg `-0.0762` n `6`; index avg `-0.6322` n `25`; metal avg `-0.4479` n `20`; unknown avg `1161.8362` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.3449`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2977`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1924`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
