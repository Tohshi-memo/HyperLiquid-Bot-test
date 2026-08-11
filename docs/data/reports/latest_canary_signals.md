# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T17:22:30.607016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0281` n `12`; crypto_alt avg `0.0298` n `230`; crypto_major avg `0.0819` n `8`; equity avg `0.0024` n `113`; fx avg `-0.003` n `6`; index avg `-0.0038` n `25`; metal avg `-0.0293` n `20`; unknown avg `0.0196` n `785`
- 1h: commodity avg `0.0969` n `12`; crypto_alt avg `-0.0225` n `230`; crypto_major avg `-0.0146` n `8`; equity avg `-0.1439` n `113`; fx avg `-0.0132` n `6`; index avg `-0.0599` n `25`; metal avg `-0.0568` n `20`; unknown avg `-0.1099` n `785`
- 4h: commodity avg `0.2535` n `12`; crypto_alt avg `-1.1113` n `230`; crypto_major avg `-0.6513` n `8`; equity avg `-0.1493` n `113`; fx avg `-0.0088` n `6`; index avg `-0.1146` n `25`; metal avg `-0.1526` n `20`; unknown avg `0.0114` n `785`
- 24h: commodity avg `0.2164` n `12`; crypto_alt avg `-1.9953` n `230`; crypto_major avg `-0.24` n `8`; equity avg `0.0638` n `113`; fx avg `-0.061` n `6`; index avg `0.0249` n `25`; metal avg `-0.0057` n `20`; unknown avg `-0.2853` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2004`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1996`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
