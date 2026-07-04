# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T03:37:25.875730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `0.1067` n `229`; crypto_major avg `0.2853` n `8`; equity avg `0.047` n `88`; fx avg `0.0069` n `6`; index avg `0.009` n `25`; metal avg `-0.0011` n `20`; unknown avg `4.1359` n `765`
- 1h: commodity avg `0.0071` n `12`; crypto_alt avg `0.3749` n `229`; crypto_major avg `0.5587` n `8`; equity avg `0.1338` n `88`; fx avg `-0.0142` n `6`; index avg `0.0211` n `25`; metal avg `0.0026` n `20`; unknown avg `3.7277` n `765`
- 4h: commodity avg `0.0036` n `12`; crypto_alt avg `-0.1163` n `229`; crypto_major avg `0.0976` n `8`; equity avg `0.1924` n `88`; fx avg `-0.0062` n `6`; index avg `-0.0148` n `25`; metal avg `-0.0433` n `20`; unknown avg `0.4451` n `763`
- 24h: commodity avg `-0.0145` n `12`; crypto_alt avg `2.4204` n `229`; crypto_major avg `3.0527` n `8`; equity avg `0.9029` n `88`; fx avg `-0.176` n `6`; index avg `0.1781` n `25`; metal avg `-0.1319` n `20`; unknown avg `4.7393` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
