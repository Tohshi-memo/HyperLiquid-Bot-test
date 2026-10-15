# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T17:22:28.535166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.307` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.1733` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0167` n `13`; crypto_alt avg `0.6864` n `236`; crypto_major avg `0.6545` n `8`; equity avg `0.1065` n `151`; fx avg `-0.0062` n `6`; index avg `0.0276` n `26`; metal avg `0.0511` n `20`; unknown avg `0.0224` n `1136`
- 1h: commodity avg `-0.1338` n `13`; crypto_alt avg `0.7144` n `236`; crypto_major avg `0.6073` n `8`; equity avg `0.314` n `151`; fx avg `0.0003` n `6`; index avg `0.0647` n `26`; metal avg `0.0265` n `20`; unknown avg `0.3707` n `1134`
- 4h: commodity avg `0.1381` n `13`; crypto_alt avg `4.7836` n `236`; crypto_major avg `3.3114` n `8`; equity avg `1.91` n `151`; fx avg `0.0252` n `6`; index avg `0.301` n `26`; metal avg `0.0044` n `20`; unknown avg `3.2187` n `1082`
- 24h: commodity avg `-0.1058` n `13`; crypto_alt avg `0.8101` n `236`; crypto_major avg `0.7123` n `8`; equity avg `-1.655` n `151`; fx avg `0.1768` n `6`; index avg `-0.2483` n `26`; metal avg `0.3804` n `20`; unknown avg `0.213` n `938`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1015`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0872`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.086`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0834`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0757`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
