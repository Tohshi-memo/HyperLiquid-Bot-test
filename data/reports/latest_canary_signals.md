# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T08:37:23.129826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.1305` n `228`; crypto_major avg `-0.105` n `8`; equity avg `-0.0474` n `69`; fx avg `0.0025` n `6`; index avg `-0.0722` n `23`; metal avg `-0.017` n `18`; unknown avg `0.7545` n `421`
- 1h: commodity avg `0.0245` n `12`; crypto_alt avg `0.2675` n `228`; crypto_major avg `0.1399` n `8`; equity avg `-0.0216` n `69`; fx avg `-0.0085` n `6`; index avg `-0.0367` n `23`; metal avg `0.0005` n `18`; unknown avg `0.8043` n `421`
- 4h: commodity avg `0.0982` n `12`; crypto_alt avg `-0.5933` n `228`; crypto_major avg `-0.6352` n `8`; equity avg `0.3689` n `69`; fx avg `0.0023` n `6`; index avg `-0.0504` n `23`; metal avg `-0.0022` n `18`; unknown avg `0.751` n `401`
- 24h: commodity avg `0.2413` n `12`; crypto_alt avg `0.2097` n `228`; crypto_major avg `1.6627` n `8`; equity avg `1.1957` n `69`; fx avg `0.2311` n `6`; index avg `-0.0073` n `23`; metal avg `0.0365` n `18`; unknown avg `1.6989` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
