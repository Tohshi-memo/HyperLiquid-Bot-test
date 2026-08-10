# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T21:52:41.780877+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.1487` n `230`; crypto_major avg `-0.1773` n `8`; equity avg `-0.0191` n `113`; fx avg `0.0022` n `6`; index avg `-0.0001` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.0071` n `785`
- 1h: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.3688` n `230`; crypto_major avg `-0.2379` n `8`; equity avg `-0.1168` n `113`; fx avg `-0.0041` n `6`; index avg `0.0043` n `25`; metal avg `0.0423` n `20`; unknown avg `0.0782` n `785`
- 4h: commodity avg `0.0594` n `12`; crypto_alt avg `-0.4697` n `230`; crypto_major avg `0.1052` n `8`; equity avg `-0.4916` n `113`; fx avg `0.0017` n `6`; index avg `-0.0069` n `25`; metal avg `0.2282` n `20`; unknown avg `0.9321` n `785`
- 24h: commodity avg `1.0809` n `12`; crypto_alt avg `-1.4027` n `230`; crypto_major avg `-1.1982` n `8`; equity avg `-1.8381` n `113`; fx avg `0.2654` n `6`; index avg `-0.0905` n `25`; metal avg `0.2916` n `20`; unknown avg `103.6428` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
