# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T20:22:23.663938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.05` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.6354` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.8265` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6446` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0798` n `12`; crypto_alt avg `0.0437` n `228`; crypto_major avg `0.1761` n `8`; equity avg `0.04` n `69`; fx avg `-0.0031` n `6`; index avg `-0.04` n `23`; metal avg `-0.0397` n `18`; unknown avg `0.0775` n `422`
- 1h: commodity avg `-0.0863` n `12`; crypto_alt avg `0.3398` n `228`; crypto_major avg `0.4183` n `8`; equity avg `-0.3513` n `69`; fx avg `-0.0065` n `6`; index avg `-0.2105` n `23`; metal avg `-0.1478` n `18`; unknown avg `0.1022` n `422`
- 4h: commodity avg `-0.736` n `12`; crypto_alt avg `1.8324` n `228`; crypto_major avg `1.8994` n `8`; equity avg `0.0729` n `69`; fx avg `0.0378` n `6`; index avg `0.2205` n `23`; metal avg `0.2548` n `18`; unknown avg `0.6586` n `422`
- 24h: commodity avg `0.481` n `12`; crypto_alt avg `1.5139` n `228`; crypto_major avg `-0.0303` n `8`; equity avg `-0.0901` n `69`; fx avg `0.0531` n `6`; index avg `0.3411` n `23`; metal avg `-0.0341` n `18`; unknown avg `2.9825` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1932`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
