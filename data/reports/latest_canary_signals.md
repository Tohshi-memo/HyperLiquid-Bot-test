# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T15:37:28.004596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.5112` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.3884` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8563` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1143` n `12`; crypto_alt avg `0.3485` n `232`; crypto_major avg `0.0873` n `8`; equity avg `0.1833` n `133`; fx avg `-0.0352` n `6`; index avg `0.0257` n `26`; metal avg `0.0111` n `20`; unknown avg `-0.1394` n `792`
- 1h: commodity avg `-0.2952` n `12`; crypto_alt avg `1.3403` n `232`; crypto_major avg `1.2815` n `8`; equity avg `0.9722` n `133`; fx avg `0.0139` n `6`; index avg `0.2016` n `26`; metal avg `0.4043` n `20`; unknown avg `0.3406` n `790`
- 4h: commodity avg `-0.4383` n `12`; crypto_alt avg `1.8727` n `232`; crypto_major avg `3.0729` n `8`; equity avg `1.2166` n `133`; fx avg `-0.0221` n `6`; index avg `0.2607` n `26`; metal avg `0.6845` n `20`; unknown avg `22.4504` n `790`
- 24h: commodity avg `-0.0751` n `12`; crypto_alt avg `3.9364` n `232`; crypto_major avg `4.7051` n `8`; equity avg `1.8831` n `133`; fx avg `-0.2849` n `6`; index avg `0.1795` n `26`; metal avg `1.0053` n `20`; unknown avg `0.7738` n `736`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
