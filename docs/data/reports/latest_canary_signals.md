# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T17:37:25.861249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0304` n `12`; crypto_alt avg `0.3628` n `230`; crypto_major avg `0.1981` n `8`; equity avg `0.1799` n `121`; fx avg `0.0025` n `6`; index avg `0.0019` n `25`; metal avg `0.0213` n `20`; unknown avg `0.1517` n `793`
- 1h: commodity avg `0.0708` n `12`; crypto_alt avg `-0.1616` n `230`; crypto_major avg `-0.1185` n `8`; equity avg `0.0303` n `121`; fx avg `0.0105` n `6`; index avg `-0.0163` n `25`; metal avg `0.0237` n `20`; unknown avg `0.091` n `793`
- 4h: commodity avg `0.0178` n `12`; crypto_alt avg `1.0499` n `230`; crypto_major avg `0.5603` n `8`; equity avg `-0.0782` n `121`; fx avg `0.032` n `6`; index avg `0.0469` n `25`; metal avg `0.0643` n `20`; unknown avg `0.1713` n `793`
- 24h: commodity avg `0.2989` n `12`; crypto_alt avg `6.6658` n `230`; crypto_major avg `3.2957` n `8`; equity avg `1.4011` n `121`; fx avg `-0.0915` n `6`; index avg `0.1113` n `25`; metal avg `0.6574` n `20`; unknown avg `1.1562` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2361`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1898`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
