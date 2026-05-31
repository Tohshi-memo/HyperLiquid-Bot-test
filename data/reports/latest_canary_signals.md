# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T01:07:18.181392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0472` n `12`; crypto_alt avg `0.0593` n `228`; crypto_major avg `0.2681` n `8`; equity avg `0.0235` n `69`; fx avg `0.0143` n `6`; index avg `0.0242` n `23`; metal avg `0.0076` n `18`; unknown avg `-0.0694` n `421`
- 1h: commodity avg `0.0695` n `12`; crypto_alt avg `0.3871` n `228`; crypto_major avg `0.4355` n `8`; equity avg `0.0471` n `69`; fx avg `-0.0016` n `6`; index avg `0.0029` n `23`; metal avg `-0.0041` n `18`; unknown avg `-0.2637` n `421`
- 4h: commodity avg `0.0861` n `12`; crypto_alt avg `-0.3846` n `228`; crypto_major avg `0.3385` n `8`; equity avg `0.1687` n `69`; fx avg `-0.0087` n `6`; index avg `0.038` n `23`; metal avg `-0.0326` n `18`; unknown avg `-0.5292` n `421`
- 24h: commodity avg `-0.1849` n `12`; crypto_alt avg `0.6785` n `228`; crypto_major avg `2.6478` n `8`; equity avg `1.0277` n `69`; fx avg `0.029` n `6`; index avg `0.0987` n `23`; metal avg `0.0148` n `18`; unknown avg `0.2972` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
