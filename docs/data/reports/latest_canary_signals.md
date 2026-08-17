# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T00:37:25.429129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0274` n `12`; crypto_alt avg `-0.0198` n `230`; crypto_major avg `-0.0141` n `8`; equity avg `-0.0149` n `114`; fx avg `0.002` n `6`; index avg `-0.0121` n `25`; metal avg `0.0083` n `20`; unknown avg `-0.0277` n `792`
- 1h: commodity avg `-0.0429` n `12`; crypto_alt avg `-0.0871` n `230`; crypto_major avg `-0.0646` n `8`; equity avg `-0.0006` n `114`; fx avg `-0.0102` n `6`; index avg `-0.0079` n `25`; metal avg `0.1101` n `20`; unknown avg `-0.1441` n `792`
- 4h: commodity avg `-0.1994` n `12`; crypto_alt avg `-0.8758` n `230`; crypto_major avg `-0.6514` n `8`; equity avg `-0.0238` n `114`; fx avg `-0.0219` n `6`; index avg `0.0052` n `25`; metal avg `0.0861` n `20`; unknown avg `0.0394` n `791`
- 24h: commodity avg `-0.1097` n `12`; crypto_alt avg `-0.829` n `230`; crypto_major avg `-0.4869` n `8`; equity avg `0.2404` n `114`; fx avg `-0.0227` n `6`; index avg `0.0387` n `25`; metal avg `0.112` n `20`; unknown avg `0.0004` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1666`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
