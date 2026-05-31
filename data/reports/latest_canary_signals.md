# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T11:22:17.329100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `-0.1606` n `228`; crypto_major avg `-0.0643` n `8`; equity avg `-0.0062` n `69`; fx avg `-0.0124` n `6`; index avg `-0.0258` n `23`; metal avg `-0.0064` n `18`; unknown avg `-0.0576` n `421`
- 1h: commodity avg `0.0187` n `12`; crypto_alt avg `0.3771` n `228`; crypto_major avg `0.0032` n `8`; equity avg `0.0029` n `69`; fx avg `-0.0372` n `6`; index avg `-0.0364` n `23`; metal avg `-0.006` n `18`; unknown avg `-0.1404` n `421`
- 4h: commodity avg `0.1025` n `12`; crypto_alt avg `-0.1396` n `228`; crypto_major avg `-0.3485` n `8`; equity avg `0.1008` n `69`; fx avg `-0.0581` n `6`; index avg `-0.0198` n `23`; metal avg `-0.0302` n `18`; unknown avg `-0.2493` n `421`
- 24h: commodity avg `0.2469` n `12`; crypto_alt avg `0.2952` n `228`; crypto_major avg `1.3136` n `8`; equity avg `1.0623` n `69`; fx avg `-0.0184` n `6`; index avg `-0.0729` n `23`; metal avg `-0.0963` n `18`; unknown avg `0.6457` n `401`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
