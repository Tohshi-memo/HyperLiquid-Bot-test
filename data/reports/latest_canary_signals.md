# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T03:50:21.254163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.034` n `12`; crypto_alt avg `-0.0564` n `230`; crypto_major avg `-0.0392` n `8`; equity avg `0.0024` n `114`; fx avg `-0.0164` n `6`; index avg `-0.0077` n `25`; metal avg `-0.002` n `20`; unknown avg `0.1439` n `791`
- 1h: commodity avg `0.0104` n `12`; crypto_alt avg `-0.1362` n `230`; crypto_major avg `-0.0183` n `8`; equity avg `0.0313` n `114`; fx avg `-0.0331` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0245` n `20`; unknown avg `0.0052` n `791`
- 4h: commodity avg `-0.0211` n `12`; crypto_alt avg `-0.0531` n `230`; crypto_major avg `0.1791` n `8`; equity avg `0.0544` n `114`; fx avg `0.0578` n `6`; index avg `0.0019` n `25`; metal avg `-0.0093` n `20`; unknown avg `0.1905` n `791`
- 24h: commodity avg `0.1871` n `12`; crypto_alt avg `0.3535` n `230`; crypto_major avg `-0.1356` n `8`; equity avg `-0.1221` n `114`; fx avg `0.1697` n `6`; index avg `-0.0353` n `25`; metal avg `0.3996` n `20`; unknown avg `0.0442` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
