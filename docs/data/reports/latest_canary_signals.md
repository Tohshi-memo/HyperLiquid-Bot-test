# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T09:52:51.950089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0208` n `12`; crypto_alt avg `0.1189` n `228`; crypto_major avg `-0.0151` n `8`; equity avg `-0.0252` n `88`; fx avg `-0.0094` n `6`; index avg `-0.0077` n `23`; metal avg `-0.006` n `20`; unknown avg `0.0199` n `764`
- 1h: commodity avg `0.037` n `12`; crypto_alt avg `-0.1368` n `228`; crypto_major avg `-0.3063` n `8`; equity avg `-0.0074` n `88`; fx avg `-0.0106` n `6`; index avg `-0.0108` n `23`; metal avg `-0.0185` n `20`; unknown avg `-0.1424` n `764`
- 4h: commodity avg `0.0637` n `12`; crypto_alt avg `-0.343` n `228`; crypto_major avg `-0.3198` n `8`; equity avg `0.1874` n `88`; fx avg `0.0025` n `6`; index avg `0.0065` n `23`; metal avg `-0.0256` n `20`; unknown avg `-0.1139` n `732`
- 24h: commodity avg `0.1773` n `12`; crypto_alt avg `1.5123` n `228`; crypto_major avg `1.3362` n `8`; equity avg `1.797` n `87`; fx avg `0.0264` n `6`; index avg `0.0682` n `23`; metal avg `0.4125` n `20`; unknown avg `-0.0719` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2058`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
