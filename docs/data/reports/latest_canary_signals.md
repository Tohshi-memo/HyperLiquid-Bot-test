# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T17:37:28.029477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.4383` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.7935` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8178` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1662` n `12`; crypto_alt avg `0.1388` n `232`; crypto_major avg `0.2985` n `8`; equity avg `0.0748` n `133`; fx avg `-0.0041` n `6`; index avg `0.0245` n `26`; metal avg `0.022` n `20`; unknown avg `0.0302` n `792`
- 1h: commodity avg `0.0299` n `12`; crypto_alt avg `0.333` n `232`; crypto_major avg `0.342` n `8`; equity avg `0.1379` n `133`; fx avg `0.0116` n `6`; index avg `0.0209` n `26`; metal avg `0.0515` n `20`; unknown avg `2.3029` n `790`
- 4h: commodity avg `-0.2262` n `12`; crypto_alt avg `2.3793` n `232`; crypto_major avg `3.2121` n `8`; equity avg `1.3943` n `133`; fx avg `0.0339` n `6`; index avg `0.2145` n `26`; metal avg `0.4186` n `20`; unknown avg `27.8417` n `790`
- 24h: commodity avg `-0.043` n `12`; crypto_alt avg `4.4857` n `232`; crypto_major avg `5.6681` n `8`; equity avg `1.97` n `133`; fx avg `-0.2584` n `6`; index avg `0.208` n `26`; metal avg `1.0077` n `20`; unknown avg `23.3977` n `736`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
