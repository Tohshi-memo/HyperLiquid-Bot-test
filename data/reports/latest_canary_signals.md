# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T03:22:23.480638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0609` n `12`; crypto_alt avg `0.085` n `228`; crypto_major avg `0.0909` n `8`; equity avg `0.0115` n `69`; fx avg `-0.0006` n `6`; index avg `0.0213` n `23`; metal avg `-0.0129` n `18`; unknown avg `-0.188` n `421`
- 1h: commodity avg `0.0235` n `12`; crypto_alt avg `-0.1989` n `228`; crypto_major avg `-0.0323` n `8`; equity avg `0.05` n `69`; fx avg `-0.0026` n `6`; index avg `0.0259` n `23`; metal avg `-0.0043` n `18`; unknown avg `-0.4709` n `419`
- 4h: commodity avg `0.0904` n `12`; crypto_alt avg `0.7423` n `228`; crypto_major avg `0.8762` n `8`; equity avg `0.1604` n `69`; fx avg `0.023` n `6`; index avg `0.0223` n `23`; metal avg `-0.0442` n `18`; unknown avg `-0.046` n `419`
- 24h: commodity avg `-0.0683` n `12`; crypto_alt avg `0.1472` n `228`; crypto_major avg `2.1945` n `8`; equity avg `0.94` n `69`; fx avg `0.0443` n `6`; index avg `0.1412` n `23`; metal avg `-0.0597` n `18`; unknown avg `1.477` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
