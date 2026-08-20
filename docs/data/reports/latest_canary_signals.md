# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T19:07:50.404690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0743` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0231` n `12`; crypto_alt avg `-0.0434` n `230`; crypto_major avg `-0.2572` n `8`; equity avg `0.1256` n `121`; fx avg `-0.0047` n `6`; index avg `0.0325` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.0152` n `792`
- 1h: commodity avg `0.1635` n `12`; crypto_alt avg `-0.3526` n `230`; crypto_major avg `-1.0538` n `8`; equity avg `0.1724` n `121`; fx avg `0.0083` n `6`; index avg `0.0205` n `25`; metal avg `0.0134` n `20`; unknown avg `-0.072` n `792`
- 4h: commodity avg `0.1538` n `12`; crypto_alt avg `0.055` n `230`; crypto_major avg `0.3324` n `8`; equity avg `-0.4407` n `121`; fx avg `0.0473` n `6`; index avg `-0.1024` n `25`; metal avg `-0.0419` n `20`; unknown avg `1.1448` n `792`
- 24h: commodity avg `0.4132` n `12`; crypto_alt avg `5.7182` n `230`; crypto_major avg `8.7185` n `8`; equity avg `-0.3285` n `121`; fx avg `0.196` n `6`; index avg `-0.0424` n `25`; metal avg `0.1745` n `20`; unknown avg `3.6568` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2238`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
