# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T14:07:22.911128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.4947` n `12`; crypto_alt avg `-0.1352` n `228`; crypto_major avg `-0.1687` n `8`; equity avg `-0.1295` n `66`; fx avg `-0.0066` n `5`; index avg `-0.1758` n `23`; metal avg `-0.5145` n `18`; unknown avg `2.4546` n `384`
- 1h: commodity avg `0.1876` n `12`; crypto_alt avg `-0.2409` n `228`; crypto_major avg `-0.6405` n `8`; equity avg `-0.9477` n `66`; fx avg `0.0052` n `5`; index avg `-0.4847` n `23`; metal avg `-0.1064` n `18`; unknown avg `1.8875` n `383`
- 4h: commodity avg `-0.7356` n `12`; crypto_alt avg `0.8292` n `228`; crypto_major avg `0.473` n `8`; equity avg `-0.1102` n `66`; fx avg `-0.0416` n `5`; index avg `0.0867` n `23`; metal avg `0.6302` n `18`; unknown avg `1.8874` n `383`
- 24h: commodity avg `0.2978` n `12`; crypto_alt avg `-1.9372` n `228`; crypto_major avg `-1.1614` n `8`; equity avg `-0.1139` n `65`; fx avg `0.0657` n `5`; index avg `0.0524` n `23`; metal avg `0.6513` n `18`; unknown avg `1.4064` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
