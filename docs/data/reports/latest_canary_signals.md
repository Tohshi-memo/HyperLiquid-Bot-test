# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T12:37:38.509618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0655` n `12`; crypto_alt avg `-0.0435` n `230`; crypto_major avg `-0.0744` n `8`; equity avg `-0.2086` n `102`; fx avg `0.0048` n `6`; index avg `-0.0228` n `25`; metal avg `-0.0152` n `20`; unknown avg `0.0223` n `774`
- 1h: commodity avg `-0.0643` n `12`; crypto_alt avg `0.0806` n `230`; crypto_major avg `-0.0132` n `8`; equity avg `0.1795` n `102`; fx avg `0.0088` n `6`; index avg `0.0995` n `25`; metal avg `0.0672` n `20`; unknown avg `0.0549` n `774`
- 4h: commodity avg `0.1426` n `12`; crypto_alt avg `-0.0145` n `230`; crypto_major avg `-0.2616` n `8`; equity avg `-0.684` n `102`; fx avg `-0.0251` n `6`; index avg `-0.0323` n `25`; metal avg `-0.1391` n `20`; unknown avg `-0.1115` n `774`
- 24h: commodity avg `-0.6891` n `12`; crypto_alt avg `-3.3305` n `230`; crypto_major avg `-3.4895` n `8`; equity avg `-4.2576` n `102`; fx avg `-0.153` n `6`; index avg `-0.8064` n `25`; metal avg `-0.4803` n `20`; unknown avg `1225.3214` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
