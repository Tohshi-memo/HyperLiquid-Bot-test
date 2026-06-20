# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T09:22:27.748280+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `0.0654` n `228`; crypto_major avg `-0.0292` n `8`; equity avg `0.0117` n `78`; fx avg `0.0084` n `6`; index avg `0.0181` n `23`; metal avg `0.0048` n `18`; unknown avg `-0.0182` n `687`
- 1h: commodity avg `-0.0239` n `12`; crypto_alt avg `0.2256` n `228`; crypto_major avg `0.0047` n `8`; equity avg `-0.0825` n `78`; fx avg `-0.2792` n `6`; index avg `0.0115` n `23`; metal avg `-0.006` n `18`; unknown avg `-0.0074` n `687`
- 4h: commodity avg `0.0389` n `12`; crypto_alt avg `0.1218` n `228`; crypto_major avg `0.0673` n `8`; equity avg `-0.0263` n `78`; fx avg `-0.2732` n `6`; index avg `-0.0301` n `23`; metal avg `0.0011` n `18`; unknown avg `0.0499` n `639`
- 24h: commodity avg `0.4996` n `12`; crypto_alt avg `-2.9674` n `228`; crypto_major avg `-3.5043` n `8`; equity avg `1.2476` n `78`; fx avg `-0.3724` n `6`; index avg `0.2974` n `23`; metal avg `-4.1041` n `18`; unknown avg `0.0347` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
