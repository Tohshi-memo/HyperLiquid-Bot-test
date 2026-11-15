# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T02:56:00.864127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `4.2736` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `4.1376` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `3.4789` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `3.4677` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `3.461` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.8338` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0152` n `13`; crypto_alt avg `0.1336` n `239`; crypto_major avg `0.1693` n `8`; equity avg `0.0829` n `162`; fx avg `0.0094` n `6`; index avg `0.0026` n `27`; metal avg `0.0369` n `20`; unknown avg `0.2814` n `1261`
- 1h: commodity avg `0.0121` n `13`; crypto_alt avg `3.1382` n `239`; crypto_major avg `4.2857` n `8`; equity avg `0.818` n `162`; fx avg `0.006` n `6`; index avg `0.0403` n `27`; metal avg `0.1481` n `20`; unknown avg `51.9163` n `1257`
- 4h: commodity avg `0.0438` n `13`; crypto_alt avg `2.981` n `239`; crypto_major avg `3.5048` n `8`; equity avg `0.671` n `162`; fx avg `0.0029` n `6`; index avg `0.0281` n `27`; metal avg `0.0259` n `20`; unknown avg `241.3622` n `1250`
- 24h: commodity avg `-0.0191` n `13`; crypto_alt avg `-5.9251` n `239`; crypto_major avg `-5.0763` n `8`; equity avg `-0.8609` n `162`; fx avg `0.0351` n `6`; index avg `-0.0794` n `27`; metal avg `-0.4293` n `20`; unknown avg `47.2537` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
