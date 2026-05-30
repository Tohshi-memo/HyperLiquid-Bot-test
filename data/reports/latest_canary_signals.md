# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T23:07:20.707010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0201` n `12`; crypto_alt avg `0.2023` n `228`; crypto_major avg `0.112` n `8`; equity avg `0.0609` n `69`; fx avg `-0.0162` n `6`; index avg `-0.058` n `23`; metal avg `-0.008` n `18`; unknown avg `-0.1601` n `421`
- 1h: commodity avg `0.0266` n `12`; crypto_alt avg `-0.0646` n `228`; crypto_major avg `0.2329` n `8`; equity avg `0.1412` n `69`; fx avg `-0.0136` n `6`; index avg `0.0132` n `23`; metal avg `-0.0121` n `18`; unknown avg `-0.364` n `421`
- 4h: commodity avg `0.1554` n `12`; crypto_alt avg `-0.6361` n `228`; crypto_major avg `-0.3265` n `8`; equity avg `0.2628` n `69`; fx avg `-0.0176` n `6`; index avg `-0.0081` n `23`; metal avg `-0.0227` n `18`; unknown avg `-0.5975` n `421`
- 24h: commodity avg `-0.1444` n `12`; crypto_alt avg `1.0523` n `228`; crypto_major avg `2.5519` n `8`; equity avg `1.0911` n `69`; fx avg `0.0124` n `6`; index avg `0.0985` n `23`; metal avg `0.0156` n `18`; unknown avg `1.2066` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
