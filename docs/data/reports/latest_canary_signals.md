# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T14:11:14.900645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `0.2745` n `228`; crypto_major avg `0.2346` n `8`; equity avg `0.0449` n `69`; fx avg `0.0152` n `6`; index avg `0.0879` n `23`; metal avg `0.0102` n `18`; unknown avg `0.8318` n `421`
- 1h: commodity avg `0.076` n `12`; crypto_alt avg `0.0336` n `228`; crypto_major avg `0.2042` n `8`; equity avg `0.118` n `69`; fx avg `0.0` n `6`; index avg `0.0755` n `23`; metal avg `-0.0026` n `18`; unknown avg `-0.0468` n `421`
- 4h: commodity avg `0.3102` n `12`; crypto_alt avg `0.2883` n `228`; crypto_major avg `0.565` n `8`; equity avg `0.3375` n `69`; fx avg `0.0165` n `6`; index avg `0.1722` n `23`; metal avg `-0.0314` n `18`; unknown avg `0.807` n `421`
- 24h: commodity avg `-0.3334` n `12`; crypto_alt avg `2.773` n `228`; crypto_major avg `3.3929` n `8`; equity avg `1.4717` n `69`; fx avg `0.1018` n `6`; index avg `0.1528` n `23`; metal avg `-0.2569` n `18`; unknown avg `1.5162` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1919`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
