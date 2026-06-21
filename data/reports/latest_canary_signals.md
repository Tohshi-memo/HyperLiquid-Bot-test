# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T07:52:29.741865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0157` n `12`; crypto_alt avg `-0.1005` n `228`; crypto_major avg `-0.0903` n `8`; equity avg `-0.0081` n `78`; fx avg `0.1022` n `6`; index avg `-0.0048` n `23`; metal avg `-0.0441` n `18`; unknown avg `-0.119` n `694`
- 1h: commodity avg `-0.0344` n `12`; crypto_alt avg `0.2559` n `228`; crypto_major avg `-0.0761` n `8`; equity avg `0.0118` n `78`; fx avg `0.0011` n `6`; index avg `-0.0008` n `23`; metal avg `-0.0336` n `18`; unknown avg `0.1711` n `694`
- 4h: commodity avg `-0.0759` n `12`; crypto_alt avg `0.1815` n `228`; crypto_major avg `-0.4013` n `8`; equity avg `0.1318` n `78`; fx avg `0.0023` n `6`; index avg `0.0117` n `23`; metal avg `0.0194` n `18`; unknown avg `0.5159` n `654`
- 24h: commodity avg `0.0301` n `12`; crypto_alt avg `1.3488` n `228`; crypto_major avg `0.1311` n `8`; equity avg `0.3167` n `78`; fx avg `0.0704` n `6`; index avg `0.047` n `23`; metal avg `-0.0426` n `18`; unknown avg `0.1733` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
