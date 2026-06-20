# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T07:22:25.516783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0597` n `12`; crypto_alt avg `0.1482` n `228`; crypto_major avg `0.2417` n `8`; equity avg `0.0227` n `78`; fx avg `0.0117` n `6`; index avg `-0.0336` n `23`; metal avg `0.0041` n `18`; unknown avg `0.1829` n `687`
- 1h: commodity avg `0.0532` n `12`; crypto_alt avg `-0.2174` n `228`; crypto_major avg `-0.1099` n `8`; equity avg `-0.0599` n `78`; fx avg `0.0065` n `6`; index avg `-0.0452` n `23`; metal avg `0.0458` n `18`; unknown avg `-0.0812` n `679`
- 4h: commodity avg `0.1187` n `12`; crypto_alt avg `0.6743` n `228`; crypto_major avg `1.2591` n `8`; equity avg `0.3476` n `78`; fx avg `-0.0236` n `6`; index avg `-0.0225` n `23`; metal avg `0.0847` n `18`; unknown avg `0.1433` n `639`
- 24h: commodity avg `0.574` n `12`; crypto_alt avg `-3.1319` n `228`; crypto_major avg `-3.3254` n `8`; equity avg `1.3117` n `78`; fx avg `-0.0989` n `6`; index avg `0.2746` n `23`; metal avg `-4.0838` n `18`; unknown avg `0.162` n `530`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
