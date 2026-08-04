# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T14:37:35.998512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0799` n `12`; crypto_alt avg `0.1336` n `230`; crypto_major avg `0.2563` n `8`; equity avg `0.2795` n `107`; fx avg `0.0158` n `6`; index avg `0.042` n `25`; metal avg `-0.0146` n `20`; unknown avg `0.0298` n `782`
- 1h: commodity avg `0.0831` n `12`; crypto_alt avg `-0.4135` n `230`; crypto_major avg `-0.2881` n `8`; equity avg `0.1227` n `107`; fx avg `0.0417` n `6`; index avg `0.12` n `25`; metal avg `-0.0424` n `20`; unknown avg `-0.153` n `782`
- 4h: commodity avg `-1.2601` n `12`; crypto_alt avg `-0.1878` n `230`; crypto_major avg `0.4105` n `8`; equity avg `1.2088` n `107`; fx avg `-0.0547` n `6`; index avg `0.3562` n `25`; metal avg `0.4727` n `20`; unknown avg `-0.1221` n `781`
- 24h: commodity avg `-0.8916` n `12`; crypto_alt avg `-0.369` n `230`; crypto_major avg `0.2369` n `8`; equity avg `3.7129` n `107`; fx avg `0.1084` n `6`; index avg `0.7035` n `25`; metal avg `1.0059` n `20`; unknown avg `0.5307` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
