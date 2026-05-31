# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T14:54:15.682936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `-0.1491` n `228`; crypto_major avg `-0.1091` n `8`; equity avg `0.0188` n `69`; fx avg `0.0005` n `6`; index avg `-0.0359` n `23`; metal avg `-0.0131` n `18`; unknown avg `0.1835` n `421`
- 1h: commodity avg `0.0214` n `12`; crypto_alt avg `-0.9548` n `228`; crypto_major avg `-0.4943` n `8`; equity avg `-0.0911` n `69`; fx avg `-0.0019` n `6`; index avg `0.0124` n `23`; metal avg `-0.0003` n `18`; unknown avg `0.0282` n `421`
- 4h: commodity avg `0.0994` n `12`; crypto_alt avg `-0.8444` n `228`; crypto_major avg `-0.2707` n `8`; equity avg `0.0269` n `69`; fx avg `-0.0192` n `6`; index avg `-0.0365` n `23`; metal avg `-0.0058` n `18`; unknown avg `-0.1113` n `421`
- 24h: commodity avg `0.1355` n `12`; crypto_alt avg `-0.9879` n `228`; crypto_major avg `0.2191` n `8`; equity avg `0.659` n `69`; fx avg `-0.025` n `6`; index avg `-0.2932` n `23`; metal avg `-0.0467` n `18`; unknown avg `0.1967` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
