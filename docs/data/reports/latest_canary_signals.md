# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T03:37:30.992639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `-0.1641` n `230`; crypto_major avg `-0.0937` n `8`; equity avg `0.0028` n `114`; fx avg `-0.0134` n `6`; index avg `0.0009` n `25`; metal avg `0.0004` n `20`; unknown avg `-0.1235` n `791`
- 1h: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.0414` n `230`; crypto_major avg `0.0861` n `8`; equity avg `0.0436` n `114`; fx avg `-0.0375` n `6`; index avg `0.0127` n `25`; metal avg `-0.0144` n `20`; unknown avg `0.1444` n `791`
- 4h: commodity avg `-0.0461` n `12`; crypto_alt avg `0.0104` n `230`; crypto_major avg `0.2343` n `8`; equity avg `0.0267` n `114`; fx avg `0.1259` n `6`; index avg `0.0052` n `25`; metal avg `-0.0017` n `20`; unknown avg `0.2027` n `791`
- 24h: commodity avg `0.1331` n `12`; crypto_alt avg `0.2906` n `230`; crypto_major avg `-0.2236` n `8`; equity avg `-0.1661` n `114`; fx avg `0.1993` n `6`; index avg `-0.0321` n `25`; metal avg `0.3631` n `20`; unknown avg `0.0027` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1905`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
