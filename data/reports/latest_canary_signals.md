# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T11:07:30.519324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `12`; crypto_alt avg `0.0116` n `230`; crypto_major avg `0.0222` n `8`; equity avg `-0.0144` n `114`; fx avg `0.0` n `6`; index avg `0.0001` n `25`; metal avg `-0.0051` n `20`; unknown avg `-0.0659` n `791`
- 1h: commodity avg `0.0046` n `12`; crypto_alt avg `-0.012` n `230`; crypto_major avg `0.0356` n `8`; equity avg `-0.0229` n `114`; fx avg `0.0002` n `6`; index avg `-0.0026` n `25`; metal avg `-0.0044` n `20`; unknown avg `0.0591` n `791`
- 4h: commodity avg `0.0153` n `12`; crypto_alt avg `0.387` n `230`; crypto_major avg `0.0621` n `8`; equity avg `-0.0518` n `114`; fx avg `0.0032` n `6`; index avg `-0.0077` n `25`; metal avg `0.0017` n `20`; unknown avg `0.0426` n `791`
- 24h: commodity avg `0.1133` n `12`; crypto_alt avg `0.0887` n `230`; crypto_major avg `0.1546` n `8`; equity avg `0.3554` n `114`; fx avg `-0.0058` n `6`; index avg `0.0511` n `25`; metal avg `0.0203` n `20`; unknown avg `0.0905` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.21`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
