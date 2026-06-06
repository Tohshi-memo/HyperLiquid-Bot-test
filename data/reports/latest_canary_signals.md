# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T00:37:23.649191+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2241` n `12`; crypto_alt avg `0.119` n `228`; crypto_major avg `0.1902` n `8`; equity avg `-0.0897` n `74`; fx avg `0.0011` n `6`; index avg `-0.0703` n `23`; metal avg `0.0307` n `18`; unknown avg `1.2351` n `425`
- 1h: commodity avg `0.4226` n `12`; crypto_alt avg `1.3999` n `228`; crypto_major avg `1.3708` n `8`; equity avg `0.397` n `74`; fx avg `-0.0001` n `6`; index avg `0.2611` n `23`; metal avg `0.0296` n `18`; unknown avg `0.761` n `425`
- 4h: commodity avg `0.5653` n `12`; crypto_alt avg `0.3155` n `228`; crypto_major avg `0.2704` n `8`; equity avg `0.278` n `74`; fx avg `0.006` n `6`; index avg `0.4609` n `23`; metal avg `0.0285` n `18`; unknown avg `2.2855` n `425`
- 24h: commodity avg `-0.9492` n `12`; crypto_alt avg `-6.1339` n `228`; crypto_major avg `-5.3281` n `8`; equity avg `-5.2928` n `74`; fx avg `-0.1122` n `6`; index avg `-3.4836` n `23`; metal avg `-4.2436` n `18`; unknown avg `-1.0909` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
