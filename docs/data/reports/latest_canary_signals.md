# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T08:52:30.210228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0395` n `12`; crypto_alt avg `0.0231` n `230`; crypto_major avg `-0.0452` n `8`; equity avg `-0.0084` n `114`; fx avg `-0.0001` n `6`; index avg `0.0033` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.0064` n `791`
- 1h: commodity avg `-0.0019` n `12`; crypto_alt avg `0.0769` n `230`; crypto_major avg `-0.1352` n `8`; equity avg `-0.0001` n `114`; fx avg `0.0009` n `6`; index avg `-0.0001` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.0462` n `791`
- 4h: commodity avg `-0.1991` n `12`; crypto_alt avg `0.1393` n `230`; crypto_major avg `-0.2801` n `8`; equity avg `-0.0336` n `114`; fx avg `-0.0045` n `6`; index avg `-0.0032` n `25`; metal avg `-0.0039` n `20`; unknown avg `-0.1285` n `759`
- 24h: commodity avg `-0.207` n `12`; crypto_alt avg `0.9149` n `230`; crypto_major avg `-0.1579` n `8`; equity avg `-0.4025` n `114`; fx avg `0.1507` n `6`; index avg `-0.1065` n `25`; metal avg `0.2275` n `20`; unknown avg `-0.1316` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
