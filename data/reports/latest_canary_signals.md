# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T06:22:14.425613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0606` n `12`; crypto_alt avg `0.1018` n `228`; crypto_major avg `0.0021` n `8`; equity avg `0.1227` n `66`; fx avg `-0.0021` n `6`; index avg `0.0584` n `23`; metal avg `0.217` n `18`; unknown avg `-0.0048` n `383`
- 1h: commodity avg `0.0006` n `12`; crypto_alt avg `0.568` n `228`; crypto_major avg `0.3777` n `8`; equity avg `0.2141` n `66`; fx avg `0.0233` n `6`; index avg `0.0711` n `23`; metal avg `0.3535` n `18`; unknown avg `0.0281` n `363`
- 4h: commodity avg `0.2364` n `12`; crypto_alt avg `0.2052` n `228`; crypto_major avg `0.2185` n `8`; equity avg `0.2866` n `66`; fx avg `0.0618` n `6`; index avg `0.1043` n `23`; metal avg `-0.0668` n `18`; unknown avg `0.2549` n `363`
- 24h: commodity avg `0.2036` n `12`; crypto_alt avg `1.8633` n `228`; crypto_major avg `1.0696` n `8`; equity avg `-0.6911` n `66`; fx avg `0.3298` n `6`; index avg `-0.2844` n `23`; metal avg `0.6653` n `18`; unknown avg `0.4767` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
