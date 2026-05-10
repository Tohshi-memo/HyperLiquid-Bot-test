# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T13:37:17.052809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `-0.0131` n `228`; crypto_major avg `0.1141` n `8`; equity avg `-0.0335` n `65`; fx avg `0.0` n `5`; index avg `0.0042` n `23`; metal avg `-0.0137` n `18`; unknown avg `-0.1643` n `376`
- 1h: commodity avg `-0.1075` n `12`; crypto_alt avg `0.3961` n `228`; crypto_major avg `0.3282` n `8`; equity avg `-0.0117` n `65`; fx avg `-0.0004` n `5`; index avg `0.0249` n `23`; metal avg `0.2162` n `18`; unknown avg `-0.3602` n `376`
- 4h: commodity avg `-0.0508` n `12`; crypto_alt avg `0.1813` n `228`; crypto_major avg `0.015` n `8`; equity avg `0.0395` n `65`; fx avg `-0.0102` n `5`; index avg `-0.012` n `23`; metal avg `0.2994` n `18`; unknown avg `-0.422` n `376`
- 24h: commodity avg `-0.0361` n `12`; crypto_alt avg `0.4996` n `228`; crypto_major avg `0.1375` n `8`; equity avg `0.8546` n `65`; fx avg `-0.0089` n `5`; index avg `0.2568` n `23`; metal avg `0.7216` n `18`; unknown avg `0.1158` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
