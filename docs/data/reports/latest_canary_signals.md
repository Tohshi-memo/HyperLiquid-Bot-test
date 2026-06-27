# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T12:22:30.004860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `0.1078` n `228`; crypto_major avg `0.0949` n `8`; equity avg `-0.0067` n `88`; fx avg `0.0021` n `6`; index avg `0.0` n `23`; metal avg `-0.0012` n `20`; unknown avg `0.0347` n `764`
- 1h: commodity avg `0.0786` n `12`; crypto_alt avg `0.3818` n `228`; crypto_major avg `0.1233` n `8`; equity avg `0.0066` n `88`; fx avg `0.0011` n `6`; index avg `0.0133` n `23`; metal avg `0.0054` n `20`; unknown avg `3.293` n `764`
- 4h: commodity avg `0.1165` n `12`; crypto_alt avg `0.0993` n `228`; crypto_major avg `-0.2321` n `8`; equity avg `-0.0184` n `88`; fx avg `-0.008` n `6`; index avg `-0.0149` n `23`; metal avg `-0.0106` n `20`; unknown avg `0.0314` n `764`
- 24h: commodity avg `0.1397` n `12`; crypto_alt avg `1.9624` n `228`; crypto_major avg `1.7392` n `8`; equity avg `1.9257` n `87`; fx avg `0.0387` n `6`; index avg `0.0736` n `23`; metal avg `0.3848` n `20`; unknown avg `0.1933` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2062`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
