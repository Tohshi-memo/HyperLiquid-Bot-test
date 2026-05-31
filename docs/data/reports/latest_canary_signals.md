# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T13:22:19.490126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `12`; crypto_alt avg `0.1749` n `228`; crypto_major avg `0.3772` n `8`; equity avg `0.0605` n `69`; fx avg `0.0005` n `6`; index avg `0.0287` n `23`; metal avg `0.0022` n `18`; unknown avg `0.1811` n `421`
- 1h: commodity avg `0.0467` n `12`; crypto_alt avg `0.167` n `228`; crypto_major avg `0.3822` n `8`; equity avg `0.0315` n `69`; fx avg `-0.0031` n `6`; index avg `-0.0024` n `23`; metal avg `-0.0033` n `18`; unknown avg `-0.1166` n `421`
- 4h: commodity avg `0.1236` n `12`; crypto_alt avg `0.264` n `228`; crypto_major avg `0.2578` n `8`; equity avg `-0.0049` n `69`; fx avg `-0.0159` n `6`; index avg `-0.0466` n `23`; metal avg `-0.0063` n `18`; unknown avg `-0.2897` n `421`
- 24h: commodity avg `0.1443` n `12`; crypto_alt avg `0.2586` n `228`; crypto_major avg `1.3788` n `8`; equity avg `0.8444` n `69`; fx avg `0.0019` n `6`; index avg `-0.2046` n `23`; metal avg `-0.037` n `18`; unknown avg `0.7745` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
