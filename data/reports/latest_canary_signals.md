# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T10:52:14.152232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.8695` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.7097` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0094` n `12`; crypto_alt avg `-0.0378` n `228`; crypto_major avg `-0.0873` n `8`; equity avg `0.0052` n `65`; fx avg `0.0006` n `5`; index avg `0.0038` n `23`; metal avg `0.0025` n `18`; unknown avg `-0.0495` n `383`
- 1h: commodity avg `-0.0389` n `12`; crypto_alt avg `0.1221` n `228`; crypto_major avg `0.2919` n `8`; equity avg `0.1173` n `65`; fx avg `0.0015` n `5`; index avg `0.0731` n `23`; metal avg `0.0107` n `18`; unknown avg `0.1168` n `383`
- 4h: commodity avg `1.7512` n `12`; crypto_alt avg `-8.6958` n `228`; crypto_major avg `-2.1183` n `8`; equity avg `-2.6295` n `65`; fx avg `-0.1683` n `5`; index avg `-1.6659` n `23`; metal avg `-5.828` n `18`; unknown avg `550.2091` n `367`
- 24h: commodity avg `1.7512` n `12`; crypto_alt avg `-8.6958` n `228`; crypto_major avg `-2.1183` n `8`; equity avg `-2.6295` n `65`; fx avg `-0.1683` n `5`; index avg `-1.6659` n `23`; metal avg `-5.828` n `18`; unknown avg `550.2091` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
