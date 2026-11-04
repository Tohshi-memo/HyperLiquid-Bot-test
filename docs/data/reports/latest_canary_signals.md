# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T16:37:41.293174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `4.2665` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `3.8173` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6339` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.4064` n `13`; crypto_alt avg `-0.1206` n `239`; crypto_major avg `-0.1484` n `8`; equity avg `-0.0885` n `158`; fx avg `-0.0083` n `6`; index avg `0.0026` n `27`; metal avg `0.0755` n `20`; unknown avg `3.8527` n `1264`
- 1h: commodity avg `-1.0205` n `13`; crypto_alt avg `-0.5669` n `239`; crypto_major avg `-0.2926` n `8`; equity avg `-1.5776` n `158`; fx avg `-0.0178` n `6`; index avg `-0.1259` n `27`; metal avg `0.0871` n `20`; unknown avg `0.2646` n `1252`
- 4h: commodity avg `-1.0809` n `13`; crypto_alt avg `1.7838` n `239`; crypto_major avg `2.7364` n `8`; equity avg `-1.5301` n `158`; fx avg `-0.028` n `6`; index avg `-0.0228` n `27`; metal avg `0.1025` n `20`; unknown avg `0.4382` n `1250`
- 24h: commodity avg `-1.2949` n `13`; crypto_alt avg `2.6462` n `239`; crypto_major avg `2.6715` n `8`; equity avg `-1.1651` n `158`; fx avg `0.0838` n `6`; index avg `0.0574` n `27`; metal avg `1.0338` n `20`; unknown avg `0.127` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.263`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
