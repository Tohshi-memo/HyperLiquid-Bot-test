# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T16:07:31.283786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5607` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0763` n `12`; crypto_alt avg `-0.105` n `230`; crypto_major avg `-0.2134` n `8`; equity avg `0.0281` n `107`; fx avg `0.0148` n `6`; index avg `0.0034` n `25`; metal avg `0.0003` n `20`; unknown avg `0.0274` n `782`
- 1h: commodity avg `-0.2203` n `12`; crypto_alt avg `0.0465` n `230`; crypto_major avg `-0.1376` n `8`; equity avg `0.4785` n `107`; fx avg `0.013` n `6`; index avg `0.116` n `25`; metal avg `0.0303` n `20`; unknown avg `-0.0547` n `782`
- 4h: commodity avg `-0.536` n `12`; crypto_alt avg `-0.1262` n `230`; crypto_major avg `-0.0791` n `8`; equity avg `1.4816` n `107`; fx avg `0.0501` n `6`; index avg `0.3728` n `25`; metal avg `0.3097` n `20`; unknown avg `-0.3059` n `781`
- 24h: commodity avg `-1.1274` n `12`; crypto_alt avg `-0.1585` n `230`; crypto_major avg `0.2105` n `8`; equity avg `4.253` n `107`; fx avg `0.0727` n `6`; index avg `0.7925` n `25`; metal avg `1.1406` n `20`; unknown avg `0.3958` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
