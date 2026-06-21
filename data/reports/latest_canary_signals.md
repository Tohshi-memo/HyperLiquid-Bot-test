# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T20:22:26.611137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0216` n `12`; crypto_alt avg `-0.1946` n `228`; crypto_major avg `-0.2563` n `8`; equity avg `-0.0117` n `78`; fx avg `0.0002` n `6`; index avg `-0.0083` n `23`; metal avg `-0.0001` n `18`; unknown avg `-0.0474` n `702`
- 1h: commodity avg `-0.0685` n `12`; crypto_alt avg `-0.2524` n `228`; crypto_major avg `-0.1364` n `8`; equity avg `-0.0144` n `78`; fx avg `-0.0423` n `6`; index avg `0.0159` n `23`; metal avg `-0.0185` n `18`; unknown avg `0.2052` n `702`
- 4h: commodity avg `0.1443` n `12`; crypto_alt avg `-0.4011` n `228`; crypto_major avg `-0.1112` n `8`; equity avg `-0.0616` n `78`; fx avg `-0.1374` n `6`; index avg `0.0134` n `23`; metal avg `-0.0762` n `18`; unknown avg `-0.0107` n `694`
- 24h: commodity avg `0.2687` n `12`; crypto_alt avg `1.3594` n `228`; crypto_major avg `0.1814` n `8`; equity avg `0.2558` n `78`; fx avg `-0.1123` n `6`; index avg `0.0287` n `23`; metal avg `-0.0884` n `18`; unknown avg `0.2754` n `645`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
