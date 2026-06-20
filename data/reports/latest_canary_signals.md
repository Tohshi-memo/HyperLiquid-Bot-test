# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T08:52:25.753334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0207` n `12`; crypto_alt avg `0.0083` n `228`; crypto_major avg `-0.0278` n `8`; equity avg `-0.1053` n `78`; fx avg `0.0021` n `6`; index avg `-0.0346` n `23`; metal avg `-0.0182` n `18`; unknown avg `0.0207` n `687`
- 1h: commodity avg `-0.0249` n `12`; crypto_alt avg `0.0048` n `228`; crypto_major avg `-0.1934` n `8`; equity avg `-0.0884` n `78`; fx avg `0.0158` n `6`; index avg `-0.0046` n `23`; metal avg `-0.0341` n `18`; unknown avg `0.0154` n `687`
- 4h: commodity avg `0.099` n `12`; crypto_alt avg `0.2487` n `228`; crypto_major avg `0.3793` n `8`; equity avg `0.0506` n `78`; fx avg `0.0241` n `6`; index avg `-0.0362` n `23`; metal avg `0.0021` n `18`; unknown avg `-0.0764` n `639`
- 24h: commodity avg `0.503` n `12`; crypto_alt avg `-3.2145` n `228`; crypto_major avg `-3.6047` n `8`; equity avg `1.2061` n `78`; fx avg `-0.0978` n `6`; index avg `0.2708` n `23`; metal avg `-4.1127` n `18`; unknown avg `0.0018` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
