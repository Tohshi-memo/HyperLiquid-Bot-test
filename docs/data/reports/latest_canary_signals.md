# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T14:07:21.021287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0192` n `12`; crypto_alt avg `-0.2099` n `228`; crypto_major avg `-0.0333` n `8`; equity avg `-0.0279` n `69`; fx avg `0.0018` n `6`; index avg `0.0105` n `23`; metal avg `0.0019` n `18`; unknown avg `-0.0658` n `421`
- 1h: commodity avg `0.0336` n `12`; crypto_alt avg `-0.3737` n `228`; crypto_major avg `0.0173` n `8`; equity avg `0.0614` n `69`; fx avg `-0.0003` n `6`; index avg `0.0557` n `23`; metal avg `-0.0146` n `18`; unknown avg `-0.1783` n `421`
- 4h: commodity avg `0.1829` n `12`; crypto_alt avg `-0.0595` n `228`; crypto_major avg `0.0702` n `8`; equity avg `0.0197` n `69`; fx avg `-0.0129` n `6`; index avg `-0.0129` n `23`; metal avg `0.0059` n `18`; unknown avg `-0.4898` n `421`
- 24h: commodity avg `0.0869` n `12`; crypto_alt avg `-0.3624` n `228`; crypto_major avg `0.8429` n `8`; equity avg `0.7936` n `69`; fx avg `-0.0147` n `6`; index avg `-0.2614` n `23`; metal avg `-0.053` n `18`; unknown avg `0.2142` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
