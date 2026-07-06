# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T03:22:24.609187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0195` n `12`; crypto_alt avg `-0.21` n `229`; crypto_major avg `-0.3897` n `8`; equity avg `-0.019` n `88`; fx avg `-0.0047` n `6`; index avg `-0.0184` n `25`; metal avg `-0.0152` n `20`; unknown avg `2.8073` n `765`
- 1h: commodity avg `-0.1394` n `12`; crypto_alt avg `-0.4548` n `229`; crypto_major avg `-0.7287` n `8`; equity avg `-0.2665` n `88`; fx avg `-0.0179` n `6`; index avg `-0.044` n `25`; metal avg `-0.1993` n `20`; unknown avg `0.311` n `763`
- 4h: commodity avg `-0.0702` n `12`; crypto_alt avg `-0.8185` n `229`; crypto_major avg `-0.9675` n `8`; equity avg `-1.4428` n `88`; fx avg `0.0506` n `6`; index avg `-0.2301` n `25`; metal avg `-0.4124` n `20`; unknown avg `-0.0221` n `763`
- 24h: commodity avg `-0.2635` n `12`; crypto_alt avg `0.5976` n `229`; crypto_major avg `1.4203` n `8`; equity avg `-0.9648` n `88`; fx avg `0.0747` n `6`; index avg `-0.1327` n `25`; metal avg `-0.1977` n `20`; unknown avg `1.019` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
