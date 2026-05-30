# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T19:52:21.938320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `0.0477` n `228`; crypto_major avg `0.0073` n `8`; equity avg `0.0255` n `69`; fx avg `0.0012` n `6`; index avg `0.0261` n `23`; metal avg `-0.003` n `18`; unknown avg `0.8641` n `421`
- 1h: commodity avg `0.0113` n `12`; crypto_alt avg `-0.1201` n `228`; crypto_major avg `0.0333` n `8`; equity avg `0.0934` n `69`; fx avg `0.0117` n `6`; index avg `0.052` n `23`; metal avg `-0.017` n `18`; unknown avg `0.9741` n `421`
- 4h: commodity avg `-0.3652` n `12`; crypto_alt avg `0.3482` n `228`; crypto_major avg `0.6436` n `8`; equity avg `0.0278` n `69`; fx avg `-0.0105` n `6`; index avg `-0.0034` n `23`; metal avg `-0.0054` n `18`; unknown avg `0.5164` n `421`
- 24h: commodity avg `-0.1091` n `12`; crypto_alt avg `1.5781` n `228`; crypto_major avg `2.526` n `8`; equity avg `0.9848` n `69`; fx avg `-0.0038` n `6`; index avg `0.1175` n `23`; metal avg `-0.059` n `18`; unknown avg `0.2548` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1882`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
