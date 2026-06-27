# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T21:22:26.335193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `0.1071` n `228`; crypto_major avg `0.0702` n `8`; equity avg `-0.0008` n `88`; fx avg `-0.0023` n `6`; index avg `-0.0067` n `23`; metal avg `-0.0073` n `20`; unknown avg `-0.0181` n `764`
- 1h: commodity avg `-0.0972` n `12`; crypto_alt avg `0.1621` n `228`; crypto_major avg `0.2039` n `8`; equity avg `0.0449` n `88`; fx avg `-0.0034` n `6`; index avg `0.0031` n `23`; metal avg `0.0023` n `20`; unknown avg `-0.0329` n `764`
- 4h: commodity avg `-0.0586` n `12`; crypto_alt avg `-0.4711` n `228`; crypto_major avg `-0.663` n `8`; equity avg `0.0102` n `88`; fx avg `0.0017` n `6`; index avg `0.0063` n `23`; metal avg `-0.0242` n `20`; unknown avg `-0.1998` n `764`
- 24h: commodity avg `-0.0746` n `12`; crypto_alt avg `-0.0324` n `228`; crypto_major avg `-0.1206` n `8`; equity avg `0.5835` n `88`; fx avg `-0.0086` n `6`; index avg `0.0258` n `23`; metal avg `0.0096` n `20`; unknown avg `-0.1939` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2084`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
