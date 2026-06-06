# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T08:17:51.498320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5659` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.3009` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.0312` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0385` n `12`; crypto_alt avg `0.2162` n `228`; crypto_major avg `0.1924` n `8`; equity avg `0.0932` n `74`; fx avg `0.0` n `6`; index avg `0.0511` n `23`; metal avg `0.0237` n `18`; unknown avg `-0.0679` n `425`
- 1h: commodity avg `-0.0065` n `12`; crypto_alt avg `0.3779` n `228`; crypto_major avg `0.3779` n `8`; equity avg `-0.2193` n `74`; fx avg `0.001` n `6`; index avg `-0.1308` n `23`; metal avg `-0.0413` n `18`; unknown avg `0.084` n `425`
- 4h: commodity avg `-0.3341` n `12`; crypto_alt avg `2.4134` n `228`; crypto_major avg `2.2318` n `8`; equity avg `-0.0691` n `74`; fx avg `-0.0279` n `6`; index avg `-0.2094` n `23`; metal avg `0.2006` n `18`; unknown avg `0.5166` n `415`
- 24h: commodity avg `-1.2104` n `12`; crypto_alt avg `-3.2875` n `228`; crypto_major avg `-2.8503` n `8`; equity avg `-6.9371` n `74`; fx avg `-0.2455` n `6`; index avg `-4.2477` n `23`; metal avg `-4.2168` n `18`; unknown avg `0.4364` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
