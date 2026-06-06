# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T09:07:20.933999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.3357` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.9394` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.7112` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.169` n `12`; crypto_alt avg `-0.2149` n `228`; crypto_major avg `-0.4355` n `8`; equity avg `0.048` n `74`; fx avg `0.0002` n `6`; index avg `0.4485` n `23`; metal avg `0.0482` n `18`; unknown avg `0.0289` n `425`
- 1h: commodity avg `0.2798` n `12`; crypto_alt avg `0.6933` n `228`; crypto_major avg `0.3705` n `8`; equity avg `0.4078` n `74`; fx avg `0.0002` n `6`; index avg `0.6934` n `23`; metal avg `0.1456` n `18`; unknown avg `0.2243` n `425`
- 4h: commodity avg `0.1109` n `12`; crypto_alt avg `4.4102` n `228`; crypto_major avg `3.4466` n `8`; equity avg `0.7354` n `74`; fx avg `-0.0119` n `6`; index avg `0.8917` n `23`; metal avg `0.5072` n `18`; unknown avg `1.0403` n `415`
- 24h: commodity avg `-1.1866` n `12`; crypto_alt avg `-2.6372` n `228`; crypto_major avg `-2.6892` n `8`; equity avg `-6.6821` n `74`; fx avg `-0.2449` n `6`; index avg `-3.6161` n `23`; metal avg `-4.0639` n `18`; unknown avg `1.0622` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
