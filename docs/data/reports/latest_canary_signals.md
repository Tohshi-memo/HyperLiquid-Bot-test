# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T23:07:25.299715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.2833` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `4.1234` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.0439` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0307` n `12`; crypto_alt avg `0.0972` n `230`; crypto_major avg `0.1929` n `8`; equity avg `0.0649` n `121`; fx avg `0.003` n `6`; index avg `0.0061` n `25`; metal avg `0.03` n `20`; unknown avg `0.0989` n `792`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `-0.3345` n `230`; crypto_major avg `-0.9011` n `8`; equity avg `0.247` n `121`; fx avg `0.0314` n `6`; index avg `0.0477` n `25`; metal avg `0.0116` n `20`; unknown avg `0.0008` n `792`
- 4h: commodity avg `-0.0059` n `12`; crypto_alt avg `1.9952` n `230`; crypto_major avg `4.2774` n `8`; equity avg `1.2335` n `121`; fx avg `-0.0047` n `6`; index avg `0.1223` n `25`; metal avg `0.154` n `20`; unknown avg `1.3114` n `792`
- 24h: commodity avg `-0.1051` n `12`; crypto_alt avg `5.2689` n `230`; crypto_major avg `9.7266` n `8`; equity avg `1.2162` n `120`; fx avg `-0.1913` n `6`; index avg `0.1653` n `25`; metal avg `1.2861` n `20`; unknown avg `1.4974` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
