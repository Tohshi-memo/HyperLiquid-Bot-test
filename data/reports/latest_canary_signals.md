# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T00:52:30.421628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `0.2891` n `229`; crypto_major avg `0.4121` n `8`; equity avg `0.1313` n `88`; fx avg `-0.0099` n `6`; index avg `0.0303` n `25`; metal avg `0.0037` n `20`; unknown avg `0.2405` n `765`
- 1h: commodity avg `-0.013` n `12`; crypto_alt avg `-0.0906` n `229`; crypto_major avg `0.2797` n `8`; equity avg `-0.1216` n `88`; fx avg `0.0129` n `6`; index avg `0.0246` n `25`; metal avg `-0.0131` n `20`; unknown avg `-0.0809` n `765`
- 4h: commodity avg `-0.1848` n `12`; crypto_alt avg `0.5167` n `229`; crypto_major avg `1.1572` n `8`; equity avg `-0.116` n `88`; fx avg `0.1216` n `6`; index avg `0.088` n `25`; metal avg `0.0564` n `20`; unknown avg `1.9425` n `765`
- 24h: commodity avg `-0.2271` n `12`; crypto_alt avg `0.1985` n `229`; crypto_major avg `1.4214` n `8`; equity avg `0.2117` n `88`; fx avg `0.0403` n `6`; index avg `0.1673` n `25`; metal avg `0.0842` n `20`; unknown avg `1.4765` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
