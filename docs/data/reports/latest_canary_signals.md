# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T01:52:34.799954+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0359` n `12`; crypto_alt avg `0.1531` n `228`; crypto_major avg `0.0546` n `8`; equity avg `0.0069` n `88`; fx avg `-0.0032` n `6`; index avg `0.0013` n `23`; metal avg `0.0085` n `20`; unknown avg `8.0357` n `764`
- 1h: commodity avg `0.0696` n `12`; crypto_alt avg `0.0928` n `228`; crypto_major avg `0.1266` n `8`; equity avg `-0.059` n `88`; fx avg `-0.0026` n `6`; index avg `-0.0215` n `23`; metal avg `0.0088` n `20`; unknown avg `28.5922` n `764`
- 4h: commodity avg `0.2786` n `12`; crypto_alt avg `0.3214` n `228`; crypto_major avg `-0.0396` n `8`; equity avg `-0.1103` n `88`; fx avg `-0.0247` n `6`; index avg `-0.0897` n `23`; metal avg `0.0389` n `20`; unknown avg `-0.7266` n `764`
- 24h: commodity avg `0.4175` n `12`; crypto_alt avg `-0.342` n `228`; crypto_major avg `-0.6458` n `8`; equity avg `0.1607` n `88`; fx avg `-0.0051` n `6`; index avg `-0.1116` n `23`; metal avg `-0.0447` n `20`; unknown avg `-0.5163` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2144`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
