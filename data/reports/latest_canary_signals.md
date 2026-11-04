# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T15:22:29.189184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.4983` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `3.0077` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `2.9052` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `2.6418` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `2.4764` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.3503` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0648` n `13`; crypto_alt avg `-0.0168` n `239`; crypto_major avg `-0.0798` n `8`; equity avg `-0.4602` n `158`; fx avg `-0.0018` n `6`; index avg `-0.0402` n `27`; metal avg `-0.0578` n `20`; unknown avg `4.295` n `1262`
- 1h: commodity avg `0.1462` n `13`; crypto_alt avg `2.6672` n `239`; crypto_major avg `3.0514` n `8`; equity avg `0.575` n `158`; fx avg `-0.0142` n `6`; index avg `0.0797` n `27`; metal avg `0.0437` n `20`; unknown avg `2.2955` n `1256`
- 4h: commodity avg `-0.3409` n `13`; crypto_alt avg `1.5256` n `239`; crypto_major avg `2.3009` n `8`; equity avg `-1.1974` n `158`; fx avg `0.0097` n `6`; index avg `0.0247` n `27`; metal avg `-0.0494` n `20`; unknown avg `1.0213` n `1252`
- 24h: commodity avg `-0.4628` n `13`; crypto_alt avg `3.4652` n `239`; crypto_major avg `3.2587` n `8`; equity avg `0.3215` n `158`; fx avg `0.1218` n `6`; index avg `0.158` n `27`; metal avg `0.8763` n `20`; unknown avg `0.6049` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2598`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
