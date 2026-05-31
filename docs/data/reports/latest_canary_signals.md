# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T13:52:21.036753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0296` n `12`; crypto_alt avg `-0.285` n `228`; crypto_major avg `-0.2586` n `8`; equity avg `-0.0035` n `69`; fx avg `-0.0021` n `6`; index avg `0.0015` n `23`; metal avg `-0.0146` n `18`; unknown avg `-0.1653` n `421`
- 1h: commodity avg `0.03` n `12`; crypto_alt avg `-0.1568` n `228`; crypto_major avg `0.0413` n `8`; equity avg `0.0272` n `69`; fx avg `-0.0057` n `6`; index avg `0.0362` n `23`; metal avg `-0.016` n `18`; unknown avg `-0.1533` n `421`
- 4h: commodity avg `0.1884` n `12`; crypto_alt avg `-0.1493` n `228`; crypto_major avg `-0.0353` n `8`; equity avg `0.022` n `69`; fx avg `-0.0192` n `6`; index avg `-0.0243` n `23`; metal avg `-0.0066` n `18`; unknown avg `-0.2647` n `421`
- 24h: commodity avg `0.1131` n `12`; crypto_alt avg `0.1194` n `228`; crypto_major avg `1.1154` n `8`; equity avg `0.8671` n `69`; fx avg `-0.0013` n `6`; index avg `-0.1845` n `23`; metal avg `-0.0446` n `18`; unknown avg `0.486` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
