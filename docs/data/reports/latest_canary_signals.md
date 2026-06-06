# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T05:37:27.671282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.7935` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0471` n `12`; crypto_alt avg `0.2137` n `228`; crypto_major avg `0.2136` n `8`; equity avg `0.1952` n `74`; fx avg `-0.0064` n `6`; index avg `0.0417` n `23`; metal avg `0.0955` n `18`; unknown avg `0.604` n `425`
- 1h: commodity avg `-0.1188` n `12`; crypto_alt avg `1.913` n `228`; crypto_major avg `1.8643` n `8`; equity avg `0.4716` n `74`; fx avg `-0.0142` n `6`; index avg `0.0378` n `23`; metal avg `0.0708` n `18`; unknown avg `26.1604` n `425`
- 4h: commodity avg `-0.3322` n `12`; crypto_alt avg `-2.975` n `228`; crypto_major avg `-1.6945` n `8`; equity avg `-1.0961` n `74`; fx avg `-0.0127` n `6`; index avg `-0.7158` n `23`; metal avg `-0.583` n `18`; unknown avg `-0.2382` n `425`
- 24h: commodity avg `-1.5656` n `12`; crypto_alt avg `-7.2136` n `228`; crypto_major avg `-5.1831` n `8`; equity avg `-7.0376` n `74`; fx avg `-0.1792` n `6`; index avg `-4.3581` n `23`; metal avg `-4.2497` n `18`; unknown avg `-0.8756` n `404`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
