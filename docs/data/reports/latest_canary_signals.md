# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T04:22:29.614290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `0.0137` n `229`; crypto_major avg `0.1094` n `8`; equity avg `0.1356` n `88`; fx avg `-0.0036` n `6`; index avg `0.0675` n `25`; metal avg `0.0089` n `20`; unknown avg `-0.1467` n `765`
- 1h: commodity avg `0.0591` n `12`; crypto_alt avg `-0.0263` n `229`; crypto_major avg `0.1328` n `8`; equity avg `0.2631` n `88`; fx avg `-0.0047` n `6`; index avg `0.0528` n `25`; metal avg `-0.036` n `20`; unknown avg `0.283` n `765`
- 4h: commodity avg `-0.0022` n `12`; crypto_alt avg `-0.2704` n `229`; crypto_major avg `-0.2543` n `8`; equity avg `-0.9441` n `88`; fx avg `0.0093` n `6`; index avg `-0.2677` n `25`; metal avg `-0.297` n `20`; unknown avg `-0.4701` n `763`
- 24h: commodity avg `-0.2082` n `12`; crypto_alt avg `0.4343` n `229`; crypto_major avg `1.2284` n `8`; equity avg `-0.7934` n `88`; fx avg `0.0725` n `6`; index avg `-0.0714` n `25`; metal avg `-0.2405` n `20`; unknown avg `1.1032` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
