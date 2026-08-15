# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T11:52:34.065361+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `0.0322` n `230`; crypto_major avg `0.005` n `8`; equity avg `0.0203` n `114`; fx avg `0.0016` n `6`; index avg `-0.0004` n `25`; metal avg `-0.0059` n `20`; unknown avg `-0.0354` n `791`
- 1h: commodity avg `0.1007` n `12`; crypto_alt avg `0.0089` n `230`; crypto_major avg `-0.0259` n `8`; equity avg `0.0259` n `114`; fx avg `-0.031` n `6`; index avg `0.0001` n `25`; metal avg `0.004` n `20`; unknown avg `-0.0032` n `791`
- 4h: commodity avg `0.0911` n `12`; crypto_alt avg `0.0691` n `230`; crypto_major avg `-0.1217` n `8`; equity avg `0.0136` n `114`; fx avg `-0.0059` n `6`; index avg `-0.0066` n `25`; metal avg `0.0113` n `20`; unknown avg `-0.0678` n `791`
- 24h: commodity avg `0.0984` n `12`; crypto_alt avg `1.0802` n `230`; crypto_major avg `0.1087` n `8`; equity avg `-0.736` n `114`; fx avg `0.1127` n `6`; index avg `-0.1602` n `25`; metal avg `0.119` n `20`; unknown avg `-0.1017` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1834`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
