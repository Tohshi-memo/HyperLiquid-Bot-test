# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T17:37:25.049014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.3874` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.2012` n `12`; crypto_alt avg `0.0875` n `228`; crypto_major avg `0.0544` n `8`; equity avg `0.2105` n `74`; fx avg `0.0026` n `6`; index avg `0.0721` n `23`; metal avg `-0.1076` n `18`; unknown avg `0.0769` n `547`
- 1h: commodity avg `0.5525` n `12`; crypto_alt avg `1.1441` n `228`; crypto_major avg `0.7254` n `8`; equity avg `1.5797` n `74`; fx avg `-0.0237` n `6`; index avg `0.4925` n `23`; metal avg `-0.0587` n `18`; unknown avg `0.4263` n `547`
- 4h: commodity avg `-0.12` n `12`; crypto_alt avg `-0.1906` n `228`; crypto_major avg `-0.8495` n `8`; equity avg `-3.2369` n `74`; fx avg `-0.0371` n `6`; index avg `-2.3738` n `23`; metal avg `-2.2145` n `18`; unknown avg `1.5399` n `545`
- 24h: commodity avg `-0.9304` n `12`; crypto_alt avg `-1.8639` n `228`; crypto_major avg `-2.5131` n `8`; equity avg `-2.8247` n `74`; fx avg `0.1052` n `6`; index avg `-1.9258` n `23`; metal avg `-1.6702` n `18`; unknown avg `-1.3843` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0448`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0436`, n `668`, weak_sample_signal
