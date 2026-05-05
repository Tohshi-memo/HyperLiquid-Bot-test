# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T19:00:35.939196+00:00`
- Correlation status: `ready`
- Asset price records: `384`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0094` n `7`; crypto_alt avg `0.0261` n `223`; crypto_major avg `0.0238` n `7`; equity avg `0.1071` n `47`; fx avg `-0.0071` n `4`; index avg `0.0071` n `6`; metal avg `-0.0689` n `7`; unknown avg `1.0896` n `313`
- 1h: commodity avg `0.0235` n `7`; crypto_alt avg `0.216` n `223`; crypto_major avg `0.1621` n `7`; equity avg `0.111` n `47`; fx avg `-0.0364` n `4`; index avg `0.0359` n `6`; metal avg `-0.0685` n `7`; unknown avg `1.05` n `313`
- 4h: commodity avg `-0.2531` n `7`; crypto_alt avg `0.0598` n `223`; crypto_major avg `0.2931` n `7`; equity avg `0.1681` n `47`; fx avg `-0.1541` n `4`; index avg `0.4371` n `6`; metal avg `-0.5804` n `7`; unknown avg `1.0107` n `313`
- 24h: commodity avg `-1.3455` n `7`; crypto_alt avg `1.2952` n `223`; crypto_major avg `2.0241` n `7`; equity avg `1.7288` n `47`; fx avg `-0.0282` n `4`; index avg `1.4802` n `6`; metal avg `0.8317` n `7`; unknown avg `1.8835` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2069`, n `380`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2002`, n `380`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1316`, n `380`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1276`, n `380`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.114`, n `376`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1083`, n `380`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1063`, n `376`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.105`, n `380`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `380`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `380`, weak_sample_signal
