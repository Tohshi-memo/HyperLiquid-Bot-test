# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T08:55:21.909926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0521` n `12`; crypto_alt avg `-0.1974` n `230`; crypto_major avg `-0.0173` n `8`; equity avg `0.0442` n `113`; fx avg `-0.0011` n `6`; index avg `0.0238` n `25`; metal avg `-0.0318` n `20`; unknown avg `-0.1164` n `786`
- 1h: commodity avg `-0.0991` n `12`; crypto_alt avg `-0.3144` n `230`; crypto_major avg `-0.0286` n `8`; equity avg `0.2831` n `113`; fx avg `-0.011` n `6`; index avg `0.0643` n `25`; metal avg `-0.0432` n `20`; unknown avg `-0.1239` n `786`
- 4h: commodity avg `-0.0265` n `12`; crypto_alt avg `-0.7957` n `230`; crypto_major avg `-0.125` n `8`; equity avg `0.403` n `113`; fx avg `0.0087` n `6`; index avg `0.0773` n `25`; metal avg `0.0621` n `20`; unknown avg `-0.2041` n `770`
- 24h: commodity avg `-0.1802` n `12`; crypto_alt avg `-1.4455` n `230`; crypto_major avg `0.5612` n `8`; equity avg `2.6204` n `113`; fx avg `0.0019` n `6`; index avg `0.2618` n `25`; metal avg `0.1188` n `20`; unknown avg `-0.2768` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2375`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2271`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2142`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1988`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
