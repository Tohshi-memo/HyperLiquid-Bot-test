# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T16:52:15.748400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.285` n `12`; crypto_alt avg `0.2858` n `228`; crypto_major avg `0.2108` n `8`; equity avg `0.052` n `67`; fx avg `-0.0168` n `6`; index avg `0.0219` n `23`; metal avg `0.1013` n `18`; unknown avg `0.7681` n `405`
- 1h: commodity avg `-0.2696` n `12`; crypto_alt avg `0.4853` n `228`; crypto_major avg `0.1319` n `8`; equity avg `-0.0122` n `67`; fx avg `-0.0178` n `6`; index avg `-0.0713` n `23`; metal avg `0.1049` n `18`; unknown avg `-0.0462` n `405`
- 4h: commodity avg `-0.5474` n `12`; crypto_alt avg `1.1147` n `228`; crypto_major avg `0.1631` n `8`; equity avg `0.0853` n `67`; fx avg `-0.0446` n `6`; index avg `0.074` n `23`; metal avg `0.5556` n `18`; unknown avg `1.0241` n `405`
- 24h: commodity avg `-1.0608` n `12`; crypto_alt avg `2.4611` n `228`; crypto_major avg `0.8017` n `8`; equity avg `0.8751` n `67`; fx avg `-0.0443` n `6`; index avg `0.5007` n `23`; metal avg `1.5493` n `18`; unknown avg `1.8205` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
