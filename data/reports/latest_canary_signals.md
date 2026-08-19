# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T21:22:26.825570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `6.182` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `5.5608` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `5.0193` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `3.2624` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `3.1858` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.9576` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0247` n `12`; crypto_alt avg `-0.1214` n `230`; crypto_major avg `0.3847` n `8`; equity avg `0.0034` n `121`; fx avg `0.0012` n `6`; index avg `-0.011` n `25`; metal avg `-0.0039` n `20`; unknown avg `-0.0017` n `792`
- 1h: commodity avg `0.0499` n `12`; crypto_alt avg `1.8903` n `230`; crypto_major avg `3.3123` n `8`; equity avg `0.3547` n `121`; fx avg `-0.0247` n `6`; index avg `0.0567` n `25`; metal avg `0.1265` n `20`; unknown avg `0.3684` n `792`
- 4h: commodity avg `-0.3124` n `12`; crypto_alt avg `2.92` n `230`; crypto_major avg `5.8696` n `8`; equity avg `0.8503` n `121`; fx avg `-0.0318` n `6`; index avg `0.0553` n `25`; metal avg `0.3088` n `20`; unknown avg `1.5939` n `792`
- 24h: commodity avg `-0.0348` n `12`; crypto_alt avg `6.0002` n `230`; crypto_major avg `10.5682` n `8`; equity avg `0.5338` n `120`; fx avg `-0.232` n `6`; index avg `0.0705` n `25`; metal avg `1.2455` n `20`; unknown avg `1.2823` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2222`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
