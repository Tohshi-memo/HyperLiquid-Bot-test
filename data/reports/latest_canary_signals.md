# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T00:07:29.425408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `0.0375` n `230`; crypto_major avg `-0.0246` n `8`; equity avg `-0.0446` n `114`; fx avg `0.0001` n `6`; index avg `-0.0032` n `25`; metal avg `0.0134` n `20`; unknown avg `-0.1181` n `791`
- 1h: commodity avg `0.0558` n `12`; crypto_alt avg `0.2016` n `230`; crypto_major avg `0.2182` n `8`; equity avg `-0.049` n `114`; fx avg `-0.0238` n `6`; index avg `-0.0062` n `25`; metal avg `0.036` n `20`; unknown avg `0.029` n `791`
- 4h: commodity avg `0.069` n `12`; crypto_alt avg `0.3417` n `230`; crypto_major avg `0.2776` n `8`; equity avg `0.0006` n `114`; fx avg `-0.0149` n `6`; index avg `-0.0018` n `25`; metal avg `0.0751` n `20`; unknown avg `0.8494` n `791`
- 24h: commodity avg `0.2303` n `12`; crypto_alt avg `0.1162` n `230`; crypto_major avg `-0.7251` n `8`; equity avg `-0.6117` n `114`; fx avg `0.0669` n `6`; index avg `-0.133` n `25`; metal avg `0.2633` n `20`; unknown avg `-0.1203` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
