# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T16:52:29.565918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-3.3104` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0844` n `13`; crypto_alt avg `-0.1662` n `239`; crypto_major avg `0.0091` n `8`; equity avg `0.4481` n `160`; fx avg `-0.0013` n `6`; index avg `0.0358` n `27`; metal avg `-0.0498` n `20`; unknown avg `0.7531` n `1261`
- 1h: commodity avg `-0.0334` n `13`; crypto_alt avg `-0.8694` n `239`; crypto_major avg `-0.6995` n `8`; equity avg `-0.0026` n `160`; fx avg `0.0064` n `6`; index avg `0.0024` n `27`; metal avg `-0.0888` n `20`; unknown avg `-0.1931` n `1249`
- 4h: commodity avg `0.2391` n `13`; crypto_alt avg `0.2364` n `239`; crypto_major avg `0.3328` n `8`; equity avg `3.6432` n `160`; fx avg `-0.0015` n `6`; index avg `0.3629` n `27`; metal avg `0.0159` n `20`; unknown avg `23.6935` n `1249`
- 24h: commodity avg `-0.2964` n `13`; crypto_alt avg `0.8175` n `239`; crypto_major avg `-2.1373` n `8`; equity avg `4.0815` n `160`; fx avg `-0.1581` n `6`; index avg `0.4379` n `27`; metal avg `0.3867` n `20`; unknown avg `6.3115` n `1026`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
