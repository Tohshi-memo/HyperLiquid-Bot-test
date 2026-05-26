# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T10:07:18.324121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1781` n `12`; crypto_alt avg `0.0781` n `228`; crypto_major avg `0.0753` n `8`; equity avg `0.088` n `67`; fx avg `-0.0073` n `6`; index avg `0.0009` n `23`; metal avg `0.0261` n `18`; unknown avg `0.3662` n `417`
- 1h: commodity avg `-0.2635` n `12`; crypto_alt avg `0.0502` n `228`; crypto_major avg `0.058` n `8`; equity avg `0.0901` n `67`; fx avg `0.0224` n `6`; index avg `0.0851` n `23`; metal avg `-0.1339` n `18`; unknown avg `0.3254` n `417`
- 4h: commodity avg `0.4651` n `12`; crypto_alt avg `-0.2566` n `228`; crypto_major avg `-0.4105` n `8`; equity avg `0.1756` n `67`; fx avg `0.0265` n `6`; index avg `0.1062` n `23`; metal avg `-0.344` n `18`; unknown avg `-0.2012` n `417`
- 24h: commodity avg `0.8073` n `12`; crypto_alt avg `-0.8628` n `228`; crypto_major avg `-1.6886` n `8`; equity avg `-0.5297` n `67`; fx avg `-0.084` n `6`; index avg `0.0065` n `23`; metal avg `-1.0299` n `18`; unknown avg `-0.2604` n `387`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
