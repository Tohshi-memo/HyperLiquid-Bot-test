# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T22:52:23.321133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.0334` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.912` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.5495` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0483` n `12`; crypto_alt avg `0.244` n `228`; crypto_major avg `0.0759` n `8`; equity avg `-0.1816` n `74`; fx avg `-0.0077` n `6`; index avg `-0.1438` n `23`; metal avg `-0.0083` n `18`; unknown avg `1.4439` n `425`
- 1h: commodity avg `0.3111` n `12`; crypto_alt avg `-0.7638` n `228`; crypto_major avg `-0.644` n `8`; equity avg `-0.3447` n `74`; fx avg `-0.0039` n `6`; index avg `-0.0666` n `23`; metal avg `-0.0668` n `18`; unknown avg `0.7716` n `425`
- 4h: commodity avg `-0.1264` n `12`; crypto_alt avg `3.1465` n `228`; crypto_major avg `2.907` n `8`; equity avg `0.3575` n `74`; fx avg `-0.0026` n `6`; index avg `-0.1416` n `23`; metal avg `-0.005` n `18`; unknown avg `4.4673` n `424`
- 24h: commodity avg `-1.5099` n `12`; crypto_alt avg `-5.3128` n `228`; crypto_major avg `-4.8003` n `8`; equity avg `-6.0413` n `74`; fx avg `-0.0446` n `6`; index avg `-4.1573` n `23`; metal avg `-4.4853` n `18`; unknown avg `-0.2177` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
