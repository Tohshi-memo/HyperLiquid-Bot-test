# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T17:22:31.756575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0332` n `12`; crypto_alt avg `0.0499` n `230`; crypto_major avg `0.1053` n `8`; equity avg `0.1966` n `100`; fx avg `-0.0008` n `6`; index avg `0.0393` n `25`; metal avg `-0.0058` n `20`; unknown avg `0.0669` n `772`
- 1h: commodity avg `0.0975` n `12`; crypto_alt avg `0.0517` n `230`; crypto_major avg `0.0804` n `8`; equity avg `0.0998` n `100`; fx avg `-0.0029` n `6`; index avg `-0.0133` n `25`; metal avg `0.0008` n `20`; unknown avg `0.0711` n `772`
- 4h: commodity avg `0.2182` n `12`; crypto_alt avg `-0.3176` n `230`; crypto_major avg `-0.7395` n `8`; equity avg `0.5511` n `100`; fx avg `-0.0137` n `6`; index avg `0.0144` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.1019` n `772`
- 24h: commodity avg `0.983` n `12`; crypto_alt avg `-1.5147` n `230`; crypto_major avg `-1.9143` n `8`; equity avg `-1.289` n `99`; fx avg `-0.0826` n `6`; index avg `-0.3635` n `25`; metal avg `-0.7957` n `20`; unknown avg `-0.0773` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0702`, n `666`, weak_sample_signal
