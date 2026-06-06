# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T01:07:27.385097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.067` n `12`; crypto_alt avg `0.0137` n `228`; crypto_major avg `0.1661` n `8`; equity avg `-0.0221` n `74`; fx avg `-0.008` n `6`; index avg `0.0978` n `23`; metal avg `0.0133` n `18`; unknown avg `0.05` n `425`
- 1h: commodity avg `0.1787` n `12`; crypto_alt avg `0.2749` n `228`; crypto_major avg `0.3403` n `8`; equity avg `0.0488` n `74`; fx avg `-0.0069` n `6`; index avg `0.0251` n `23`; metal avg `0.0782` n `18`; unknown avg `0.5385` n `425`
- 4h: commodity avg `0.2658` n `12`; crypto_alt avg `-0.1311` n `228`; crypto_major avg `0.0375` n `8`; equity avg `0.0295` n `74`; fx avg `0.01` n `6`; index avg `0.4235` n `23`; metal avg `-0.0605` n `18`; unknown avg `0.4975` n `425`
- 24h: commodity avg `-0.814` n `12`; crypto_alt avg `-5.1735` n `228`; crypto_major avg `-4.4359` n `8`; equity avg `-4.9721` n `74`; fx avg `-0.1595` n `6`; index avg `-3.3644` n `23`; metal avg `-3.9627` n `18`; unknown avg `-1.0418` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
