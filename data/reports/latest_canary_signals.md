# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T10:07:27.464522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.044` n `229`; crypto_major avg `0.1756` n `8`; equity avg `0.0103` n `88`; fx avg `0.0` n `6`; index avg `0.0018` n `25`; metal avg `0.0016` n `20`; unknown avg `-0.0351` n `765`
- 1h: commodity avg `-0.0354` n `12`; crypto_alt avg `-0.6593` n `229`; crypto_major avg `-0.4376` n `8`; equity avg `-0.1054` n `88`; fx avg `0.0` n `6`; index avg `-0.0102` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.0819` n `765`
- 4h: commodity avg `0.0155` n `12`; crypto_alt avg `-0.2647` n `229`; crypto_major avg `-0.0893` n `8`; equity avg `-0.0571` n `88`; fx avg `0.0119` n `6`; index avg `0.0075` n `25`; metal avg `0.0188` n `20`; unknown avg `-0.2068` n `763`
- 24h: commodity avg `-0.0079` n `12`; crypto_alt avg `-0.8924` n `229`; crypto_major avg `-0.9271` n `8`; equity avg `0.1197` n `88`; fx avg `0.0168` n `6`; index avg `0.0338` n `25`; metal avg `0.0719` n `20`; unknown avg `-1.2426` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
