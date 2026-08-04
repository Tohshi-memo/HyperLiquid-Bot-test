# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T16:44:03.744274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8616` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0365` n `12`; crypto_alt avg `-0.0535` n `230`; crypto_major avg `-0.1266` n `8`; equity avg `-0.1084` n `107`; fx avg `0.0161` n `6`; index avg `0.0062` n `25`; metal avg `0.0663` n `20`; unknown avg `-0.001` n `782`
- 1h: commodity avg `-0.0184` n `12`; crypto_alt avg `0.3251` n `230`; crypto_major avg `0.2056` n `8`; equity avg `0.2737` n `107`; fx avg `0.0251` n `6`; index avg `0.0541` n `25`; metal avg `0.1568` n `20`; unknown avg `-0.0141` n `782`
- 4h: commodity avg `-0.5199` n `12`; crypto_alt avg `-0.2069` n `230`; crypto_major avg `-0.2305` n `8`; equity avg `1.6311` n `107`; fx avg `0.0167` n `6`; index avg `0.3976` n `25`; metal avg `0.125` n `20`; unknown avg `-0.2079` n `781`
- 24h: commodity avg `-1.1097` n `12`; crypto_alt avg `-0.2009` n `230`; crypto_major avg `0.0945` n `8`; equity avg `4.2389` n `107`; fx avg `0.088` n `6`; index avg `0.803` n `25`; metal avg `1.1463` n `20`; unknown avg `0.406` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
