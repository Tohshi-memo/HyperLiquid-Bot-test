# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T06:40:06.002546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1284` n `12`; crypto_alt avg `-0.0076` n `230`; crypto_major avg `-0.0741` n `8`; equity avg `-0.1192` n `113`; fx avg `0.0181` n `6`; index avg `-0.0177` n `25`; metal avg `-0.0328` n `20`; unknown avg `-0.0545` n `785`
- 1h: commodity avg `0.2494` n `12`; crypto_alt avg `-0.1132` n `230`; crypto_major avg `-0.1383` n `8`; equity avg `-0.2406` n `113`; fx avg `0.0348` n `6`; index avg `-0.0479` n `25`; metal avg `-0.0239` n `20`; unknown avg `-0.055` n `753`
- 4h: commodity avg `0.2348` n `12`; crypto_alt avg `-0.2915` n `230`; crypto_major avg `-0.137` n `8`; equity avg `-0.2245` n `113`; fx avg `0.0185` n `6`; index avg `-0.0227` n `25`; metal avg `-0.3366` n `20`; unknown avg `-0.0539` n `753`
- 24h: commodity avg `1.2113` n `12`; crypto_alt avg `-1.0006` n `230`; crypto_major avg `-0.8948` n `8`; equity avg `-1.3291` n `113`; fx avg `0.0637` n `6`; index avg `-0.0286` n `25`; metal avg `0.0648` n `20`; unknown avg `0.1285` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
