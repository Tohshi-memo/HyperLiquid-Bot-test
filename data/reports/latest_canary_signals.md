# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T13:22:16.092056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.0369` n `228`; crypto_major avg `0.0421` n `8`; equity avg `0.0656` n `69`; fx avg `-0.0158` n `6`; index avg `-0.0086` n `23`; metal avg `-0.0017` n `18`; unknown avg `-0.1922` n `421`
- 1h: commodity avg `0.0215` n `12`; crypto_alt avg `0.0738` n `228`; crypto_major avg `0.1248` n `8`; equity avg `0.1382` n `69`; fx avg `0.002` n `6`; index avg `0.0462` n `23`; metal avg `-0.0146` n `18`; unknown avg `-0.0168` n `421`
- 4h: commodity avg `0.246` n `12`; crypto_alt avg `0.2618` n `228`; crypto_major avg `0.4484` n `8`; equity avg `0.2903` n `69`; fx avg `0.018` n `6`; index avg `0.0468` n `23`; metal avg `-0.0076` n `18`; unknown avg `-0.0194` n `421`
- 24h: commodity avg `-0.2985` n `12`; crypto_alt avg `2.9483` n `228`; crypto_major avg `3.1228` n `8`; equity avg `1.718` n `69`; fx avg `0.0627` n `6`; index avg `-0.0047` n `23`; metal avg `-0.2415` n `18`; unknown avg `0.3465` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
