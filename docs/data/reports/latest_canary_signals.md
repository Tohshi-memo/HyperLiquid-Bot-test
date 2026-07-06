# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T02:22:24.966461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.97` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0128` n `12`; crypto_alt avg `0.329` n `229`; crypto_major avg `0.3511` n `8`; equity avg `-0.001` n `88`; fx avg `0.0121` n `6`; index avg `-0.0287` n `25`; metal avg `0.0035` n `20`; unknown avg `-0.1343` n `765`
- 1h: commodity avg `0.0869` n `12`; crypto_alt avg `-0.1474` n `229`; crypto_major avg `-0.2485` n `8`; equity avg `-0.6595` n `88`; fx avg `0.0586` n `6`; index avg `-0.1863` n `25`; metal avg `-0.0799` n `20`; unknown avg `-0.2047` n `765`
- 4h: commodity avg `0.0069` n `12`; crypto_alt avg `-0.3418` n `229`; crypto_major avg `-0.1633` n `8`; equity avg `-1.0873` n `88`; fx avg `0.0741` n `6`; index avg `-0.1388` n `25`; metal avg `-0.0845` n `20`; unknown avg `-0.6369` n `765`
- 24h: commodity avg `-0.1252` n `12`; crypto_alt avg `0.8652` n `229`; crypto_major avg `1.9457` n `8`; equity avg `-0.6793` n `88`; fx avg `0.091` n `6`; index avg `-0.0828` n `25`; metal avg `-0.0095` n `20`; unknown avg `1.3029` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
