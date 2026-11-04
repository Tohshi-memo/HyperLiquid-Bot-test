# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T18:22:32.318799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2067` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.9207` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.0022` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1505` n `13`; crypto_alt avg `-0.2999` n `239`; crypto_major avg `-0.1026` n `8`; equity avg `-0.3215` n `158`; fx avg `0.0023` n `6`; index avg `-0.0276` n `27`; metal avg `-0.0289` n `20`; unknown avg `3.5942` n `1264`
- 1h: commodity avg `0.328` n `13`; crypto_alt avg `-0.0638` n `239`; crypto_major avg `0.1414` n `8`; equity avg `-0.3608` n `158`; fx avg `0.0026` n `6`; index avg `-0.0234` n `27`; metal avg `0.0457` n `20`; unknown avg `3.6555` n `1258`
- 4h: commodity avg `-0.867` n `13`; crypto_alt avg `1.3252` n `239`; crypto_major avg `2.3397` n `8`; equity avg `-0.581` n `158`; fx avg `-0.0414` n `6`; index avg `0.0667` n `27`; metal avg `0.3375` n `20`; unknown avg `2.8277` n `1250`
- 24h: commodity avg `-1.4295` n `13`; crypto_alt avg `1.9305` n `239`; crypto_major avg `2.2625` n `8`; equity avg `-0.785` n `158`; fx avg `0.0596` n `6`; index avg `0.1409` n `27`; metal avg `1.2129` n `20`; unknown avg `0.6095` n `1115`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2724`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
