# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T14:52:21.899883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `12`; crypto_alt avg `-0.1504` n `228`; crypto_major avg `-0.097` n `8`; equity avg `-0.009` n `69`; fx avg `0.0005` n `6`; index avg `-0.0321` n `23`; metal avg `-0.0142` n `18`; unknown avg `0.1677` n `421`
- 1h: commodity avg `0.013` n `12`; crypto_alt avg `-0.9561` n `228`; crypto_major avg `-0.4821` n `8`; equity avg `-0.1185` n `69`; fx avg `-0.0019` n `6`; index avg `0.0162` n `23`; metal avg `-0.0014` n `18`; unknown avg `0.011` n `421`
- 4h: commodity avg `0.091` n `12`; crypto_alt avg `-0.8456` n `228`; crypto_major avg `-0.2586` n `8`; equity avg `-0.0006` n `69`; fx avg `-0.0192` n `6`; index avg `-0.0327` n `23`; metal avg `-0.0069` n `18`; unknown avg `-0.117` n `421`
- 24h: commodity avg `0.1271` n `12`; crypto_alt avg `-0.9892` n `228`; crypto_major avg `0.2304` n `8`; equity avg `0.6311` n `69`; fx avg `-0.025` n `6`; index avg `-0.2894` n `23`; metal avg `-0.0477` n `18`; unknown avg `0.1757` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
