# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T16:52:28.057599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.4889` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.9739` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.3206` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0221` n `12`; crypto_alt avg `0.2954` n `232`; crypto_major avg `0.2276` n `8`; equity avg `0.0869` n `133`; fx avg `0.0031` n `6`; index avg `0.0175` n `26`; metal avg `-0.0103` n `20`; unknown avg `-0.2596` n `792`
- 1h: commodity avg `0.0732` n `12`; crypto_alt avg `0.0795` n `232`; crypto_major avg `-0.0333` n `8`; equity avg `0.0211` n `133`; fx avg `0.0249` n `6`; index avg `0.0027` n `26`; metal avg `-0.0011` n `20`; unknown avg `21.8405` n `790`
- 4h: commodity avg `-0.2512` n `12`; crypto_alt avg `2.0618` n `232`; crypto_major avg `3.2377` n `8`; equity avg `0.9171` n `133`; fx avg `0.0473` n `6`; index avg `0.1864` n `26`; metal avg `0.2638` n `20`; unknown avg `30.7602` n `790`
- 24h: commodity avg `-0.0703` n `12`; crypto_alt avg `4.2543` n `232`; crypto_major avg `5.3985` n `8`; equity avg `2.0617` n `133`; fx avg `-0.2726` n `6`; index avg `0.2118` n `26`; metal avg `0.9595` n `20`; unknown avg `24.8386` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
