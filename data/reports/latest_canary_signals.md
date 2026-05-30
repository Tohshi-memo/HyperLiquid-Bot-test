# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T15:42:45.149542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0841` n `12`; crypto_alt avg `-0.1825` n `228`; crypto_major avg `-0.2077` n `8`; equity avg `-0.0533` n `69`; fx avg `0.0014` n `6`; index avg `-0.0811` n `23`; metal avg `0.0295` n `18`; unknown avg `0.0089` n `421`
- 1h: commodity avg `0.0655` n `12`; crypto_alt avg `-0.407` n `228`; crypto_major avg `-0.2376` n `8`; equity avg `-0.0605` n `69`; fx avg `0.0038` n `6`; index avg `-0.1102` n `23`; metal avg `0.0078` n `18`; unknown avg `-0.1671` n `421`
- 4h: commodity avg `0.2662` n `12`; crypto_alt avg `-0.1006` n `228`; crypto_major avg `0.4018` n `8`; equity avg `0.3578` n `69`; fx avg `0.0282` n `6`; index avg `0.0603` n `23`; metal avg `-0.0082` n `18`; unknown avg `0.0399` n `421`
- 24h: commodity avg `0.3228` n `12`; crypto_alt avg `0.0512` n `228`; crypto_major avg `1.1165` n `8`; equity avg `1.1036` n `69`; fx avg `0.0028` n `6`; index avg `0.2598` n `23`; metal avg `-0.3306` n `18`; unknown avg `-0.1307` n `400`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1919`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
