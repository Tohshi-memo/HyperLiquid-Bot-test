# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T07:07:25.483879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `-0.3215` n `228`; crypto_major avg `-0.3584` n `8`; equity avg `-0.1184` n `78`; fx avg `-0.011` n `6`; index avg `-0.0166` n `23`; metal avg `0.0191` n `18`; unknown avg `-0.0821` n `687`
- 1h: commodity avg `0.0302` n `12`; crypto_alt avg `-0.1978` n `228`; crypto_major avg `-0.2059` n `8`; equity avg `-0.0615` n `78`; fx avg `0.0015` n `6`; index avg `-0.005` n `23`; metal avg `0.0409` n `18`; unknown avg `-0.1547` n `671`
- 4h: commodity avg `0.0623` n `12`; crypto_alt avg `0.6986` n `228`; crypto_major avg `1.117` n `8`; equity avg `0.3405` n `78`; fx avg `-0.0359` n `6`; index avg `0.001` n `23`; metal avg `0.088` n `18`; unknown avg `0.0636` n `639`
- 24h: commodity avg `0.513` n `12`; crypto_alt avg `-3.2719` n `228`; crypto_major avg `-3.5577` n `8`; equity avg `1.2892` n `78`; fx avg `-0.1106` n `6`; index avg `0.31` n `23`; metal avg `-4.0874` n `18`; unknown avg `0.1251` n `530`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
