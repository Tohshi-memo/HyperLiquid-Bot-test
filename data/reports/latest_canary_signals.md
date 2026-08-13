# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T15:52:33.428080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0664` n `12`; crypto_alt avg `-0.2144` n `230`; crypto_major avg `-0.1191` n `8`; equity avg `-0.3287` n `113`; fx avg `-0.004` n `6`; index avg `-0.0158` n `25`; metal avg `0.0403` n `20`; unknown avg `-0.0336` n `787`
- 1h: commodity avg `0.3036` n `12`; crypto_alt avg `-0.4684` n `230`; crypto_major avg `-0.3719` n `8`; equity avg `-0.503` n `113`; fx avg `0.0008` n `6`; index avg `-0.0557` n `25`; metal avg `-0.0756` n `20`; unknown avg `0.1416` n `787`
- 4h: commodity avg `0.1669` n `12`; crypto_alt avg `0.1899` n `230`; crypto_major avg `0.3021` n `8`; equity avg `1.1001` n `113`; fx avg `-0.0219` n `6`; index avg `0.2181` n `25`; metal avg `-0.1092` n `20`; unknown avg `-0.0455` n `787`
- 24h: commodity avg `-0.2402` n `12`; crypto_alt avg `-0.2238` n `230`; crypto_major avg `0.0481` n `8`; equity avg `1.4209` n `113`; fx avg `0.0039` n `6`; index avg `0.2979` n `25`; metal avg `-0.4762` n `20`; unknown avg `0.1966` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2278`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1995`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1958`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
