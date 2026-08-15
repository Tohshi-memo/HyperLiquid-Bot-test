# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T08:49:56.165489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0325` n `12`; crypto_alt avg `0.0614` n `230`; crypto_major avg `-0.0119` n `8`; equity avg `-0.0075` n `114`; fx avg `0.0048` n `6`; index avg `0.0011` n `25`; metal avg `-0.008` n `20`; unknown avg `-0.0024` n `791`
- 1h: commodity avg `0.0051` n `12`; crypto_alt avg `0.1106` n `230`; crypto_major avg `-0.1019` n `8`; equity avg `0.0008` n `114`; fx avg `0.0058` n `6`; index avg `-0.0023` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.0448` n `791`
- 4h: commodity avg `-0.1922` n `12`; crypto_alt avg `0.1802` n `230`; crypto_major avg `-0.2468` n `8`; equity avg `-0.0327` n `114`; fx avg `0.0004` n `6`; index avg `-0.0054` n `25`; metal avg `-0.0036` n `20`; unknown avg `-0.1265` n `759`
- 24h: commodity avg `-0.2001` n `12`; crypto_alt avg `0.9704` n `230`; crypto_major avg `-0.1247` n `8`; equity avg `-0.4016` n `114`; fx avg `0.1556` n `6`; index avg `-0.1087` n `25`; metal avg `0.2278` n `20`; unknown avg `-0.1295` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
