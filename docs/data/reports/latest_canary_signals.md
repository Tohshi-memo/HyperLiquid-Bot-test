# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T02:07:29.720786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0262` n `12`; crypto_alt avg `-0.0859` n `232`; crypto_major avg `-0.0505` n `8`; equity avg `-0.05` n `133`; fx avg `-0.014` n `6`; index avg `-0.0086` n `26`; metal avg `0.0092` n `20`; unknown avg `-0.1529` n `790`
- 1h: commodity avg `0.1221` n `12`; crypto_alt avg `0.2208` n `232`; crypto_major avg `0.16` n `8`; equity avg `-0.0911` n `133`; fx avg `-0.0421` n `6`; index avg `-0.0131` n `26`; metal avg `0.0961` n `20`; unknown avg `14.5116` n `790`
- 4h: commodity avg `0.1593` n `12`; crypto_alt avg `0.639` n `232`; crypto_major avg `0.4412` n `8`; equity avg `0.0697` n `133`; fx avg `-0.0377` n `6`; index avg `-0.0139` n `26`; metal avg `0.1303` n `20`; unknown avg `14.294` n `790`
- 24h: commodity avg `0.1946` n `12`; crypto_alt avg `0.8917` n `232`; crypto_major avg `0.532` n `8`; equity avg `1.3717` n `133`; fx avg `-0.3776` n `6`; index avg `0.1412` n `26`; metal avg `0.8605` n `20`; unknown avg `-0.3464` n `751`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
