# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T23:37:27.504327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4669` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.009` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `0.1655` n `228`; crypto_major avg `0.074` n `8`; equity avg `0.0889` n `86`; fx avg `0.0262` n `6`; index avg `0.0078` n `23`; metal avg `0.0959` n `20`; unknown avg `0.0621` n `764`
- 1h: commodity avg `0.0473` n `12`; crypto_alt avg `0.0782` n `228`; crypto_major avg `0.213` n `8`; equity avg `0.2989` n `86`; fx avg `0.0183` n `6`; index avg `0.0215` n `23`; metal avg `0.0012` n `20`; unknown avg `-0.5088` n `748`
- 4h: commodity avg `-0.0038` n `12`; crypto_alt avg `2.2632` n `228`; crypto_major avg `2.4631` n `8`; equity avg `3.057` n `86`; fx avg `-0.0279` n `6`; index avg `0.6961` n `23`; metal avg `0.4541` n `20`; unknown avg `3.0885` n `748`
- 24h: commodity avg `-0.4365` n `12`; crypto_alt avg `-1.8476` n `228`; crypto_major avg `-1.5199` n `8`; equity avg `5.6082` n `86`; fx avg `0.0575` n `6`; index avg `0.6822` n `23`; metal avg `-1.2475` n `20`; unknown avg `-0.3041` n `716`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
