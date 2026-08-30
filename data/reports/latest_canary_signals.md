# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T16:22:24.646689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `12`; crypto_alt avg `0.2788` n `231`; crypto_major avg `0.4235` n `8`; equity avg `0.0842` n `128`; fx avg `0.001` n `6`; index avg `0.0077` n `26`; metal avg `0.0174` n `20`; unknown avg `1.4436` n `793`
- 1h: commodity avg `0.0219` n `12`; crypto_alt avg `0.3524` n `231`; crypto_major avg `0.5053` n `8`; equity avg `0.1006` n `128`; fx avg `0.0005` n `6`; index avg `0.0127` n `26`; metal avg `0.0586` n `20`; unknown avg `1.5839` n `793`
- 4h: commodity avg `0.0464` n `12`; crypto_alt avg `0.4136` n `231`; crypto_major avg `0.8533` n `8`; equity avg `0.0903` n `128`; fx avg `0.0031` n `6`; index avg `0.0279` n `26`; metal avg `0.1158` n `20`; unknown avg `0.2491` n `793`
- 24h: commodity avg `0.0029` n `12`; crypto_alt avg `1.3596` n `231`; crypto_major avg `1.3074` n `8`; equity avg `0.3731` n `128`; fx avg `0.016` n `6`; index avg `0.0746` n `26`; metal avg `0.1353` n `20`; unknown avg `-0.041` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
