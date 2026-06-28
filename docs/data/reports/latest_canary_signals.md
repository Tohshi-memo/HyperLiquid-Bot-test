# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T03:37:29.330652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0402` n `12`; crypto_alt avg `0.0345` n `228`; crypto_major avg `-0.0814` n `8`; equity avg `0.0048` n `88`; fx avg `-0.0011` n `6`; index avg `0.0018` n `23`; metal avg `0.0167` n `20`; unknown avg `0.1618` n `764`
- 1h: commodity avg `-0.198` n `12`; crypto_alt avg `0.2165` n `228`; crypto_major avg `0.1129` n `8`; equity avg `0.047` n `88`; fx avg `-0.0042` n `6`; index avg `0.0086` n `23`; metal avg `0.0324` n `20`; unknown avg `6.9001` n `730`
- 4h: commodity avg `0.115` n `12`; crypto_alt avg `0.4364` n `228`; crypto_major avg `0.1454` n `8`; equity avg `-0.0017` n `88`; fx avg `-0.0401` n `6`; index avg `-0.0261` n `23`; metal avg `0.0663` n `20`; unknown avg `15.6591` n `722`
- 24h: commodity avg `0.2729` n `12`; crypto_alt avg `-0.6956` n `228`; crypto_major avg `-1.3457` n `8`; equity avg `0.0397` n `88`; fx avg `-0.0215` n `6`; index avg `-0.1132` n `23`; metal avg `-0.0276` n `20`; unknown avg `9.9389` n `674`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2176`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1808`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
