# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T11:22:25.894908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0337` n `12`; crypto_alt avg `-0.1846` n `228`; crypto_major avg `-0.2234` n `8`; equity avg `-0.0642` n `78`; fx avg `0.0041` n `6`; index avg `0.005` n `23`; metal avg `-0.0087` n `18`; unknown avg `-0.0589` n `702`
- 1h: commodity avg `-0.0618` n `12`; crypto_alt avg `-0.3883` n `228`; crypto_major avg `-0.4253` n `8`; equity avg `-0.0505` n `78`; fx avg `0.0109` n `6`; index avg `0.006` n `23`; metal avg `-0.0615` n `18`; unknown avg `-0.0337` n `702`
- 4h: commodity avg `-0.0499` n `12`; crypto_alt avg `0.3142` n `228`; crypto_major avg `-0.3811` n `8`; equity avg `-0.133` n `78`; fx avg `0.0016` n `6`; index avg `-0.0048` n `23`; metal avg `-0.0961` n `18`; unknown avg `-0.3176` n `694`
- 24h: commodity avg `0.0673` n `12`; crypto_alt avg `1.3559` n `228`; crypto_major avg `-0.1454` n `8`; equity avg `0.3535` n `78`; fx avg `0.0263` n `6`; index avg `0.0403` n `23`; metal avg `-0.0761` n `18`; unknown avg `0.5767` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
