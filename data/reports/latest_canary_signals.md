# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T17:37:15.807398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0524` n `12`; crypto_alt avg `-0.3468` n `228`; crypto_major avg `-0.2117` n `8`; equity avg `-0.0354` n `69`; fx avg `-0.0006` n `6`; index avg `-0.0487` n `23`; metal avg `-0.0162` n `18`; unknown avg `-0.2012` n `421`
- 1h: commodity avg `-0.0472` n `12`; crypto_alt avg `-0.3462` n `228`; crypto_major avg `-0.2049` n `8`; equity avg `0.021` n `69`; fx avg `-0.0085` n `6`; index avg `-0.0412` n `23`; metal avg `-0.0029` n `18`; unknown avg `-0.3856` n `421`
- 4h: commodity avg `-0.3888` n `12`; crypto_alt avg `0.2406` n `228`; crypto_major avg `0.74` n `8`; equity avg `-0.0645` n `69`; fx avg `0.0025` n `6`; index avg `-0.0674` n `23`; metal avg `0.0352` n `18`; unknown avg `-0.0613` n `421`
- 24h: commodity avg `0.1029` n `12`; crypto_alt avg `-0.1357` n `228`; crypto_major avg `1.1342` n `8`; equity avg `0.6197` n `69`; fx avg `0.0018` n `6`; index avg `-0.0172` n `23`; metal avg `-0.0548` n `18`; unknown avg `0.0143` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1903`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
