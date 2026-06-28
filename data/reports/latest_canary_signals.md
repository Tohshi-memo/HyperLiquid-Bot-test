# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T00:07:30.308599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0909` n `12`; crypto_alt avg `0.0003` n `228`; crypto_major avg `0.0465` n `8`; equity avg `-0.0028` n `88`; fx avg `-0.0065` n `6`; index avg `0.0172` n `23`; metal avg `0.033` n `20`; unknown avg `0.034` n `764`
- 1h: commodity avg `0.2378` n `12`; crypto_alt avg `-0.2714` n `228`; crypto_major avg `-0.4818` n `8`; equity avg `-0.0701` n `88`; fx avg `-0.0205` n `6`; index avg `-0.0034` n `23`; metal avg `0.0181` n `20`; unknown avg `58.24` n `764`
- 4h: commodity avg `0.246` n `12`; crypto_alt avg `-0.2934` n `228`; crypto_major avg `-0.4426` n `8`; equity avg `-0.011` n `88`; fx avg `-0.0113` n `6`; index avg `-0.034` n `23`; metal avg `0.0358` n `20`; unknown avg `-0.5252` n `764`
- 24h: commodity avg `0.1984` n `12`; crypto_alt avg `-0.978` n `228`; crypto_major avg `-1.3528` n `8`; equity avg `0.1769` n `88`; fx avg `0.0163` n `6`; index avg `-0.0583` n `23`; metal avg `-0.0603` n `20`; unknown avg `-0.8393` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
