# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T10:22:17.572527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1153` n `12`; crypto_alt avg `-0.2762` n `228`; crypto_major avg `-0.0957` n `8`; equity avg `-0.0374` n `69`; fx avg `0.0025` n `6`; index avg `0.05` n `23`; metal avg `0.005` n `18`; unknown avg `-0.2052` n `421`
- 1h: commodity avg `0.0733` n `12`; crypto_alt avg `-0.5023` n `228`; crypto_major avg `-0.2681` n `8`; equity avg `-0.0621` n `69`; fx avg `-0.0014` n `6`; index avg `0.0431` n `23`; metal avg `-0.0239` n `18`; unknown avg `-0.3698` n `421`
- 4h: commodity avg `0.1357` n `12`; crypto_alt avg `-0.8326` n `228`; crypto_major avg `-0.7574` n `8`; equity avg `0.1501` n `69`; fx avg `-0.0008` n `6`; index avg `-0.0513` n `23`; metal avg `-0.0119` n `18`; unknown avg `0.9658` n `421`
- 24h: commodity avg `0.3129` n `12`; crypto_alt avg `-0.4062` n `228`; crypto_major avg `1.1487` n `8`; equity avg `1.0568` n `69`; fx avg `0.0281` n `6`; index avg `-0.0311` n `23`; metal avg `-0.1097` n `18`; unknown avg `1.3398` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
