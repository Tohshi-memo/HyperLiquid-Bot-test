# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T02:37:29.368534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0087` n `12`; crypto_alt avg `0.1185` n `229`; crypto_major avg `0.0682` n `8`; equity avg `0.0126` n `88`; fx avg `0.0209` n `6`; index avg `-0.0074` n `25`; metal avg `-0.0002` n `20`; unknown avg `-0.1996` n `765`
- 1h: commodity avg `-0.0037` n `12`; crypto_alt avg `0.2393` n `229`; crypto_major avg `-0.0127` n `8`; equity avg `0.0775` n `88`; fx avg `0.0163` n `6`; index avg `0.0016` n `25`; metal avg `0.0103` n `20`; unknown avg `-0.3618` n `763`
- 4h: commodity avg `-0.0136` n `12`; crypto_alt avg `-0.5016` n `229`; crypto_major avg `-0.3431` n `8`; equity avg `0.0977` n `88`; fx avg `-0.0068` n `6`; index avg `-0.0441` n `25`; metal avg `-0.0131` n `20`; unknown avg `0.032` n `763`
- 24h: commodity avg `-0.0116` n `12`; crypto_alt avg `2.0972` n `229`; crypto_major avg `2.6134` n `8`; equity avg `0.9114` n `88`; fx avg `-0.1364` n `6`; index avg `0.18` n `25`; metal avg `-0.1912` n `20`; unknown avg `3.9223` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
