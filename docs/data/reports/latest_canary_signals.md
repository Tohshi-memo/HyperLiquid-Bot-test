# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T19:37:27.720160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0161` n `12`; crypto_alt avg `0.0019` n `229`; crypto_major avg `-0.0402` n `8`; equity avg `-0.0607` n `88`; fx avg `-0.0011` n `6`; index avg `-0.0032` n `25`; metal avg `0.0052` n `20`; unknown avg `0.1227` n `765`
- 1h: commodity avg `0.0014` n `12`; crypto_alt avg `0.2371` n `229`; crypto_major avg `0.3479` n `8`; equity avg `0.0653` n `88`; fx avg `0.0023` n `6`; index avg `-0.0091` n `25`; metal avg `-0.0036` n `20`; unknown avg `0.0994` n `765`
- 4h: commodity avg `0.0162` n `12`; crypto_alt avg `0.3641` n `229`; crypto_major avg `0.6616` n `8`; equity avg `0.1424` n `88`; fx avg `-0.0119` n `6`; index avg `0.021` n `25`; metal avg `-0.009` n `20`; unknown avg `2.1077` n `765`
- 24h: commodity avg `0.1804` n `12`; crypto_alt avg `3.0315` n `229`; crypto_major avg `2.8169` n `8`; equity avg `2.3273` n `88`; fx avg `-0.0498` n `6`; index avg `0.6154` n `25`; metal avg `0.6729` n `20`; unknown avg `8.9398` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
