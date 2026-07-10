# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T08:22:29.766351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0604` n `12`; crypto_alt avg `0.2936` n `229`; crypto_major avg `0.4488` n `8`; equity avg `0.0975` n `91`; fx avg `0.0051` n `6`; index avg `0.0211` n `25`; metal avg `-0.006` n `20`; unknown avg `0.0558` n `765`
- 1h: commodity avg `-0.0237` n `12`; crypto_alt avg `0.3154` n `229`; crypto_major avg `0.4426` n `8`; equity avg `-0.1176` n `91`; fx avg `0.0143` n `6`; index avg `-0.0067` n `25`; metal avg `-0.1013` n `20`; unknown avg `0.0911` n `765`
- 4h: commodity avg `-0.2955` n `12`; crypto_alt avg `0.1654` n `229`; crypto_major avg `0.3281` n `8`; equity avg `-0.9194` n `91`; fx avg `-0.0795` n `6`; index avg `-0.1718` n `25`; metal avg `-0.1089` n `20`; unknown avg `1.1457` n `733`
- 24h: commodity avg `-0.831` n `12`; crypto_alt avg `0.8571` n `229`; crypto_major avg `1.3073` n `8`; equity avg `-0.1145` n `91`; fx avg `-0.143` n `6`; index avg `0.1306` n `25`; metal avg `0.1515` n `20`; unknown avg `0.0347` n `732`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
