# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T12:22:23.021122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `12`; crypto_alt avg `0.0865` n `228`; crypto_major avg `0.0637` n `8`; equity avg `0.0373` n `69`; fx avg `0.0` n `6`; index avg `0.014` n `23`; metal avg `0.0056` n `18`; unknown avg `-0.2162` n `421`
- 1h: commodity avg `0.112` n `12`; crypto_alt avg `0.3471` n `228`; crypto_major avg `0.3461` n `8`; equity avg `0.1292` n `69`; fx avg `0.0004` n `6`; index avg `0.0313` n `23`; metal avg `-0.021` n `18`; unknown avg `0.8461` n `421`
- 4h: commodity avg `0.2121` n `12`; crypto_alt avg `0.1744` n `228`; crypto_major avg `0.4126` n `8`; equity avg `0.1641` n `69`; fx avg `0.0358` n `6`; index avg `-0.0466` n `23`; metal avg `0.0091` n `18`; unknown avg `0.7302` n `421`
- 24h: commodity avg `-0.1633` n `12`; crypto_alt avg `2.1577` n `228`; crypto_major avg `2.6888` n `8`; equity avg `1.4783` n `69`; fx avg `0.1102` n `6`; index avg `0.0029` n `23`; metal avg `0.2245` n `18`; unknown avg `1.4371` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1919`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
