# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T23:37:23.081812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2209` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.454` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.2111` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0453` n `12`; crypto_alt avg `0.1609` n `228`; crypto_major avg `0.2886` n `8`; equity avg `0.0876` n `74`; fx avg `0.0068` n `6`; index avg `0.0816` n `23`; metal avg `0.2002` n `18`; unknown avg `-0.067` n `516`
- 1h: commodity avg `-0.2042` n `12`; crypto_alt avg `-0.7313` n `228`; crypto_major avg `-0.3605` n `8`; equity avg `-0.2404` n `74`; fx avg `-0.0002` n `6`; index avg `-0.0005` n `23`; metal avg `0.2443` n `18`; unknown avg `-0.0805` n `516`
- 4h: commodity avg `-0.4808` n `12`; crypto_alt avg `2.4666` n `228`; crypto_major avg `2.7401` n `8`; equity avg `0.529` n `74`; fx avg `-0.04` n `6`; index avg `0.0803` n `23`; metal avg `0.2861` n `18`; unknown avg `1.0049` n `516`
- 24h: commodity avg `0.0417` n `12`; crypto_alt avg `3.1182` n `228`; crypto_major avg `4.918` n `8`; equity avg `1.3106` n `74`; fx avg `-0.0493` n `6`; index avg `0.2132` n `23`; metal avg `0.6135` n `18`; unknown avg `-4.6179` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
