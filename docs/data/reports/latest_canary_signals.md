# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T06:55:04.746695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0346` n `12`; crypto_alt avg `0.0437` n `230`; crypto_major avg `0.0732` n `8`; equity avg `0.0461` n `114`; fx avg `-0.0006` n `6`; index avg `0.0044` n `25`; metal avg `0.0134` n `20`; unknown avg `-0.02` n `791`
- 1h: commodity avg `-0.0728` n `12`; crypto_alt avg `0.0523` n `230`; crypto_major avg `0.1003` n `8`; equity avg `0.0265` n `114`; fx avg `-0.0018` n `6`; index avg `0.0052` n `25`; metal avg `0.0083` n `20`; unknown avg `-0.0697` n `765`
- 4h: commodity avg `-0.0305` n `12`; crypto_alt avg `0.2486` n `230`; crypto_major avg `-0.038` n `8`; equity avg `-0.0053` n `114`; fx avg `-0.0416` n `6`; index avg `-0.0239` n `25`; metal avg `-0.0248` n `20`; unknown avg `-0.043` n `759`
- 24h: commodity avg `-0.0354` n `12`; crypto_alt avg `0.9575` n `230`; crypto_major avg `0.1513` n `8`; equity avg `-0.1004` n `114`; fx avg `0.1077` n `6`; index avg `-0.07` n `25`; metal avg `0.3158` n `20`; unknown avg `-0.1838` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2158`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
