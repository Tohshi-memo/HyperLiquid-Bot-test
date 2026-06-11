# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T00:22:26.717922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.148` n `12`; crypto_alt avg `0.3707` n `228`; crypto_major avg `0.3719` n `8`; equity avg `0.5064` n `74`; fx avg `0.0106` n `6`; index avg `-0.0635` n `23`; metal avg `0.5362` n `18`; unknown avg `0.1971` n `550`
- 1h: commodity avg `-0.1233` n `12`; crypto_alt avg `0.922` n `228`; crypto_major avg `0.5689` n `8`; equity avg `0.8429` n `74`; fx avg `0.089` n `6`; index avg `0.1777` n `23`; metal avg `0.6066` n `18`; unknown avg `0.0404` n `550`
- 4h: commodity avg `0.4243` n `12`; crypto_alt avg `0.1603` n `228`; crypto_major avg `-0.0158` n `8`; equity avg `-0.304` n `74`; fx avg `0.0198` n `6`; index avg `-0.0529` n `23`; metal avg `-0.2354` n `18`; unknown avg `0.0402` n `550`
- 24h: commodity avg `1.2315` n `12`; crypto_alt avg `-1.5694` n `228`; crypto_major avg `-1.8504` n `8`; equity avg `-2.3039` n `74`; fx avg `0.1058` n `6`; index avg `-1.7098` n `23`; metal avg `-2.2656` n `18`; unknown avg `-0.3763` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
