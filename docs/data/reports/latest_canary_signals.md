# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T22:37:27.832562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `0.3839` n `239`; crypto_major avg `0.2239` n `8`; equity avg `0.2889` n `168`; fx avg `0.0016` n `6`; index avg `0.0173` n `27`; metal avg `0.0165` n `20`; unknown avg `158.0129` n `1265`
- 1h: commodity avg `-0.0297` n `13`; crypto_alt avg `0.4199` n `239`; crypto_major avg `0.3038` n `8`; equity avg `0.5587` n `168`; fx avg `-0.0013` n `6`; index avg `0.0205` n `27`; metal avg `0.0546` n `20`; unknown avg `26.4219` n `1253`
- 4h: commodity avg `-0.162` n `13`; crypto_alt avg `-0.3399` n `239`; crypto_major avg `-0.0392` n `8`; equity avg `0.2452` n `168`; fx avg `-0.0551` n `6`; index avg `-0.0167` n `27`; metal avg `0.0073` n `20`; unknown avg `390.1313` n `1219`
- 24h: commodity avg `0.5761` n `13`; crypto_alt avg `-1.868` n `239`; crypto_major avg `-1.8639` n `8`; equity avg `-3.9069` n `167`; fx avg `0.2068` n `6`; index avg `-0.2998` n `27`; metal avg `-1.0422` n `20`; unknown avg `426.5194` n `1111`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
