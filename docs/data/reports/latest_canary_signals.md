# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T00:37:26.947058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `12`; crypto_alt avg `0.0351` n `230`; crypto_major avg `0.0223` n `8`; equity avg `-0.0038` n `114`; fx avg `-0.0037` n `6`; index avg `0.0009` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.0248` n `791`
- 1h: commodity avg `-0.0046` n `12`; crypto_alt avg `0.1014` n `230`; crypto_major avg `-0.0311` n `8`; equity avg `0.0009` n `114`; fx avg `0.0009` n `6`; index avg `0.0` n `25`; metal avg `0.0011` n `20`; unknown avg `-0.0524` n `791`
- 4h: commodity avg `-0.0341` n `12`; crypto_alt avg `-0.2391` n `230`; crypto_major avg `-0.1818` n `8`; equity avg `-0.0005` n `114`; fx avg `-0.0043` n `6`; index avg `0.0141` n `25`; metal avg `-0.0027` n `20`; unknown avg `0.1491` n `791`
- 24h: commodity avg `-0.1219` n `12`; crypto_alt avg `0.1791` n `230`; crypto_major avg `0.061` n `8`; equity avg `0.2074` n `114`; fx avg `0.0342` n `6`; index avg `0.0164` n `25`; metal avg `-0.0615` n `20`; unknown avg `0.1056` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2226`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1749`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
