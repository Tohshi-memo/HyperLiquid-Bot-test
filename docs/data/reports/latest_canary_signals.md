# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T05:37:29.702059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0185` n `12`; crypto_alt avg `0.1309` n `230`; crypto_major avg `0.1425` n `8`; equity avg `-0.027` n `113`; fx avg `0.0075` n `6`; index avg `0.0048` n `25`; metal avg `-0.1589` n `20`; unknown avg `-0.1675` n `785`
- 1h: commodity avg `0.0643` n `12`; crypto_alt avg `-0.0221` n `230`; crypto_major avg `-0.1049` n `8`; equity avg `-0.181` n `113`; fx avg `0.0155` n `6`; index avg `-0.0345` n `25`; metal avg `-0.26` n `20`; unknown avg `0.1366` n `785`
- 4h: commodity avg `0.0241` n `12`; crypto_alt avg `-0.1796` n `230`; crypto_major avg `0.0221` n `8`; equity avg `0.0977` n `113`; fx avg `0.0106` n `6`; index avg `0.052` n `25`; metal avg `-0.3617` n `20`; unknown avg `-0.3506` n `785`
- 24h: commodity avg `0.9114` n `12`; crypto_alt avg `-0.6844` n `230`; crypto_major avg `-0.6638` n `8`; equity avg `-0.9303` n `113`; fx avg `0.094` n `6`; index avg `0.0402` n `25`; metal avg `0.1007` n `20`; unknown avg `103.9216` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
