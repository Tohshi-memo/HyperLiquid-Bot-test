# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T21:39:49.751803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1966` n `12`; crypto_alt avg `0.2994` n `228`; crypto_major avg `0.2501` n `8`; equity avg `0.1058` n `78`; fx avg `-0.0035` n `6`; index avg `-0.0059` n `23`; metal avg `0.0094` n `18`; unknown avg `5.6212` n `702`
- 1h: commodity avg `0.0848` n `12`; crypto_alt avg `-0.6455` n `228`; crypto_major avg `-0.4592` n `8`; equity avg `-0.0195` n `78`; fx avg `-0.045` n `6`; index avg `-0.0111` n `23`; metal avg `-0.0268` n `18`; unknown avg `0.1488` n `702`
- 4h: commodity avg `0.1778` n `12`; crypto_alt avg `-0.8989` n `228`; crypto_major avg `-0.4113` n `8`; equity avg `-0.0747` n `78`; fx avg `-0.099` n `6`; index avg `-0.0161` n `23`; metal avg `-0.1155` n `18`; unknown avg `1.0275` n `694`
- 24h: commodity avg `0.3071` n `12`; crypto_alt avg `0.3913` n `228`; crypto_major avg `-0.5576` n `8`; equity avg `0.1837` n `78`; fx avg `-0.1555` n `6`; index avg `0.0075` n `23`; metal avg `-0.1365` n `18`; unknown avg `0.7616` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
