# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T08:22:21.517683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.71` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.3737` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.1724` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0538` n `12`; crypto_alt avg `0.3989` n `228`; crypto_major avg `0.3474` n `8`; equity avg `0.1795` n `74`; fx avg `0.0` n `6`; index avg `0.1017` n `23`; metal avg `0.0412` n `18`; unknown avg `0.1303` n `425`
- 1h: commodity avg `0.0085` n `12`; crypto_alt avg `0.5615` n `228`; crypto_major avg `0.5331` n `8`; equity avg `-0.1337` n `74`; fx avg `0.001` n `6`; index avg `-0.0804` n `23`; metal avg `-0.0238` n `18`; unknown avg `0.2913` n `425`
- 4h: commodity avg `-0.3194` n `12`; crypto_alt avg `2.6008` n `228`; crypto_major avg `2.3906` n `8`; equity avg `0.0169` n `74`; fx avg `-0.0279` n `6`; index avg `-0.1589` n `23`; metal avg `0.2182` n `18`; unknown avg `0.8316` n `415`
- 24h: commodity avg `-1.1953` n `12`; crypto_alt avg `-3.1118` n `228`; crypto_major avg `-2.701` n `8`; equity avg `-6.8598` n `74`; fx avg `-0.2455` n `6`; index avg `-4.1997` n `23`; metal avg `-4.2007` n `18`; unknown avg `0.596` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
