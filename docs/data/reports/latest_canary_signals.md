# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T22:52:26.333562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `12`; crypto_alt avg `-0.0016` n `230`; crypto_major avg `0.0123` n `8`; equity avg `-0.0075` n `114`; fx avg `0.0028` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.001` n `791`
- 1h: commodity avg `0.0221` n `12`; crypto_alt avg `0.1504` n `230`; crypto_major avg `0.0823` n `8`; equity avg `0.0098` n `114`; fx avg `0.0032` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0059` n `20`; unknown avg `2.5332` n `791`
- 4h: commodity avg `-0.009` n `12`; crypto_alt avg `0.188` n `230`; crypto_major avg `0.1281` n `8`; equity avg `0.1901` n `114`; fx avg `0.0064` n `6`; index avg `0.0221` n `25`; metal avg `0.0297` n `20`; unknown avg `-0.0632` n `791`
- 24h: commodity avg `0.2451` n `12`; crypto_alt avg `0.1947` n `230`; crypto_major avg `-1.0343` n `8`; equity avg `-0.5738` n `114`; fx avg `0.08` n `6`; index avg `-0.0947` n `25`; metal avg `0.2291` n `20`; unknown avg `-0.0778` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
