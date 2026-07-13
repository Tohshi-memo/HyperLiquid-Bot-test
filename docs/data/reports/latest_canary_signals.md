# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T05:52:25.627176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `-0.0156` n `230`; crypto_major avg `-0.0692` n `8`; equity avg `0.1262` n `92`; fx avg `0.0296` n `6`; index avg `0.0265` n `25`; metal avg `-0.0556` n `20`; unknown avg `-0.3006` n `766`
- 1h: commodity avg `0.0569` n `12`; crypto_alt avg `0.2307` n `230`; crypto_major avg `0.1123` n `8`; equity avg `0.2293` n `92`; fx avg `0.006` n `6`; index avg `0.0494` n `25`; metal avg `0.0274` n `20`; unknown avg `-0.2999` n `766`
- 4h: commodity avg `0.0395` n `12`; crypto_alt avg `-0.6079` n `230`; crypto_major avg `-1.0224` n `8`; equity avg `-0.6211` n `92`; fx avg `0.041` n `6`; index avg `-0.101` n `25`; metal avg `-0.2479` n `20`; unknown avg `0.096` n `766`
- 24h: commodity avg `0.1972` n `12`; crypto_alt avg `-1.6196` n `230`; crypto_major avg `-1.1359` n `8`; equity avg `-2.2153` n `92`; fx avg `0.0505` n `6`; index avg `-0.4854` n `25`; metal avg `-0.4608` n `20`; unknown avg `-0.13` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1832`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
