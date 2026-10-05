# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T06:37:29.232942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0666` n `13`; crypto_alt avg `-0.0371` n `235`; crypto_major avg `-0.0235` n `8`; equity avg `-0.0378` n `144`; fx avg `-0.0235` n `6`; index avg `-0.0071` n `26`; metal avg `-0.0119` n `20`; unknown avg `0.2461` n `1079`
- 1h: commodity avg `0.007` n `13`; crypto_alt avg `0.2207` n `235`; crypto_major avg `0.3142` n `8`; equity avg `0.1051` n `144`; fx avg `-0.052` n `6`; index avg `0.0221` n `26`; metal avg `0.1189` n `20`; unknown avg `2.3136` n `1061`
- 4h: commodity avg `0.0393` n `13`; crypto_alt avg `-0.5458` n `235`; crypto_major avg `-0.5288` n `8`; equity avg `-0.2216` n `144`; fx avg `-0.0747` n `6`; index avg `-0.0687` n `26`; metal avg `-0.0029` n `20`; unknown avg `1.184` n `970`
- 24h: commodity avg `-0.2844` n `13`; crypto_alt avg `0.5166` n `235`; crypto_major avg `1.0442` n `8`; equity avg `0.287` n `144`; fx avg `-0.1067` n `6`; index avg `-0.0455` n `26`; metal avg `0.1718` n `20`; unknown avg `0.1196` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
