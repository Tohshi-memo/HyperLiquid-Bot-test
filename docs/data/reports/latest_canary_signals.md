# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T16:22:30.751122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.8984` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.8546` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.1226` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.1413` n `232`; crypto_major avg `-0.006` n `8`; equity avg `0.0766` n `133`; fx avg `0.0143` n `6`; index avg `0.0042` n `26`; metal avg `0.0103` n `20`; unknown avg `21.6901` n `792`
- 1h: commodity avg `-0.1953` n `12`; crypto_alt avg `0.379` n `232`; crypto_major avg `0.3927` n `8`; equity avg `0.22` n `133`; fx avg `-0.0225` n `6`; index avg `0.0276` n `26`; metal avg `-0.0457` n `20`; unknown avg `22.2995` n `790`
- 4h: commodity avg `-0.4258` n `12`; crypto_alt avg `1.9517` n `232`; crypto_major avg `3.4726` n `8`; equity avg `1.35` n `133`; fx avg `0.0462` n `6`; index avg `0.2838` n `26`; metal avg `0.618` n `20`; unknown avg `31.1419` n `790`
- 24h: commodity avg `-0.156` n `12`; crypto_alt avg `3.5003` n `232`; crypto_major avg `4.6519` n `8`; equity avg `1.8308` n `133`; fx avg `-0.2708` n `6`; index avg `0.1792` n `26`; metal avg `0.941` n `20`; unknown avg `0.5756` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
