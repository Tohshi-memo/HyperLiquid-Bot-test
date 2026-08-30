# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T18:22:31.963969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `12`; crypto_alt avg `0.0737` n `231`; crypto_major avg `0.0924` n `8`; equity avg `-0.0105` n `128`; fx avg `-0.0012` n `6`; index avg `0.0072` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.0473` n `793`
- 1h: commodity avg `0.0154` n `12`; crypto_alt avg `-0.0284` n `231`; crypto_major avg `0.102` n `8`; equity avg `-0.027` n `128`; fx avg `-0.0079` n `6`; index avg `0.0016` n `26`; metal avg `-0.0116` n `20`; unknown avg `-0.0424` n `793`
- 4h: commodity avg `0.049` n `12`; crypto_alt avg `0.3617` n `231`; crypto_major avg `0.2665` n `8`; equity avg `0.0715` n `128`; fx avg `0.0122` n `6`; index avg `0.025` n `26`; metal avg `0.016` n `20`; unknown avg `0.353` n `793`
- 24h: commodity avg `0.0402` n `12`; crypto_alt avg `1.6582` n `231`; crypto_major avg `1.184` n `8`; equity avg `0.3837` n `128`; fx avg `0.017` n `6`; index avg `0.1084` n `26`; metal avg `0.1063` n `20`; unknown avg `0.1704` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
