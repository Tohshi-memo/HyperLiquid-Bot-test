# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T09:52:29.478156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `0.1675` n `229`; crypto_major avg `0.1755` n `8`; equity avg `0.0126` n `88`; fx avg `-0.0107` n `6`; index avg `0.0165` n `25`; metal avg `0.043` n `20`; unknown avg `0.0979` n `765`
- 1h: commodity avg `-0.013` n `12`; crypto_alt avg `0.1374` n `229`; crypto_major avg `0.1858` n `8`; equity avg `0.0557` n `88`; fx avg `0.0136` n `6`; index avg `-0.0091` n `25`; metal avg `-0.0306` n `20`; unknown avg `0.2921` n `755`
- 4h: commodity avg `-0.1148` n `12`; crypto_alt avg `0.4778` n `229`; crypto_major avg `0.1506` n `8`; equity avg `0.2343` n `88`; fx avg `-0.1319` n `6`; index avg `0.0826` n `25`; metal avg `0.053` n `20`; unknown avg `0.193` n `739`
- 24h: commodity avg `0.4223` n `12`; crypto_alt avg `1.524` n `229`; crypto_major avg `2.4338` n `8`; equity avg `0.1367` n `88`; fx avg `-0.0816` n `6`; index avg `0.2211` n `25`; metal avg `1.17` n `20`; unknown avg `5.6018` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
