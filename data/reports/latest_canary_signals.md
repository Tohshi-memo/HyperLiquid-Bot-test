# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T08:37:26.874341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.05` n `12`; crypto_alt avg `0.0615` n `230`; crypto_major avg `0.0148` n `8`; equity avg `0.0798` n `102`; fx avg `-0.0007` n `6`; index avg `0.0323` n `25`; metal avg `-0.0044` n `20`; unknown avg `0.0026` n `774`
- 1h: commodity avg `-0.2387` n `12`; crypto_alt avg `-0.1139` n `230`; crypto_major avg `-0.0297` n `8`; equity avg `0.1951` n `102`; fx avg `0.0042` n `6`; index avg `0.0154` n `25`; metal avg `0.0052` n `20`; unknown avg `0.0267` n `774`
- 4h: commodity avg `-0.3216` n `12`; crypto_alt avg `0.1052` n `230`; crypto_major avg `-0.0881` n `8`; equity avg `-0.0277` n `102`; fx avg `-0.0414` n `6`; index avg `0.0206` n `25`; metal avg `-0.0053` n `20`; unknown avg `-0.0067` n `758`
- 24h: commodity avg `-0.6377` n `12`; crypto_alt avg `-3.6301` n `230`; crypto_major avg `-3.6289` n `8`; equity avg `-4.0321` n `102`; fx avg `-0.174` n `6`; index avg `-0.843` n `25`; metal avg `-0.4306` n `20`; unknown avg `1158.5731` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
