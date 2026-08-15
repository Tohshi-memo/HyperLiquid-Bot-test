# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T05:22:27.373747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `0.1446` n `230`; crypto_major avg `-0.0685` n `8`; equity avg `-0.024` n `114`; fx avg `0.0108` n `6`; index avg `-0.0` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.1604` n `791`
- 1h: commodity avg `0.024` n `12`; crypto_alt avg `0.2691` n `230`; crypto_major avg `-0.091` n `8`; equity avg `-0.0493` n `114`; fx avg `0.0005` n `6`; index avg `-0.015` n `25`; metal avg `0.0037` n `20`; unknown avg `-0.2482` n `791`
- 4h: commodity avg `0.0739` n `12`; crypto_alt avg `0.5085` n `230`; crypto_major avg `0.1626` n `8`; equity avg `0.0435` n `114`; fx avg `0.0633` n `6`; index avg `-0.0049` n `25`; metal avg `-0.0336` n `20`; unknown avg `-0.0222` n `791`
- 24h: commodity avg `0.1844` n `12`; crypto_alt avg `1.0411` n `230`; crypto_major avg `-0.2028` n `8`; equity avg `0.0381` n `114`; fx avg `0.158` n `6`; index avg `-0.0313` n `25`; metal avg `0.4574` n `20`; unknown avg `-0.1258` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1914`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
