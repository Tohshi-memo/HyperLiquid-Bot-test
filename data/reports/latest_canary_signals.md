# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T22:07:19.366420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0159` n `12`; crypto_alt avg `-0.6637` n `228`; crypto_major avg `-0.4616` n `8`; equity avg `-0.1097` n `69`; fx avg `-0.0002` n `6`; index avg `0.0015` n `23`; metal avg `-0.0245` n `18`; unknown avg `0.8487` n `421`
- 1h: commodity avg `0.0575` n `12`; crypto_alt avg `-0.6332` n `228`; crypto_major avg `-0.4329` n `8`; equity avg `-0.0802` n `69`; fx avg `-0.0002` n `6`; index avg `0.0077` n `23`; metal avg `-0.0185` n `18`; unknown avg `0.8946` n `421`
- 4h: commodity avg `0.1278` n `12`; crypto_alt avg `-0.4353` n `228`; crypto_major avg `-0.4078` n `8`; equity avg `0.1612` n `69`; fx avg `0.0072` n `6`; index avg `-0.0174` n `23`; metal avg `-0.0209` n `18`; unknown avg `0.8168` n `421`
- 24h: commodity avg `0.0301` n `12`; crypto_alt avg `1.6028` n `228`; crypto_major avg `2.5636` n `8`; equity avg `0.9895` n `69`; fx avg `0.0274` n `6`; index avg `0.0368` n `23`; metal avg `0.0931` n `18`; unknown avg `0.3798` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
