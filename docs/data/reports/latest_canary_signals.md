# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T09:37:40.287279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.064` n `13`; crypto_alt avg `-0.3098` n `237`; crypto_major avg `-0.3371` n `8`; equity avg `-0.3168` n `152`; fx avg `-0.0034` n `6`; index avg `-0.0537` n `26`; metal avg `-0.0757` n `20`; unknown avg `0.9023` n `1233`
- 1h: commodity avg `0.1394` n `13`; crypto_alt avg `-0.2441` n `237`; crypto_major avg `-0.3597` n `8`; equity avg `-0.6076` n `152`; fx avg `-0.035` n `6`; index avg `-0.1027` n `26`; metal avg `-0.0062` n `20`; unknown avg `1.2891` n `1207`
- 4h: commodity avg `0.1312` n `13`; crypto_alt avg `-0.3359` n `237`; crypto_major avg `-0.1413` n `8`; equity avg `0.2575` n `152`; fx avg `-0.0784` n `6`; index avg `-0.0373` n `26`; metal avg `-0.1443` n `20`; unknown avg `0.2587` n `1134`
- 24h: commodity avg `0.326` n `13`; crypto_alt avg `0.0903` n `237`; crypto_major avg `0.2579` n `8`; equity avg `-1.011` n `152`; fx avg `-0.0931` n `6`; index avg `-0.1292` n `26`; metal avg `-0.4278` n `20`; unknown avg `49.4836` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1919`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
