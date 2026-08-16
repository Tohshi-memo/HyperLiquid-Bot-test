# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T09:37:13.042852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `12`; crypto_alt avg `0.0298` n `230`; crypto_major avg `-0.0258` n `8`; equity avg `0.0007` n `114`; fx avg `0.0007` n `6`; index avg `-0.0013` n `25`; metal avg `0.0048` n `20`; unknown avg `-0.0454` n `791`
- 1h: commodity avg `-0.0106` n `12`; crypto_alt avg `0.09` n `230`; crypto_major avg `0.0059` n `8`; equity avg `0.0038` n `114`; fx avg `0.0029` n `6`; index avg `0.0043` n `25`; metal avg `-0.0048` n `20`; unknown avg `0.0022` n `791`
- 4h: commodity avg `0.0025` n `12`; crypto_alt avg `0.4196` n `230`; crypto_major avg `0.1482` n `8`; equity avg `0.1008` n `114`; fx avg `0.0044` n `6`; index avg `0.0158` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.0465` n `759`
- 24h: commodity avg `0.0916` n `12`; crypto_alt avg `0.1085` n `230`; crypto_major avg `0.2258` n `8`; equity avg `0.4018` n `114`; fx avg `-0.0074` n `6`; index avg `0.0583` n `25`; metal avg `0.0211` n `20`; unknown avg `-0.0089` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2059`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
