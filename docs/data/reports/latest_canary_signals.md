# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T09:22:30.085488+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0222` n `12`; crypto_alt avg `0.1472` n `230`; crypto_major avg `0.0799` n `8`; equity avg `0.0172` n `114`; fx avg `0.0031` n `6`; index avg `0.0092` n `25`; metal avg `0.0034` n `20`; unknown avg `-0.0297` n `791`
- 1h: commodity avg `0.0219` n `12`; crypto_alt avg `0.1293` n `230`; crypto_major avg `-0.1237` n `8`; equity avg `-0.0106` n `114`; fx avg `-0.0083` n `6`; index avg `0.0125` n `25`; metal avg `0.001` n `20`; unknown avg `-0.0182` n `791`
- 4h: commodity avg `-0.1697` n `12`; crypto_alt avg `-0.0427` n `230`; crypto_major avg `-0.2369` n `8`; equity avg `-0.0223` n `114`; fx avg `-0.0056` n `6`; index avg `0.0049` n `25`; metal avg `0.0089` n `20`; unknown avg `-0.0326` n `759`
- 24h: commodity avg `-0.1035` n `12`; crypto_alt avg `0.9504` n `230`; crypto_major avg `-0.1558` n `8`; equity avg `-0.4065` n `114`; fx avg `0.1624` n `6`; index avg `-0.1011` n `25`; metal avg `0.202` n `20`; unknown avg `-0.1508` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1778`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
