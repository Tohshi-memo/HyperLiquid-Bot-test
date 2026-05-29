# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T18:37:31.696399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9478` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5157` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0563` n `12`; crypto_alt avg `-0.1641` n `228`; crypto_major avg `-0.0199` n `8`; equity avg `-0.0173` n `69`; fx avg `0.0045` n `6`; index avg `0.0087` n `23`; metal avg `0.0608` n `18`; unknown avg `-0.0571` n `419`
- 1h: commodity avg `-0.0088` n `12`; crypto_alt avg `-0.7821` n `228`; crypto_major avg `-0.6378` n `8`; equity avg `-0.2415` n `69`; fx avg `0.0012` n `6`; index avg `-0.0467` n `23`; metal avg `0.1287` n `18`; unknown avg `-0.1022` n `419`
- 4h: commodity avg `-0.9171` n `12`; crypto_alt avg `2.3084` n `228`; crypto_major avg `2.0307` n `8`; equity avg `1.0977` n `69`; fx avg `0.0959` n `6`; index avg `0.2902` n `23`; metal avg `0.515` n `18`; unknown avg `1.6557` n `418`
- 24h: commodity avg `-1.0665` n `12`; crypto_alt avg `0.7755` n `228`; crypto_major avg `1.2164` n `8`; equity avg `1.3626` n `69`; fx avg `0.1951` n `6`; index avg `-0.0072` n `23`; metal avg `0.2637` n `18`; unknown avg `1.0134` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1887`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
