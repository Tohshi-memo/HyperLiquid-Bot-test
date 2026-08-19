# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T22:37:27.723080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.9439` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `4.5778` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.6416` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0173` n `12`; crypto_alt avg `-0.2367` n `230`; crypto_major avg `-0.4203` n `8`; equity avg `0.0471` n `121`; fx avg `0.0053` n `6`; index avg `0.005` n `25`; metal avg `-0.0362` n `20`; unknown avg `0.1356` n `792`
- 1h: commodity avg `-0.0928` n `12`; crypto_alt avg `-0.5576` n `230`; crypto_major avg `-0.62` n `8`; equity avg `0.1657` n `121`; fx avg `0.0052` n `6`; index avg `0.039` n `25`; metal avg `-0.0386` n `20`; unknown avg `0.2094` n `792`
- 4h: commodity avg `-0.0961` n `12`; crypto_alt avg `2.1465` n `230`; crypto_major avg `4.8478` n `8`; equity avg `1.2062` n `121`; fx avg `-0.0214` n `6`; index avg `0.0941` n `25`; metal avg `0.27` n `20`; unknown avg `1.2009` n `792`
- 24h: commodity avg `-0.1223` n `12`; crypto_alt avg `5.2675` n `230`; crypto_major avg `10.1213` n `8`; equity avg `0.9293` n `120`; fx avg `-0.2168` n `6`; index avg `0.1366` n `25`; metal avg `1.2479` n `20`; unknown avg `1.4955` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
