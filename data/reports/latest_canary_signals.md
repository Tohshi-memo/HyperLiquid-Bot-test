# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T02:04:52.311395+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `12`; crypto_alt avg `-0.2666` n `228`; crypto_major avg `-0.1369` n `8`; equity avg `0.041` n `69`; fx avg `-0.0038` n `6`; index avg `0.0283` n `23`; metal avg `-0.0183` n `18`; unknown avg `0.4328` n `421`
- 1h: commodity avg `0.0988` n `12`; crypto_alt avg `-0.8205` n `228`; crypto_major avg `-0.8299` n `8`; equity avg `-0.4212` n `69`; fx avg `0.005` n `6`; index avg `0.0737` n `23`; metal avg `0.227` n `18`; unknown avg `0.2189` n `421`
- 4h: commodity avg `-0.017` n `12`; crypto_alt avg `0.1365` n `228`; crypto_major avg `-0.4036` n `8`; equity avg `-0.0071` n `69`; fx avg `0.0769` n `6`; index avg `0.1028` n `23`; metal avg `0.6672` n `18`; unknown avg `0.725` n `421`
- 24h: commodity avg `1.0451` n `12`; crypto_alt avg `-0.0779` n `228`; crypto_major avg `-0.8298` n `8`; equity avg `0.5296` n `69`; fx avg `0.0412` n `6`; index avg `0.3433` n `23`; metal avg `0.2401` n `18`; unknown avg `1.3646` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2846`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2552`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
