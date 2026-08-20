# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T00:07:30.194123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4869` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4574` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.2362` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0126` n `12`; crypto_alt avg `0.2806` n `230`; crypto_major avg `0.3488` n `8`; equity avg `-0.3409` n `121`; fx avg `-0.004` n `6`; index avg `-0.0875` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.0564` n `792`
- 1h: commodity avg `0.0177` n `12`; crypto_alt avg `0.2747` n `230`; crypto_major avg `-0.1369` n `8`; equity avg `-0.3647` n `121`; fx avg `0.0005` n `6`; index avg `-0.1152` n `25`; metal avg `-0.0298` n `20`; unknown avg `0.0305` n `792`
- 4h: commodity avg `0.0505` n `12`; crypto_alt avg `1.4591` n `230`; crypto_major avg `2.5374` n `8`; equity avg `0.3012` n `121`; fx avg `0.0002` n `6`; index avg `0.0184` n `25`; metal avg `0.08` n `20`; unknown avg `0.2563` n `792`
- 24h: commodity avg `-0.0643` n `12`; crypto_alt avg `5.4943` n `230`; crypto_major avg `9.6862` n `8`; equity avg `1.1857` n `120`; fx avg `-0.1905` n `6`; index avg `0.133` n `25`; metal avg `1.2481` n `20`; unknown avg `1.4903` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
