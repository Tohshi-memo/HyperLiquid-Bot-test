# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T16:37:23.000778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `0.2266` n `231`; crypto_major avg `0.1765` n `8`; equity avg `0.0237` n `128`; fx avg `0.0014` n `6`; index avg `0.0121` n `26`; metal avg `0.0108` n `20`; unknown avg `0.0528` n `793`
- 1h: commodity avg `0.0052` n `12`; crypto_alt avg `0.5147` n `231`; crypto_major avg `0.6241` n `8`; equity avg `0.1214` n `128`; fx avg `-0.0008` n `6`; index avg `0.0241` n `26`; metal avg `0.0499` n `20`; unknown avg `1.3854` n `793`
- 4h: commodity avg `0.0482` n `12`; crypto_alt avg `0.5973` n `231`; crypto_major avg `1.0233` n `8`; equity avg `0.1428` n `128`; fx avg `0.0031` n `6`; index avg `0.0139` n `26`; metal avg `0.1195` n `20`; unknown avg `0.3912` n `793`
- 24h: commodity avg `0.0151` n `12`; crypto_alt avg `1.4916` n `231`; crypto_major avg `1.3304` n `8`; equity avg `0.3882` n `128`; fx avg `0.0221` n `6`; index avg `0.091` n `26`; metal avg `0.1465` n `20`; unknown avg `0.1195` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
