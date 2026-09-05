# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T12:37:28.129047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `12`; crypto_alt avg `0.1952` n `232`; crypto_major avg `0.24` n `8`; equity avg `0.008` n `134`; fx avg `0.0018` n `6`; index avg `0.0013` n `26`; metal avg `-0.0085` n `20`; unknown avg `0.1494` n `786`
- 1h: commodity avg `0.0218` n `12`; crypto_alt avg `0.2972` n `232`; crypto_major avg `0.3686` n `8`; equity avg `0.0041` n `134`; fx avg `0.0021` n `6`; index avg `-0.003` n `26`; metal avg `-0.011` n `20`; unknown avg `-0.0095` n `783`
- 4h: commodity avg `0.0222` n `12`; crypto_alt avg `0.5476` n `232`; crypto_major avg `0.5038` n `8`; equity avg `0.0994` n `134`; fx avg `-0.0165` n `6`; index avg `0.0336` n `26`; metal avg `-0.0088` n `20`; unknown avg `-0.0748` n `780`
- 24h: commodity avg `0.1351` n `12`; crypto_alt avg `2.8478` n `232`; crypto_major avg `1.2663` n `8`; equity avg `1.7793` n `134`; fx avg `-0.0504` n `6`; index avg `0.1828` n `26`; metal avg `0.3208` n `20`; unknown avg `17.2829` n `650`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
