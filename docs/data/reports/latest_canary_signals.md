# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T17:53:03.128139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.09` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `-0.0159` n `230`; crypto_major avg `-0.0064` n `8`; equity avg `-0.258` n `102`; fx avg `-0.0157` n `6`; index avg `-0.0469` n `25`; metal avg `-0.0497` n `20`; unknown avg `-0.1499` n `774`
- 1h: commodity avg `0.2022` n `12`; crypto_alt avg `-0.7862` n `230`; crypto_major avg `-0.9633` n `8`; equity avg `-0.7245` n `102`; fx avg `-0.0356` n `6`; index avg `-0.1281` n `25`; metal avg `-0.0904` n `20`; unknown avg `0.3533` n `774`
- 4h: commodity avg `-0.505` n `12`; crypto_alt avg `0.391` n `230`; crypto_major avg `0.7989` n `8`; equity avg `1.147` n `102`; fx avg `-0.0643` n `6`; index avg `0.1226` n `25`; metal avg `0.1458` n `20`; unknown avg `-0.1013` n `774`
- 24h: commodity avg `-0.9378` n `12`; crypto_alt avg `-2.2992` n `230`; crypto_major avg `-2.2272` n `8`; equity avg `-2.8581` n `102`; fx avg `-0.0896` n `6`; index avg `-0.2512` n `25`; metal avg `-0.3985` n `20`; unknown avg `-0.5125` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
