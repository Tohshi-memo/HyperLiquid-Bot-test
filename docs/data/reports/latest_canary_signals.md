# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T05:52:26.135670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0501` n `12`; crypto_alt avg `0.0605` n `233`; crypto_major avg `0.0457` n `8`; equity avg `-0.0167` n `136`; fx avg `-0.0024` n `6`; index avg `0.0007` n `26`; metal avg `0.0033` n `20`; unknown avg `1.5045` n `838`
- 1h: commodity avg `0.0815` n `12`; crypto_alt avg `0.1746` n `233`; crypto_major avg `0.2052` n `8`; equity avg `-0.1034` n `136`; fx avg `-0.0088` n `6`; index avg `-0.0172` n `26`; metal avg `0.0073` n `20`; unknown avg `49.8408` n `836`
- 4h: commodity avg `0.1078` n `12`; crypto_alt avg `0.017` n `233`; crypto_major avg `-0.1041` n `8`; equity avg `-0.2538` n `136`; fx avg `-0.0002` n `6`; index avg `-0.0511` n `26`; metal avg `0.0046` n `20`; unknown avg `0.6092` n `806`
- 24h: commodity avg `0.1721` n `12`; crypto_alt avg `1.171` n `233`; crypto_major avg `0.2207` n `8`; equity avg `-0.5969` n `136`; fx avg `-0.0117` n `6`; index avg `-0.0894` n `26`; metal avg `0.0434` n `20`; unknown avg `-0.0186` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
