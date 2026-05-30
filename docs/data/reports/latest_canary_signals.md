# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T21:37:24.304789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0714` n `12`; crypto_alt avg `0.0186` n `228`; crypto_major avg `0.0264` n `8`; equity avg `0.0299` n `69`; fx avg `0.0` n `6`; index avg `-0.0562` n `23`; metal avg `-0.008` n `18`; unknown avg `-0.0708` n `421`
- 1h: commodity avg `0.0729` n `12`; crypto_alt avg `0.0908` n `228`; crypto_major avg `0.1496` n `8`; equity avg `0.0928` n `69`; fx avg `-0.0037` n `6`; index avg `0.023` n `23`; metal avg `-0.0084` n `18`; unknown avg `0.1893` n `421`
- 4h: commodity avg `0.1283` n `12`; crypto_alt avg `0.7154` n `228`; crypto_major avg `0.5944` n `8`; equity avg `0.3126` n `69`; fx avg `0.0062` n `6`; index avg `0.0378` n `23`; metal avg `-0.0056` n `18`; unknown avg `-0.0511` n `421`
- 24h: commodity avg `0.0526` n `12`; crypto_alt avg `2.0002` n `228`; crypto_major avg `2.9767` n `8`; equity avg `0.9902` n `69`; fx avg `0.03` n `6`; index avg `0.1333` n `23`; metal avg `0.1126` n `18`; unknown avg `0.3937` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1838`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
