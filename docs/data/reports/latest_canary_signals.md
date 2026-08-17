# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T04:22:32.658062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0338` n `12`; crypto_alt avg `0.003` n `230`; crypto_major avg `0.0149` n `8`; equity avg `0.0466` n `114`; fx avg `-0.0029` n `6`; index avg `0.0079` n `25`; metal avg `-0.0225` n `20`; unknown avg `-0.0547` n `792`
- 1h: commodity avg `-0.0034` n `12`; crypto_alt avg `0.1465` n `230`; crypto_major avg `0.1779` n `8`; equity avg `0.1393` n `114`; fx avg `0.0094` n `6`; index avg `0.0301` n `25`; metal avg `-0.0116` n `20`; unknown avg `0.2344` n `792`
- 4h: commodity avg `0.0246` n `12`; crypto_alt avg `0.998` n `230`; crypto_major avg `1.298` n `8`; equity avg `0.6803` n `114`; fx avg `0.0056` n `6`; index avg `0.0521` n `25`; metal avg `0.1039` n `20`; unknown avg `1.6913` n `792`
- 24h: commodity avg `-0.1771` n `12`; crypto_alt avg `0.5275` n `230`; crypto_major avg `0.7293` n `8`; equity avg `0.8002` n `114`; fx avg `-0.023` n `6`; index avg `0.0985` n `25`; metal avg `0.1904` n `20`; unknown avg `0.1401` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
