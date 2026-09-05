# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T09:07:24.328614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `0.1907` n `232`; crypto_major avg `0.0987` n `8`; equity avg `0.0245` n `134`; fx avg `0.0095` n `6`; index avg `0.0003` n `26`; metal avg `-0.0022` n `20`; unknown avg `-0.0781` n `788`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `0.3189` n `232`; crypto_major avg `0.3547` n `8`; equity avg `0.0414` n `134`; fx avg `-0.0034` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0114` n `20`; unknown avg `0.0711` n `782`
- 4h: commodity avg `-0.0138` n `12`; crypto_alt avg `1.2743` n `232`; crypto_major avg `1.2155` n `8`; equity avg `-0.0014` n `134`; fx avg `-0.0094` n `6`; index avg `-0.0083` n `26`; metal avg `0.014` n `20`; unknown avg `5.9203` n `744`
- 24h: commodity avg `0.1211` n `12`; crypto_alt avg `0.5873` n `232`; crypto_major avg `-1.2133` n `8`; equity avg `0.9047` n `134`; fx avg `-0.1264` n `6`; index avg `0.0565` n `26`; metal avg `-0.1865` n `20`; unknown avg `16.439` n `648`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
