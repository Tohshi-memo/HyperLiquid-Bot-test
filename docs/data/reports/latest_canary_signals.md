# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T23:51:04.580811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8795` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8313` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5355` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `-0.1344` n `230`; crypto_major avg `-0.1492` n `8`; equity avg `-0.1066` n `102`; fx avg `-0.0036` n `6`; index avg `-0.0372` n `25`; metal avg `-0.0131` n `20`; unknown avg `0.0223` n `774`
- 1h: commodity avg `0.0291` n `12`; crypto_alt avg `-0.4277` n `230`; crypto_major avg `-0.3787` n `8`; equity avg `-0.1853` n `102`; fx avg `0.005` n `6`; index avg `-0.0424` n `25`; metal avg `-0.0148` n `20`; unknown avg `-0.0272` n `774`
- 4h: commodity avg `0.0388` n `12`; crypto_alt avg `-1.9774` n `230`; crypto_major avg `-1.9349` n `8`; equity avg `-0.3994` n `102`; fx avg `-0.0105` n `6`; index avg `-0.0554` n `25`; metal avg `-0.1036` n `20`; unknown avg `1.2738` n `774`
- 24h: commodity avg `-0.6353` n `12`; crypto_alt avg `-3.8679` n `230`; crypto_major avg `-3.2292` n `8`; equity avg `-2.233` n `102`; fx avg `-0.017` n `6`; index avg `-0.6065` n `25`; metal avg `-0.0798` n `20`; unknown avg `1161.746` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.3623`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.3097`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1935`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
