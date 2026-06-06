# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T01:22:22.481898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0539` n `12`; crypto_alt avg `-0.8371` n `228`; crypto_major avg `-0.7931` n `8`; equity avg `-0.3144` n `74`; fx avg `-0.0016` n `6`; index avg `-0.0889` n `23`; metal avg `-0.0274` n `18`; unknown avg `0.6906` n `425`
- 1h: commodity avg `0.1591` n `12`; crypto_alt avg `-0.5105` n `228`; crypto_major avg `-0.3493` n `8`; equity avg `-0.4539` n `74`; fx avg `-0.0084` n `6`; index avg `-0.1471` n `23`; metal avg `0.0359` n `18`; unknown avg `0.9745` n `425`
- 4h: commodity avg `0.2621` n `12`; crypto_alt avg `-1.0131` n `228`; crypto_major avg `-0.7699` n `8`; equity avg `-0.6658` n `74`; fx avg `0.0094` n `6`; index avg `0.0132` n `23`; metal avg `-0.1032` n `18`; unknown avg `1.2184` n `425`
- 24h: commodity avg `-1.0616` n `12`; crypto_alt avg `-5.8596` n `228`; crypto_major avg `-5.169` n `8`; equity avg `-5.1738` n `74`; fx avg `-0.1977` n `6`; index avg `-3.3762` n `23`; metal avg `-3.6976` n `18`; unknown avg `-0.5469` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
