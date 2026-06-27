# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T10:22:27.341595+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `12`; crypto_alt avg `-0.0398` n `228`; crypto_major avg `0.0985` n `8`; equity avg `0.0081` n `88`; fx avg `0.0199` n `6`; index avg `0.0019` n `23`; metal avg `0.0012` n `20`; unknown avg `-0.0302` n `764`
- 1h: commodity avg `0.0119` n `12`; crypto_alt avg `0.2108` n `228`; crypto_major avg `0.2143` n `8`; equity avg `0.0052` n `88`; fx avg `0.038` n `6`; index avg `0.0012` n `23`; metal avg `-0.0027` n `20`; unknown avg `-0.0284` n `764`
- 4h: commodity avg `0.1231` n `12`; crypto_alt avg `-0.0404` n `228`; crypto_major avg `0.0757` n `8`; equity avg `0.2088` n `88`; fx avg `0.0036` n `6`; index avg `0.0189` n `23`; metal avg `-0.0255` n `20`; unknown avg `-0.1669` n `748`
- 24h: commodity avg `0.1763` n `12`; crypto_alt avg `1.5927` n `228`; crypto_major avg `1.6345` n `8`; equity avg `1.9118` n `87`; fx avg `0.0231` n `6`; index avg `0.0909` n `23`; metal avg `0.4714` n `20`; unknown avg `0.006` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2057`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
