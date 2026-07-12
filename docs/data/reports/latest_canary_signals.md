# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T16:37:23.649683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0374` n `12`; crypto_alt avg `-0.0992` n `230`; crypto_major avg `-0.0623` n `8`; equity avg `0.0367` n `92`; fx avg `0.0062` n `6`; index avg `-0.002` n `25`; metal avg `-0.0026` n `20`; unknown avg `-0.026` n `759`
- 1h: commodity avg `0.0825` n `12`; crypto_alt avg `-0.1035` n `230`; crypto_major avg `0.0372` n `8`; equity avg `-0.0259` n `92`; fx avg `-0.0001` n `6`; index avg `0.0199` n `25`; metal avg `-0.0163` n `20`; unknown avg `-0.0225` n `759`
- 4h: commodity avg `0.1082` n `12`; crypto_alt avg `0.0177` n `230`; crypto_major avg `0.4236` n `8`; equity avg `-0.011` n `92`; fx avg `0.0041` n `6`; index avg `0.0529` n `25`; metal avg `-0.0224` n `20`; unknown avg `-0.0332` n `759`
- 24h: commodity avg `0.5425` n `12`; crypto_alt avg `-1.0572` n `230`; crypto_major avg `-0.2937` n `8`; equity avg `-0.0673` n `92`; fx avg `0.0365` n `6`; index avg `-0.0822` n `25`; metal avg `-0.1084` n `20`; unknown avg `0.4479` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
