# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T13:37:18.933364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.0533` n `228`; crypto_major avg `-0.0666` n `8`; equity avg `0.0321` n `69`; fx avg `-0.0005` n `6`; index avg `0.0151` n `23`; metal avg `-0.0041` n `18`; unknown avg `-0.0763` n `421`
- 1h: commodity avg `0.0007` n `12`; crypto_alt avg `0.043` n `228`; crypto_major avg `0.2289` n `8`; equity avg `0.0394` n `69`; fx avg `-0.0036` n `6`; index avg `0.0104` n `23`; metal avg `-0.0083` n `18`; unknown avg `0.0453` n `421`
- 4h: commodity avg `0.1039` n `12`; crypto_alt avg `0.164` n `228`; crypto_major avg `0.2192` n `8`; equity avg `0.0344` n `69`; fx avg `-0.0171` n `6`; index avg `-0.0341` n `23`; metal avg `-0.003` n `18`; unknown avg `0.1021` n `421`
- 24h: commodity avg `0.1302` n `12`; crypto_alt avg `0.6086` n `228`; crypto_major avg `1.5398` n `8`; equity avg `0.8945` n `69`; fx avg `0.0014` n `6`; index avg `-0.1739` n `23`; metal avg `-0.03` n `18`; unknown avg `0.4533` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
