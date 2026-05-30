# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T15:37:18.186659+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1154` n `12`; crypto_alt avg `0.0219` n `228`; crypto_major avg `0.0508` n `8`; equity avg `-0.01` n `69`; fx avg `0.0014` n `6`; index avg `-0.0645` n `23`; metal avg `0.03` n `18`; unknown avg `1.3494` n `421`
- 1h: commodity avg `0.0969` n `12`; crypto_alt avg `-0.2029` n `228`; crypto_major avg `0.0213` n `8`; equity avg `-0.0172` n `69`; fx avg `0.0038` n `6`; index avg `-0.0936` n `23`; metal avg `0.0083` n `18`; unknown avg `0.8278` n `421`
- 4h: commodity avg `0.2977` n `12`; crypto_alt avg `0.1052` n `228`; crypto_major avg `0.6629` n `8`; equity avg `0.4016` n `69`; fx avg `0.0282` n `6`; index avg `0.077` n `23`; metal avg `-0.0078` n `18`; unknown avg `0.4743` n `421`
- 24h: commodity avg `0.3547` n `12`; crypto_alt avg `0.2565` n `228`; crypto_major avg `1.3823` n `8`; equity avg `1.1481` n `69`; fx avg `0.0028` n `6`; index avg `0.2764` n `23`; metal avg `-0.3302` n `18`; unknown avg `0.2557` n `400`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1919`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
