# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T13:07:32.288862+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `12`; crypto_alt avg `0.0541` n `228`; crypto_major avg `0.1124` n `8`; equity avg `0.0527` n `88`; fx avg `0.0` n `6`; index avg `0.005` n `23`; metal avg `0.0061` n `20`; unknown avg `-0.0418` n `764`
- 1h: commodity avg `-0.0181` n `12`; crypto_alt avg `0.1119` n `228`; crypto_major avg `0.3379` n `8`; equity avg `0.0552` n `88`; fx avg `0.0021` n `6`; index avg `0.0049` n `23`; metal avg `0.0051` n `20`; unknown avg `0.0748` n `764`
- 4h: commodity avg `0.1301` n `12`; crypto_alt avg `0.1272` n `228`; crypto_major avg `0.0122` n `8`; equity avg `0.0512` n `88`; fx avg `0.0223` n `6`; index avg `-0.007` n `23`; metal avg `-0.0062` n `20`; unknown avg `0.129` n `764`
- 24h: commodity avg `0.1606` n `12`; crypto_alt avg `2.6897` n `228`; crypto_major avg `2.8562` n `8`; equity avg `2.4936` n `87`; fx avg `0.0031` n `6`; index avg `0.1602` n `23`; metal avg `0.3825` n `20`; unknown avg `0.4302` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.208`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
