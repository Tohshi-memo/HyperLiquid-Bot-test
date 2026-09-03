# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T17:22:31.695420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9905` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5634` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0418` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0778` n `12`; crypto_alt avg `-0.0009` n `232`; crypto_major avg `-0.0232` n `8`; equity avg `-0.007` n `133`; fx avg `0.003` n `6`; index avg `-0.0184` n `26`; metal avg `0.0124` n `20`; unknown avg `0.0023` n `792`
- 1h: commodity avg `0.2724` n `12`; crypto_alt avg `0.307` n `232`; crypto_major avg `0.094` n `8`; equity avg `0.0731` n `133`; fx avg `0.018` n `6`; index avg `-0.0065` n `26`; metal avg `0.0116` n `20`; unknown avg `2.4013` n `790`
- 4h: commodity avg `-0.0754` n `12`; crypto_alt avg `2.0774` n `232`; crypto_major avg `2.9151` n `8`; equity avg `0.8733` n `133`; fx avg `0.0407` n `6`; index avg `0.1639` n `26`; metal avg `0.3517` n `20`; unknown avg `9.6899` n `790`
- 24h: commodity avg `0.1101` n `12`; crypto_alt avg `4.5359` n `232`; crypto_major avg `5.5939` n `8`; equity avg `1.8718` n `133`; fx avg `-0.2498` n `6`; index avg `0.1741` n `26`; metal avg `1.0049` n `20`; unknown avg `22.3738` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
