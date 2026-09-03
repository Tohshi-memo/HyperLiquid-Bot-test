# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T17:52:36.018312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.3791` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6152` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9699` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0225` n `12`; crypto_alt avg `0.1495` n `232`; crypto_major avg `-0.0056` n `8`; equity avg `0.0911` n `133`; fx avg `-0.0023` n `6`; index avg `0.0224` n `26`; metal avg `-0.0135` n `20`; unknown avg `0.0789` n `792`
- 1h: commodity avg `-0.0152` n `12`; crypto_alt avg `0.1881` n `232`; crypto_major avg `0.1086` n `8`; equity avg `0.1425` n `133`; fx avg `0.0063` n `6`; index avg `0.0259` n `26`; metal avg `0.0483` n `20`; unknown avg `2.6295` n `790`
- 4h: commodity avg `-0.2986` n `12`; crypto_alt avg `2.5363` n `232`; crypto_major avg `3.0805` n `8`; equity avg `1.1106` n `133`; fx avg `0.0508` n `6`; index avg `0.1615` n `26`; metal avg `0.4653` n `20`; unknown avg `3.7218` n `790`
- 24h: commodity avg `-0.0253` n `12`; crypto_alt avg `4.4352` n `232`; crypto_major avg `5.3604` n `8`; equity avg `1.9514` n `133`; fx avg `-0.2572` n `6`; index avg `0.2011` n `26`; metal avg `0.9264` n `20`; unknown avg `0.9352` n `736`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
