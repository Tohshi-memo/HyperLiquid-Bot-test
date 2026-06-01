# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T20:07:25.387458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.99` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.3053` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.8693` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6691` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0375` n `12`; crypto_alt avg `-0.1494` n `228`; crypto_major avg `-0.0533` n `8`; equity avg `-0.1287` n `69`; fx avg `0.0018` n `6`; index avg `-0.0056` n `23`; metal avg `0.0205` n `18`; unknown avg `-0.1459` n `422`
- 1h: commodity avg `0.0314` n `12`; crypto_alt avg `0.2793` n `228`; crypto_major avg `0.276` n `8`; equity avg `-0.4321` n `69`; fx avg `0.0031` n `6`; index avg `-0.1752` n `23`; metal avg `-0.1432` n `18`; unknown avg `-0.141` n `422`
- 4h: commodity avg `-0.5026` n `12`; crypto_alt avg `2.1297` n `228`; crypto_major avg `1.8027` n `8`; equity avg `-0.0666` n `69`; fx avg `0.068` n `6`; index avg `0.3287` n `23`; metal avg `0.1336` n `18`; unknown avg `0.4701` n `422`
- 24h: commodity avg `0.6456` n `12`; crypto_alt avg `1.6169` n `228`; crypto_major avg `-0.1574` n `8`; equity avg `-0.141` n `69`; fx avg `0.0476` n `6`; index avg `0.3552` n `23`; metal avg `-0.0143` n `18`; unknown avg `3.0103` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
