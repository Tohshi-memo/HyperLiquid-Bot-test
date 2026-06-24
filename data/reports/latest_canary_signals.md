# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T23:54:09.034292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4138` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0463` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `-0.0577` n `228`; crypto_major avg `-0.031` n `8`; equity avg `0.002` n `86`; fx avg `0.0146` n `6`; index avg `-0.0274` n `23`; metal avg `-0.0208` n `20`; unknown avg `-0.223` n `764`
- 1h: commodity avg `0.0426` n `12`; crypto_alt avg `0.263` n `228`; crypto_major avg `0.3669` n `8`; equity avg `0.3843` n `86`; fx avg `0.0354` n `6`; index avg `-0.0134` n `23`; metal avg `0.0763` n `20`; unknown avg `-0.627` n `748`
- 4h: commodity avg `-0.0002` n `12`; crypto_alt avg `2.1699` n `228`; crypto_major avg `2.4136` n `8`; equity avg `2.9919` n `86`; fx avg `-0.0016` n `6`; index avg `0.6118` n `23`; metal avg `0.3673` n `20`; unknown avg `2.9828` n `748`
- 24h: commodity avg `-0.4188` n `12`; crypto_alt avg `-2.1029` n `228`; crypto_major avg `-1.7889` n `8`; equity avg `5.4036` n `86`; fx avg `0.0437` n `6`; index avg `0.599` n `23`; metal avg `-1.4629` n `20`; unknown avg `-1.3711` n `716`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
