# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T15:22:38.342987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.5371` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5661` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.329` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0661` n `12`; crypto_alt avg `-0.0003` n `232`; crypto_major avg `-0.2679` n `8`; equity avg `0.1219` n `133`; fx avg `0.0266` n `6`; index avg `0.0286` n `26`; metal avg `0.0576` n `20`; unknown avg `0.0399` n `792`
- 1h: commodity avg `-0.2569` n `12`; crypto_alt avg `1.1087` n `232`; crypto_major avg `1.7117` n `8`; equity avg `0.6572` n `133`; fx avg `0.0531` n `6`; index avg `0.125` n `26`; metal avg `0.3894` n `20`; unknown avg `0.2844` n `790`
- 4h: commodity avg `-0.2643` n `12`; crypto_alt avg `1.7454` n `232`; crypto_major avg `3.2728` n `8`; equity avg `0.9438` n `133`; fx avg `0.0352` n `6`; index avg `0.2387` n `26`; metal avg `0.7067` n `20`; unknown avg `23.7879` n `790`
- 24h: commodity avg `0.0451` n `12`; crypto_alt avg `3.8981` n `232`; crypto_major avg `4.872` n `8`; equity avg `1.8212` n `133`; fx avg `-0.2412` n `6`; index avg `0.1701` n `26`; metal avg `0.9853` n `20`; unknown avg `0.7298` n `736`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
