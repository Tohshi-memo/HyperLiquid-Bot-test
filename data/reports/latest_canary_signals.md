# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T14:04:36.085686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.7342` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0721` n `12`; crypto_alt avg `0.1341` n `230`; crypto_major avg `0.0679` n `8`; equity avg `0.1519` n `121`; fx avg `0.0127` n `6`; index avg `0.0189` n `25`; metal avg `-0.0493` n `20`; unknown avg `-0.0003` n `792`
- 1h: commodity avg `0.0418` n `12`; crypto_alt avg `0.0315` n `230`; crypto_major avg `-0.0259` n `8`; equity avg `-0.3532` n `121`; fx avg `0.0105` n `6`; index avg `0.0076` n `25`; metal avg `-0.035` n `20`; unknown avg `0.0901` n `792`
- 4h: commodity avg `0.0321` n `12`; crypto_alt avg `0.5316` n `230`; crypto_major avg `0.4701` n `8`; equity avg `-1.2641` n `121`; fx avg `0.0196` n `6`; index avg `-0.1375` n `25`; metal avg `-0.0647` n `20`; unknown avg `0.4408` n `792`
- 24h: commodity avg `0.2141` n `12`; crypto_alt avg `7.4119` n `230`; crypto_major avg `11.9713` n `8`; equity avg `0.2696` n `121`; fx avg `0.1909` n `6`; index avg `-0.0185` n `25`; metal avg `0.1928` n `20`; unknown avg `2.624` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
