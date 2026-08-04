# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T18:19:47.089953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `0.0976` n `230`; crypto_major avg `0.1671` n `8`; equity avg `0.1067` n `107`; fx avg `0.0034` n `6`; index avg `0.0134` n `25`; metal avg `-0.0025` n `20`; unknown avg `-0.04` n `782`
- 1h: commodity avg `-0.038` n `12`; crypto_alt avg `0.2053` n `230`; crypto_major avg `0.2522` n `8`; equity avg `0.2918` n `107`; fx avg `0.0112` n `6`; index avg `0.0849` n `25`; metal avg `-0.0725` n `20`; unknown avg `-0.123` n `782`
- 4h: commodity avg `-0.1088` n `12`; crypto_alt avg `0.7509` n `230`; crypto_major avg `0.8134` n `8`; equity avg `1.7121` n `107`; fx avg `0.0384` n `6`; index avg `0.3422` n `25`; metal avg `0.1942` n `20`; unknown avg `-0.0523` n `782`
- 24h: commodity avg `-1.1563` n `12`; crypto_alt avg `-0.2335` n `230`; crypto_major avg `0.4019` n `8`; equity avg `3.9558` n `107`; fx avg `0.1192` n `6`; index avg `0.8217` n `25`; metal avg `1.1216` n `20`; unknown avg `0.4457` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
