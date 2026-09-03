# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T18:22:29.063181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8762` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0986` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0221` n `12`; crypto_alt avg `-0.0614` n `232`; crypto_major avg `-0.1181` n `8`; equity avg `-0.0098` n `133`; fx avg `0.0027` n `6`; index avg `-0.0026` n `26`; metal avg `0.0001` n `20`; unknown avg `1.6228` n `792`
- 1h: commodity avg `-0.2514` n `12`; crypto_alt avg `0.375` n `232`; crypto_major avg `0.2215` n `8`; equity avg `0.202` n `133`; fx avg `-0.0047` n `6`; index avg `0.0614` n `26`; metal avg `-0.0137` n `20`; unknown avg `2.5397` n `790`
- 4h: commodity avg `-0.436` n `12`; crypto_alt avg `2.1906` n `232`; crypto_major avg `2.4402` n `8`; equity avg `1.1587` n `133`; fx avg `0.044` n `6`; index avg `0.208` n `26`; metal avg `0.3416` n `20`; unknown avg `1.5462` n `790`
- 24h: commodity avg `-0.1582` n `12`; crypto_alt avg `4.5008` n `232`; crypto_major avg `5.1801` n `8`; equity avg `1.6265` n `133`; fx avg `-0.2615` n `6`; index avg `0.2024` n `26`; metal avg `0.913` n `20`; unknown avg `1.0993` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
