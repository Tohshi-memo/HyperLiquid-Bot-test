# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T03:01:09.145106+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `0.0509` n `230`; crypto_major avg `0.0592` n `8`; equity avg `0.0011` n `114`; fx avg `-0.0038` n `6`; index avg `-0.0021` n `25`; metal avg `0.0017` n `20`; unknown avg `0.083` n `791`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `0.1424` n `230`; crypto_major avg `0.1895` n `8`; equity avg `0.011` n `114`; fx avg `0.0962` n `6`; index avg `0.0025` n `25`; metal avg `0.0091` n `20`; unknown avg `0.3666` n `791`
- 4h: commodity avg `0.0016` n `12`; crypto_alt avg `0.3152` n `230`; crypto_major avg `0.5006` n `8`; equity avg `0.0196` n `114`; fx avg `0.0633` n `6`; index avg `-0.0006` n `25`; metal avg `0.0396` n `20`; unknown avg `0.4094` n `791`
- 24h: commodity avg `0.1821` n `12`; crypto_alt avg `0.3268` n `230`; crypto_major avg `-0.228` n `8`; equity avg `-0.0776` n `114`; fx avg `0.2088` n `6`; index avg `-0.0188` n `25`; metal avg `0.4332` n `20`; unknown avg `-0.05` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2181`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
