# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T13:37:28.904045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `-0.0155` n `228`; crypto_major avg `0.0509` n `8`; equity avg `-0.0065` n `88`; fx avg `0.0006` n `6`; index avg `0.0013` n `23`; metal avg `0.0007` n `20`; unknown avg `-0.0082` n `764`
- 1h: commodity avg `-0.0045` n `12`; crypto_alt avg `0.1451` n `228`; crypto_major avg `0.3728` n `8`; equity avg `0.0534` n `88`; fx avg `-0.0006` n `6`; index avg `0.0121` n `23`; metal avg `0.0037` n `20`; unknown avg `0.0312` n `764`
- 4h: commodity avg `0.123` n `12`; crypto_alt avg `0.4269` n `228`; crypto_major avg `0.4628` n `8`; equity avg `0.0443` n `88`; fx avg `0.0008` n `6`; index avg `0.0002` n `23`; metal avg `0.0022` n `20`; unknown avg `0.2169` n `764`
- 24h: commodity avg `0.1933` n `12`; crypto_alt avg `2.3901` n `228`; crypto_major avg `2.6276` n `8`; equity avg `2.0328` n `87`; fx avg `0.0177` n `6`; index avg `0.1375` n `23`; metal avg `0.4553` n `20`; unknown avg `0.427` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2094`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
