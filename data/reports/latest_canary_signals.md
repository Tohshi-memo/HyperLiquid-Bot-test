# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T22:37:51.965704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0242` n `12`; crypto_alt avg `0.0174` n `230`; crypto_major avg `-0.0179` n `8`; equity avg `-0.0177` n `114`; fx avg `-0.0097` n `6`; index avg `-0.0002` n `25`; metal avg `0.0033` n `20`; unknown avg `0.117` n `791`
- 1h: commodity avg `0.0418` n `12`; crypto_alt avg `0.0899` n `230`; crypto_major avg `0.0087` n `8`; equity avg `0.0355` n `114`; fx avg `-0.0009` n `6`; index avg `-0.005` n `25`; metal avg `0.0125` n `20`; unknown avg `0.6367` n `791`
- 4h: commodity avg `-0.0425` n `12`; crypto_alt avg `0.0707` n `230`; crypto_major avg `0.0083` n `8`; equity avg `0.2818` n `114`; fx avg `0.004` n `6`; index avg `0.039` n `25`; metal avg `0.0326` n `20`; unknown avg `8.7092` n `791`
- 24h: commodity avg `0.2401` n `12`; crypto_alt avg `0.1819` n `230`; crypto_major avg `-1.1394` n `8`; equity avg `-0.5438` n `114`; fx avg `0.0732` n `6`; index avg `-0.0933` n `25`; metal avg `0.2241` n `20`; unknown avg `-0.0877` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
