# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T11:37:29.260712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0604` n `12`; crypto_alt avg `0.1704` n `228`; crypto_major avg `0.2595` n `8`; equity avg `0.2604` n `74`; fx avg `0.0019` n `6`; index avg `0.0847` n `23`; metal avg `-0.0292` n `18`; unknown avg `0.019` n `517`
- 1h: commodity avg `-0.722` n `12`; crypto_alt avg `0.9091` n `228`; crypto_major avg `0.9897` n `8`; equity avg `0.9723` n `74`; fx avg `0.0175` n `6`; index avg `0.4331` n `23`; metal avg `0.6615` n `18`; unknown avg `0.307` n `517`
- 4h: commodity avg `-0.9298` n `12`; crypto_alt avg `1.3923` n `228`; crypto_major avg `0.8368` n `8`; equity avg `1.2803` n `74`; fx avg `0.005` n `6`; index avg `0.6495` n `23`; metal avg `0.6267` n `18`; unknown avg `-0.0217` n `517`
- 24h: commodity avg `-0.2062` n `12`; crypto_alt avg `1.5721` n `228`; crypto_major avg `2.511` n `8`; equity avg `2.038` n `74`; fx avg `-0.2479` n `6`; index avg `1.0417` n `23`; metal avg `0.0851` n `18`; unknown avg `-2.2691` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
