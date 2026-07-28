# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T13:22:35.178484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0149` n `12`; crypto_alt avg `-0.201` n `230`; crypto_major avg `-0.1695` n `8`; equity avg `-0.0822` n `102`; fx avg `0.0075` n `6`; index avg `0.0128` n `25`; metal avg `-0.0047` n `20`; unknown avg `-0.025` n `774`
- 1h: commodity avg `-0.0498` n `12`; crypto_alt avg `-0.1031` n `230`; crypto_major avg `0.0045` n `8`; equity avg `-0.1114` n `102`; fx avg `0.0173` n `6`; index avg `0.0075` n `25`; metal avg `0.0248` n `20`; unknown avg `0.1318` n `774`
- 4h: commodity avg `0.0681` n `12`; crypto_alt avg `-0.0898` n `230`; crypto_major avg `-0.2771` n `8`; equity avg `-0.614` n `102`; fx avg `-0.0133` n `6`; index avg `0.0143` n `25`; metal avg `-0.0736` n `20`; unknown avg `0.0292` n `774`
- 24h: commodity avg `-0.7854` n `12`; crypto_alt avg `-3.3979` n `230`; crypto_major avg `-3.5037` n `8`; equity avg `-4.1309` n `102`; fx avg `-0.1477` n `6`; index avg `-0.7789` n `25`; metal avg `-0.4485` n `20`; unknown avg `1225.265` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
