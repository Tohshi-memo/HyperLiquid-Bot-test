# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T02:22:25.828922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0457` n `12`; crypto_alt avg `-0.1` n `233`; crypto_major avg `-0.0437` n `8`; equity avg `-0.016` n `136`; fx avg `-0.0031` n `6`; index avg `0.0118` n `26`; metal avg `0.014` n `20`; unknown avg `-0.0492` n `790`
- 1h: commodity avg `0.0159` n `12`; crypto_alt avg `-0.173` n `233`; crypto_major avg `0.016` n `8`; equity avg `-0.0278` n `136`; fx avg `-0.0074` n `6`; index avg `0.0142` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.2054` n `788`
- 4h: commodity avg `-0.2308` n `12`; crypto_alt avg `-0.9197` n `233`; crypto_major avg `-0.6942` n `8`; equity avg `-0.0937` n `136`; fx avg `-0.0334` n `6`; index avg `0.0294` n `26`; metal avg `0.0033` n `20`; unknown avg `1478.4084` n `762`
- 24h: commodity avg `1.0708` n `12`; crypto_alt avg `-1.5099` n `233`; crypto_major avg `-1.9423` n `8`; equity avg `-1.62` n `136`; fx avg `0.115` n `6`; index avg `-0.2692` n `26`; metal avg `-1.2699` n `20`; unknown avg `-0.9108` n `677`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
