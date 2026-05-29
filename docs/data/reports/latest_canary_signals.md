# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T17:37:16.479649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.0571` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.3811` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.202` n `12`; crypto_alt avg `0.2686` n `228`; crypto_major avg `0.0453` n `8`; equity avg `0.0948` n `69`; fx avg `0.001` n `6`; index avg `-0.011` n `23`; metal avg `0.001` n `18`; unknown avg `0.0011` n `419`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `0.3955` n `228`; crypto_major avg `0.2722` n `8`; equity avg `0.1143` n `69`; fx avg `0.002` n `6`; index avg `0.1055` n `23`; metal avg `-0.2385` n `18`; unknown avg `0.109` n `419`
- 4h: commodity avg `-0.6289` n `12`; crypto_alt avg `2.7335` n `228`; crypto_major avg `2.4282` n `8`; equity avg `1.0701` n `69`; fx avg `0.0708` n `6`; index avg `0.0863` n `23`; metal avg `0.0471` n `18`; unknown avg `0.9812` n `417`
- 24h: commodity avg `-0.6552` n `12`; crypto_alt avg `1.9946` n `228`; crypto_major avg `2.1689` n `8`; equity avg `2.1271` n `69`; fx avg `0.2071` n `6`; index avg `-0.01` n `23`; metal avg `0.0957` n `18`; unknown avg `1.3247` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1929`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
